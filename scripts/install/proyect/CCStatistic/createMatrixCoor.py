'''
clase que tiene la responsabilidad de crear la matriz de correlacion de los datos.
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class correlationMatrix(object):

    def __init__(self, dataSet, header, pathFile, title):

        self.dataSet = dataSet
        self.header = header
        self.pathFile = pathFile
        self.title = title
        self.createDataFrame()

    #transformamos a float los elmentos de la matriz...
    def transformFloat(self):

        for i in range (len(self.dataSet)):
            for j in range (len(self.dataSet[i])-1):
                self.dataSet[i][j] = float(self.dataSet[i][j])

    #metodo que permite formar el data frame...
    def createDataFrame(self):

        self.transformFloat()
        self.df = pd.DataFrame(data=self.dataSet, columns=self.header)

    #metodo que permite exportar la matrix...
    def exportMatrixCor(self):

        correlation_matrix = self.df.corr()
        plt.figure(figsize=(30,28))
        heatmap = sns.heatmap(correlation_matrix, vmax=1, square=True, annot=False,fmt='.2f', cmap ='GnBu', cbar_kws={"shrink": .5}, robust=True)
        plt.title(self.title, fontsize=50)

        loc, labels = plt.xticks()
        heatmap.set_xticklabels(labels, rotation=45, fontsize=35)
        heatmap.set_yticklabels(labels[::-1], rotation=45, fontsize=35)
        plt.savefig(self.pathFile+"correlationMatrix.svg")
