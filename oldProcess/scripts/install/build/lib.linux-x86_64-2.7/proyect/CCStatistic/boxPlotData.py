'''
clase que tiene la responsabilidad de almacenar la informacion con respecto a la data necesaria para generar un box plot
y almacenarlo como imagen...
'''

import numpy as np
import matplotlib.pyplot as plt

class boxPlotObject(object):

    def __init__(self, dataSet, header, pathOutput):

        self.header = header[:-1]#sin la clase...
        self.dataSet = dataSet
        self.pathOutput = pathOutput
        self.processData()

    #metodo que permite procesar la informacion, quitando el atributo columna de la matriz...
    def processData(self):

        for i in range(len(self.dataSet)):
            self.dataSet[i].pop(len(self.dataSet[i])-1)
            for j in range(len(self.dataSet[i])):
                self.dataSet[i][j] = float(self.dataSet[i][j])

    #metodo que permite hacer el box plot...
    def createBoxPlot(self):

        plt.boxplot(self.dataSet)
        plt.show()
