'''
clase con la responsabilidad de calcular las distancias entre los residuos y hacer el cambio en la matriz
dependiendo de las caracterisiticas de la misma...
'''

import pandas as pd
from Bio.PDB.PDBParser import PDBParser
from proyect.CCProcesFile import document
class processDistance(object):

    def __init__(self, matrixName, pathInput, distMin, criterio, pathOutput, header, structure):

        self.pathInput = pathInput
        self.structure = structure
        self.matrixName = matrixName
        self.distMin = distMin
        self.criterio = criterio
        self.pathOutput = pathOutput
        self.header = header

    #metodo que permite leer la matriz en forma de data frame...
    def readMatrix(self):

        self.matrix = document.document(self.pathInput+self.matrixName, "djaskd").readMatrix()

    #metodo que permite calcular la distancia entre dos residuos, retorna: {0,1} cuando criterio es 1, double dist cuando criterio es 2
    #y double energia cuando criterio es 3, tambien si distancia no esta en los ragos evaluados... retorna 0
    def calculateDistance(self, residueA, residueB):

        #cuando es glicina tomamos el carbono alfa...
        distance = 0
        atomA = self.getAtomForDistance(residueA)
        atomB = self.getAtomForDistance(residueB)

        distance = atomA - atomB

        if distance >= self.distMin:
            return 0
        else:
            if self.criterio == 1:
                return 1
            else:
                return distance

    #metodo que permite obtener los atomos a ser calculados...
    def getAtomForDistance(self, residue):

        dataSplit = residue.split('-')
        if dataSplit[0] == "GLY":
            return self.structure[0][dataSplit[2]][int(dataSplit[1])]['CA']
        else:
            return self.structure[0][dataSplit[2]][int(dataSplit[1])]['CB']

    #metodo que permite evaluar todas las distancias y modificar la matriz...
    def changeValueMatrix(self):
        self.readMatrix()
        for i in range (1, len(self.header)):
            for j in range (1, len(self.header)):
                distance = self.calculateDistance(self.header[i], self.header[j])
                self.matrix[i][j] = distance
        self.matrix = self.matrix[1:]
        #exportamos la matriz...
        print "Export Matrix"
        nameFile = self.matrixName
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(self.matrix, self.header)
