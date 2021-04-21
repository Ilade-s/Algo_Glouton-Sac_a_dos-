"""
Implémentation d'un algorithme des k plus proches voisins
Fait à partir de https://cache.media.eduscol.education.fr/file/NSI/76/6/RA_Lycee_G_NSI_algo_knn_1170766.pdf

"""
import pandas
import matplotlib.pyplot as plt

iris = pandas.read_csv("DataKvoisins/iris.csv")
x = iris.loc[:, "petal_length"]
y = iris.loc[:, "petal_width"]
lab = iris.loc[:, "species"]
plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')
plt.scatter(x[lab == 1], y[lab == 1], color='r', label='virginica')
plt.scatter(x[lab == 2], y[lab == 2], color='b', label='versicolor')
plt.legend()
plt.xlim((0, 7))
plt.ylim((0, 2.5))
plt.show()
