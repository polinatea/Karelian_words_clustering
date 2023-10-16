# Karelian_words_clustering
Dialects of the Karelian language are territorial variants of the Karelian language, distributed mainly in the Republic of Karelia, as well as in the Leningrad, Novgorod and Tver regions of the Russian Federation. In addition, a number of speakers of Karelian dialects live in eastern and southeastern Finland.
From the way the dialects of the Karelian language are formed, one can see the processes of formation of the Karelian people, languages, as well as population movements that occurred before the 19th century. [1] Each territory has its own “dialect”.
When studying linguistics, there has always been the problem of collecting data, processing the collected data and comparing dialects with each other. To solve this problem, there is a clustering task - it allows you to combine large amounts of data into groups based on various characteristics for further work with them.
The website murreh is a dialect database of the Karelian language. The dictionary was prepared by employees of the linguistics sector of the Institute of Language, Literature and History of the Karelian Scientific Center of the Russian Academy of Sciences based on data collected in 1979–1981 during expeditionary work in 24 Karelian, 6 Vepsian and 5 Sami points. Each word has a set of characteristics and a geographical reference[2].
The purpose of this course work is to perform clustering of words according to a given criterion, as well as visualize the resulting groups of words on a map.

This course work will use the complete-linkage method, also known as the far-neighbor method, which belongs to hierarchical clustering.

As can be seen in Figure 1, the visualization of clustering results is a map with the coordinates of settlements plotted. Different clusters are colored differently. You can view the name of a settlement by hovering your mouse over the point. Matplotlib also allows you to scale the plot in real time.
Figure 1 shows a visualization of clustering based on the “diphthong” feature. You can see that the number of colors is 5, corresponding to the number of clusters. Clusters of dots that have the same color indicate that in a given place the residents use the same dialect.

![image](https://github.com/polinatea/Karelian_words_clustering/assets/67418401/6cbc0d96-dc06-4938-ae7d-d7a326ba004a)
Fig 1. Visualization of clustering based on the “Diphthongs” feature
