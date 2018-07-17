'''
clase que tiene la responsabilidad de generar un linechart mutiple con respecto a la cantidad de elementos que existan en la lista que recibe como argumento...
El objetivo general es crear una representacion para la visualizacion de las diferentes accuracy obtenidas en una division generada para las diferentes distribuciones
existentes en ella...
'''

#modulos a manejar...
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class multipleLineChart(object):

    def __init__(self, pathOutput, pathInput, numberGroups):

        self.pathInput = pathInput
        self.pathOutput = pathOutput
        self.numberGroups = numberGroups
        self.dictValues = {}
        self.ListGroups = ['A', 'B', 'C', 'F', 'H', 'M', 'N', 'O', 'P', 'R', 'T', 'U', 'Z']
        self.readListInDir()
        self.colorList = ['olive', 'orangered', 'green', 'darkblue', 'cyan', 'crimson', 'seagreen', 'firebrick', 'chocolate', 'maroon', 'skyblue', 'teal', 'red']
    #metodo que hace las lecturas de los documentos y forma las listas...
    def readListInDir(self):

        self.dictValues.update({'x':range(1,101)})
        self.colList = []
        for i in range (1, self.numberGroups+1):

            #formamos el nombre del archivo...
            nameFile = "%shistogramData_Group_group_%s_performance_accuracy.csv" % (self.pathInput, self.ListGroups[i-1])
            dataValues = pd.read_csv(nameFile)
            key = "G%d" % i
            data = []
            for j in range (len(dataValues['dataInfo'])):
                data.append(dataValues['dataInfo'][j])
            self.dictValues.update({key:data})
            self.colList.append(key)


    #metodo que permite hacer el grafico de interes...
    def makeGraphs(self):

        self.dictValues = pd.DataFrame(self.dictValues)
        pos=0
        for element in self.colList:
            plt.plot('x', element, data=self.dictValues, marker='', color=self.colorList[pos], linewidth=2)
            pos+=1
        plt.legend()
        title = "Accuracy for groups in distribution for sampling with %d elements" % self.numberGroups
        plt.title(title, loc='center', fontsize=16, fontweight=0)
        nameFig = "%sPerformanceLine.png" % self.pathOutput
        plt.savefig(nameFig)
