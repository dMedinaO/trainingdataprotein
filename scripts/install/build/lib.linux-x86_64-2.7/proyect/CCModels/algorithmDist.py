'''
clase con la responsabilidad de buscar el algoritmo con la mejor performance y evaluar la cantidad de veces que aparece,
la idea es generar un barchart o piechart con dicha informacion y visualizar el contenido del mismo...
Como entrada, recibe el path donde se encuentra la division y la cantidad de grupos que son...
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class searchAlgorithm(object):

    def __init__(self, pathRoot, groups, pathOutput):

        self.pathRoot = pathRoot
        self.pathOutput = pathOutput
        self.groups = groups
        self.dictValues = {}#sera un doble diccionario, primero con la key del grupo y segundo con la key del algoritmo
        self.dictConts = {}#diccionario con la informacion de los grupos y sus respectivos contadores de algoritmos...
        self.ListGroups = ['A', 'B', 'C', 'F', 'H', 'M', 'N', 'O', 'P', 'R', 'T', 'U', 'Z']

    #metodo que permite hacer la busqueda de la informacion para obtener el mejor algoritmo por cada iteracion...
    def searchBestAlgorithm(self):

        for j in self.ListGroups:
            self.dictValues.update({str(j):{}})#el diccionario apuntara a un diccionario de los mejores algoritmos por iteracion...
            for i in range (1, 101):#para cada iteracion...
                #creamos el path y hacemos la lectura del documento...
                pathRead = "%s%d_iteration/group_%s/performanceTrainingWithLOU.csv" % (self.pathRoot, i, j)
                data =  pd.read_csv(pathRead)

                #search max accuracy...
                maxAccuracy = max(data['Accuracy'])
                listIteration = self.getAlgorithm(data, maxAccuracy)
                self.dictValues[str(j)].update({str(i):listIteration})

    #metodo que permite hacer la busqueda del algoritmo en base a la accuracy...
    def getAlgorithm(self, data, maxAccuracy):

        listAlgorithm = []
        for index in range (len(data['Accuracy'])):
            if data['Accuracy'][index] == maxAccuracy:
                listAlgorithm.append(data['algorithm'][index])## NOTE: puede que un valor lo entreguen varios algoritmos...
        return listAlgorithm

    #metodo que permite hacer el conteo de cada algoritmo por grupo...
    def createCountForGroup(self, group):

        listAlgorithm = []
        for iteration in self.dictValues[group]:
            for element in self.dictValues[group][iteration]:
                listAlgorithm.append(element)

        return listAlgorithm

    #metodo que recibe una lista y retorna un diccionario con el numero de apariciones de cada elemento en ella...
    def countValuesInDict(self, listData):

        listUnique = list(set(listData))
        dictResponse = {}

        for element in listUnique:
            cont=0
            for value in listData:
                if element == value:
                    cont+=1
            dictResponse.update({element:cont})
        return dictResponse

    #metodo general de busqueda de elementos...
    def searchCountValues(self):

        for group in self.dictValues:
            self.dictConts.update({group:self.countValuesInDict(self.createCountForGroup(group))})

    #metodo que permite crear los graficos por cada grupo...
    def createPieChart(self):

        for group in self.dictConts:

            #obtenemos los labels y los valores...
            values = []
            labels = []

            for data in self.dictConts[group]:
                labels.append(data)
                values.append(self.dictConts[group][data])

            y_pos = np.arange(len(labels))

            plt.figure(figsize=(15,15))
            # Create bars and choose color
            plt.bar(y_pos, values, color = (0.5,0.1,0.5,0.6))

            # Add title and axis names
            plt.title('Algorithms with best performance')
            plt.xlabel('Algorithm')
            plt.ylabel('Count')

            # Create names
            plt.xticks(y_pos, labels)
            plt.xticks(rotation=45)
            #save fig
            namePict = "%s%s_algorithms.png" % (self.pathOutput, group)
            plt.savefig(namePict)
