'''
clase con la responsabilidad de generar distintos graficos de barras con respecto a la comparacion de los modelos de interes v/s los restantes modelos de otras divisiones
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class barChartModels(object):

    def __init__(self, pathInput, pathOutput, group):

        self.pathInput = pathInput
        self.pathOutput = pathOutput
        self.group = group
        self.ListGroups = ['grupo1','grupo2', 'grupo3','grupo4','grupo5','grupo6','grupo7']
        #self.ListGroups = ['1', '2', '3', '4', '5', '6', '7', '8']

    #metodo que permite hacer las lecturas de todos las comparaciones generadas para cada modelo...
    def readDocuments(self):

        self.pandasFiles = []

        for element in self.ListGroups:
            if element != self.group:
                nameFile = "%sexportResultPredict_%s.csv" % (self.pathInput, element)
                #nameFile = "%sexportResultPredict_%s.csv" % (self.pathInput, element)
                self.pandasFiles.append(pd.read_csv(nameFile))

    #metodo que permite hacer los graficos por cada modelo...
    def makeGraphsByModel(self):

        #recolectamos la data...
        for i in range (len(self.pandasFiles[0]['algorithm'])):#para cada modelo existente
            print i
            dataGraph = []
            for j in range(len(self.pandasFiles)):#para cada documento...

                if j==0:#agregamos la data inicial y la data del modelo a comparar...
                    dataGraph.append(self.pandasFiles[j]['actualScore'][i])
                    dataGraph.append(self.pandasFiles[j]['new score'][i])
                else:
                    dataGraph.append(self.pandasFiles[j]['new score'][i])

            #formamos la data para crear el grafico...
            nameExport = "%s%s_modelIndex%d" % (self.pathOutput, self.group, i)
            xTicks = [x for x in self.ListGroups if (x != self.group)]
            xTicksFull = [self.group]
            for element in xTicks:
                xTicksFull.append(element)
            title = "Compare Model %s %s for group %s" % (self.pandasFiles[0]['algorithm'][i], self.pandasFiles[0]['desc'][i], self.group)
            self.createBarChart(dataGraph, xTicksFull, nameExport, title)

    #metodo que permite hacer los graficos de barra...
    def createBarChart(self, listData, xTicks, nameExport, title):

        plt.figure()
        y_pos = np.arange(len(xTicks))
        plt.bar(y_pos, listData, color = (0.5,0.1,0.5,0.6))
        plt.xticks(y_pos, xTicks, rotation=45)
        plt.title(title, fontsize=12)
        plt.savefig(nameExport)
