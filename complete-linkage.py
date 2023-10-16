from numpy import append
import pymysql
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from numpy import append
#server connection
mydb = pymysql.connect(
  host="localhost",
    database="murreh",
    user = 'root'
)

mycursor = mydb.cursor() #cursor created
q = "Гармония"

mycursor.execute("select qsections.id from qsections where title = %s",(q))
rows = mycursor.fetchall()


for row in rows:
    s = row
qsectionId = s[0]

mycursor.execute("select distinct answers.answer,places.name_ru, questions.question from places, \
  answers, anketas, anketa_question, questions, qsections where (anketas.place_id = places.id)\
     and (anketas.id =anketa_question.anketa_id) and (anketa_question.answer_id = answers.id) \
       and (anketa_question.question_id = questions.id) and (questions.qsection_id = qsections.id)\
          and (qsections.id = %s) order by questions.question;",(qsectionId))
rows = mycursor.fetchall()


max_distance_global = 0
def difference_table(data, clusters):
    global max_distance_global
    #Creating empty matrix
    v=[0]*len(clusters)
    d_matrix = []
    for i in range(len(clusters)):
        d_matrix.append(list(v))

    min_distance=-1
    min_points=(0,0)

    #Filling the matrix

    #Loops through clusters up->down
    for i in range(len(clusters)):

        #Loops through cluster left->right
        for j in range(0, i):

            max_distance = -1
            #Looping through cities INSIDE clusters
            for l in clusters[i]:
                for m in clusters[j]:
                    distance=0

                    #Loops through mua and karel
                    for k in range(len(data)):

                        equals=False
                        #Check if they have equal element:
                        for elem_1 in data[k][l]: # правее 
                            for elem_2 in data[k][m]: # левее
                                if elem_1 == elem_2:
                                    equals=True
                        if equals == False:
                            distance += 1

                    if distance > max_distance: # сравниваем 2 и выбираем большее 
                        max_distance = distance

            d_matrix[i][j] = max_distance
            if max_distance < min_distance or min_distance == -1:
                min_distance = max_distance
                min_points = (i, j)

            if max_distance > max_distance_global:
                max_distance_global = max_distance

    return ((d_matrix, (min_distance, min_points)))



def create_first_clusters():
    clusters = []
    for i in range(len(data[0])):
        v=[]
        v.append(i)
        clusters.append(v)

    return (clusters)


city_list = []
questionIds = {}
citiesIds = {}
data = []

for t in rows: 
  # Если текущий вопрос еще не попадался
  if t[2] not in questionIds.keys():
    # берем айди согласно длине словаря айдишников
    questionInd = len(questionIds)
    # добавляем вопрос в словарь айдишников
    questionIds[t[2]] = questionInd
    # добавляем в лист data новый лист под новый вопрос
    data.append([])
    # добавляем к данному вопросу листы под все города
    for i in range(len(citiesIds)):
      data[questionInd].append([])

  # иначе берем индекс уже существующего вопроса
  else:
    questionInd = questionIds[t[2]]
  # если текущий город еще не в словаре айдишников
  if t[1] not in citiesIds.keys():
    # вычисляем будущий айдишник по длине словаря айдишников
    citiesInd = len(citiesIds)
    # добавляем город в словарь айдишников
    citiesIds[t[1]] = citiesInd
    # добавляем город в список городов (для вывода кластеров)
    city_list.append(t[1])
    # добавляем к данному вопросу лист для следующего города 
    for el in data:
      el.append([])
  # иначе берем индекс уже существующего города
  else:
    citiesInd = citiesIds[t[1]]

  # добавляем ответ соотвественно его индексам (вопросу и городу)
  data[questionInd][citiesInd].append(t[0])


clusters = create_first_clusters()


step = 0
while True:
    d_matrix_result = difference_table(data, clusters)

    d_matrix = d_matrix_result[0]
    min_distance=d_matrix_result[1][0]
    min_points=d_matrix_result[1][1]

    step += 1
    if min_distance >= max_distance_global:
        break

    clusters[min_points[0]] = clusters[min_points[0]] + clusters[min_points[1]]
    clusters.pop(min_points[1])


for i in range(len(clusters)):
    cluster=[]
    for city in clusters[i]:
        cluster.append(city_list[city])
    
    print("Cluster", i, "=", cluster)


colors = ["red","green","cyan","yellow","purple","black","orange","purple","beige","brown","gray","cyan","magenta"]

x_list = [0] * len(city_list)   # [x0  x1    x2  x3]
y_list = [0] * len(city_list)   # [y0  y1    y2  y3]
c_final = [0] * len(city_list)  # [red green red green]
for i in range(len(clusters)):
    for j in range(len(clusters[i])):
        c_final[clusters[i][j]] = colors[i]
        x_list[clusters[i][j]] = random.uniform(0.1, 10.0)
        y_list[clusters[i][j]] = random.uniform(0.1, 10.0)

fig,ax = plt.subplots()
sc = plt.scatter(x_list, y_list, c=c_final, alpha=0.8,s=20)     
annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
bbox=dict(boxstyle="round", fc="w"),
arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    text = city_list[ind["ind"][0]]
    annot.xy = pos
    annot.set_text(text)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
