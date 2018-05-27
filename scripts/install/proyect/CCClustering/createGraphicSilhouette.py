'''
clase que permite crear los graficos de coeficientes de siluetas...
recibe la matriz de datos y la lista de labels de grupos...
'''

from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class graphicSilhouette(object):

    def __init__(self, matrixData, groupLabel, n_clusters, clusterList):

        self.matrixData = matrixData
        self.groupLabel = groupLabel
        self.n_clusters = n_clusters
        self.clusterList = clusterList
        self.getValuesGroup()

    #metodo que permita crear los centros de cada grupo...
    def createCentroideVectorForGroup(self, groupData):
        centroideVector = []
        for i in range(len(groupData[0])):
            col=[]
            for j in range(len(groupData)):
                col.append(groupData[j][i])
            centroideVector.append(np.mean(col))
        return centroideVector

    #metodo que permite obtener los valores por grupo y calcular el centroide para cada vector...
    def getValuesGroup(self):
        self.centers = []
        for element in self.clusterList:
            clusterData = []
            for i in range(len(self.groupLabel)):
                if self.groupLabel[i] == element:
                    clusterData.append(self.matrixData[i])
            self.centers.append(self.createCentroideVectorForGroup(clusterData))

    #metodo que permite crear el grafico y obtener los valores de la performance...
    def createGraphic(self):

        # Create a subplot with 1 row and 2 columns
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(18, 7)
        ax1.set_xlim([-0.1, 1])
        ax1.set_ylim([0, len(self.matrixData) + (self.n_clusters + 1) * 10])
        self.silhouette_avg = silhouette_score(self.matrixData, self.groupLabel)

        print("For n_clusters =", self.n_clusters,
              "The average silhouette_score is :", self.silhouette_avg)
