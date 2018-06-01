'''
interfaz que tiene la responsabilidad de procesar distintas solicitudes y hacer los calculos con respecto a los
valores entregados, permite calcular los centroides, las distancias maximas y minimas al centroide, la desviacion
estandar de la muestra, etc...
'''

import numpy as np
import math

class processOption(object):

    def __init__(self):#instancia de un constructor vacio...
        super(processOption, self).__init__()

    #metodo que permite hacer el calculo del centroide...
    def calculateCentroide(self, ListVector):

        centroide = []
        for i in range (len(ListVector[0])):
            col = []
            for j in range(len(ListVector)):
                col.append(ListVector[j][i])
            centroide.append(np.mean(col))
        return centroide

    #metodo interno para calcular distancias entre vectores...
    def calculateDistanceVectors(self, vectorA, vectorB):

        sumData = 0

        for i in range(len(vectorA)):
            dist = (vectorA[i] - vectorB[i])**2
            sumData+=dist
        return math.sqrt(sumData)

    #metodo que permite calcular la distancia maxima y la minima al centroide...
    def calculateMaxMinDistanceToCentroide(self, ListVector, centroide):

        distances = []
        for vector in ListVector:
            distances.append(self.calculateDistanceVectors(vector, centroide))

        maxDist = max(distances)
        minDist = min(distances)

        return maxDist, minDist
