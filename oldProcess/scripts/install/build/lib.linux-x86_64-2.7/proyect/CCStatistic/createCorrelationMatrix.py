'''
clase con la responsabilidad de generar la matriz de correlacion, exporta la imagen y el archivo csv...
recibe como entrada el archivo con la data normalizada y el path de salida...
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class correlationMatrix(object):

    def __init__(self, matrixName, pathOutput):

        self.matrixName = matrixName
        self.pathOutput = pathOutput

    #modulo para crear la matrix...
    def createCorrelationMatrixData(self):

        self.df = pd.read_csv(self.matrixName)
        correlation_matrix = self.df.corr()
        plt.figure(figsize=(30,28))
        heatmap = sns.heatmap(correlation_matrix)
        #plt.title("Correlation Matrix for data set", fontsize=50)

        loc, labels = plt.xticks()
        heatmap.set_xticklabels(labels, rotation=45, fontsize=20)
        heatmap.set_yticklabels(labels[::-1], rotation=45, fontsize=20)
        plt.savefig(self.pathOutput+"correlationMatrix.svg")
        correlation_matrix.to_csv(self.pathOutput+"correlationMatrix.csv")
