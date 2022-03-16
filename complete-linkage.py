#! /usr/bin/python

# data = np.array([
#         [0.05, 0.95],
#         [0.1, 0.9],
#         [0.2, 0.8],
#         [0.25, 0.75],
#         [0.45, 0.55],
#         [0.5, 0.5],
#         [0.55, 0.45],
#         [0.85, 0.15],
#         [0.9, 0.1],
#         [0.95, 0.05]])

# data = np.array([
#         [0.40, 0.53],
#         [0.22, 0.38],
#         [0.35, 0.32],
#         [0.26, 0.19],
#         [0.08, 0.41],
#         [0.45, 0.30]])

#         [],
#         [[0.35, 0.32], [0.45, 0.30], [0.22, 0.38], [0.40, 0.53]],
#         [0.26, 0.19],
#         [0.08, 0.41]])

# x = data[:,0]
# y= data[:,1]

# df = pd.DataFrame(data, columns=['x', 'y'])
# print(df)

def create_data(city_list):
    dict_1 = []
    dict_2 = []

    for i in range(len(city_list)):
        dict_1.append(city_list[i]["words"][0])
        dict_2.append(city_list[i]["words"][1])


    data = (dict_1, dict_2)
    print (data)
    return(data)

# def euclid_dist(x, y):
#     return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

#def distance_matrix(data):
#    #Creating empty matrix
#    v=[0]*len(data)
#    d_matrix = []
#    for i in range(len(data)):
#        d_matrix.append(list(v))

#    min_value=np.Infinity
#    min_points=(0, 0)

#    #Filling the matrix
#    for i in range(len(data)):
#        for j in range(0, i):
#            dist = euclid_dist(data[i], data[j])
#            d_matrix[i][j] = dist

#            #Saving minimum value for later usage
#            if dist < min_value:
#                min_value = dist
#                min_points = (i, j)


#    return((d_matrix, (min_value, min_points)))

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


if __name__ == "__main__":
    city_list = [{"city": "Габозеро",
                "words": [["a"],["a", "c"]]},

                {"city": "Саригора",
                "words": [["b"],["b"]]},

                {"city": "Койкоры",
                "words": [["a", "c"], ["c"]]},

                {"city": "Виданы",
                "words": [["d"], ["b"]]}]
                
    print("city_list = ", type(city_list))
    data = create_data(city_list)
    print(type(data))
    clusters = create_first_clusters()
    print("Data: ", data)
    print("Clusters: ", clusters)

    step = 0
    while True:
        d_matrix_result = difference_table(data, clusters)

        d_matrix = d_matrix_result[0]
        min_distance=d_matrix_result[1][0]
        min_points=d_matrix_result[1][1]

        print("Difference matrix for step", step)
        for elem in d_matrix:
            print(elem)
        print()
        print("Min distance: ", min_distance, " from points: ", min_points)
        print()
        print()


        step += 1
        if min_distance >= max_distance_global:
            break

        clusters[min_points[0]] = clusters[min_points[0]] + clusters[min_points[1]]
        clusters.pop(min_points[1])

        # print(clusters)

for i in range(len(clusters)):
    cluster=[]
    for city in clusters[i]:
        cluster.append(city_list[city]["city"])
    
    print("Cluster", i, "=", cluster)