'''
clase que tiene la responsabilidad de generar un scatter plot de los datos,
recibe un data frame con la data a exportar, ademas del nombre de archivo para guardar la imagen...
'''

import pandas as pd
import seaborn as sns

class scatterMatrixPlot(object):

    def __init__(self, dataSet, header, pathFile, attribute):

        self.dataSet = dataSet
        self.header = header
        self.pathFile = pathFile
        self.attribute = attribute
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
    def exportScatter(self):
        sns.set(style="ticks")
        sns_plot = sns.pairplot(self.df, hue=self.attribute)
        sns_plot.savefig(self.pathFile+"scatterPlotMatrix.svg")
