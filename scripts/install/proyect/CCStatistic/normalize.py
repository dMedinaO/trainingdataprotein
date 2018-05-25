'''
script que recibe una matriz de datos y una lista de header y calcula la normalizacion de datos...
hace la llamada al modulo document para generar el archivo a exportar
Tambien recibe un path donde se almacenara el resultado
'''

#modulos a trabajar...
from proyect.CCProcesFile import document #para hacer la instancia a la clase de lectura y escritura de archivos...
from sklearn import preprocessing
import numpy as np
import os
import sys
import pandas as pd

class NormalizeData(object):

    def __init__(self, header, matrix, pathOutput):#constructor de la clase

        self.header = header
        self.matrix = matrix
        self.pathOutput = pathOutput
        self.matrixNormalized = []
        self.classData = []

    #metodo que permite obtener los datos de la matriz sin la columna clase...
    def removeAttributeClass(self):

        for element in self.matrix:
            self.matrixNormalized.append(element[:-1])#el conjunto de elementos...
            self.classData.append(element[-1])#el atributo clase...

    #metodo que permite hacer la union de los datos con la clase...
    def makeUnionData(self):
        matrixJoin = []
        for i in range (len(self.matrixNormalized)):
            row = []
            for j in range (len(self.matrixNormalized[i])):
                row.append(self.matrixNormalized[i][j])
            #agregamos la clase...
            row.append(self.classData[i])
            matrixJoin.append(row)
        self.matrixNormalized = matrixJoin

    #metodo que permite ejecutar la normalizacion, esta normalizacion se hace en cuenta sin considerar el atributo clase...
    def createMatrixNorm(self):

        #hacemos el procesamiento de la matriz...
        self.removeAttributeClass()
        self.matrixNormalized = preprocessing.normalize(self.matrixNormalized, norm='l2')
        self.makeUnionData()
        document.document('dataSetNormaliced.csv', self.pathOutput).createExportFileWithPandas(self.matrixNormalized, self.header)
