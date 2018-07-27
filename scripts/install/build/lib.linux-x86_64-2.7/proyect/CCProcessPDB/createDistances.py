'''
clase con la responsabilidad de calcular las distancias entre los residuos y hacer el cambio en la matriz
dependiendo de las caracterisiticas de la misma...
'''

import pandas as pd
from Bio.PDB.PDBParser import PDBParser

class processDistance(object):

    def __init__(self, matrixName, pathInput, distMin, distMax, criterio, pathOutput, header, structure):

        self.pathInput = pathInput
        self.structure = structure
        self.matrixName = matrixName
        self.distMin = distMin
        self.distMax = distMax
        self.criterio = criterio
        self.pathOutput = pathOutput
        self.header = header

    #metodo que permite leer la matriz en forma de data frame...
    def readMatrix(self):

        self.matrix = pd.read_csv(self.pathInput+self.matrixName)

    #metodo que permite calcular la distancia entre dos residuos, retorna: {0,1} cuando criterio es 1, double dist cuando criterio es 2
    #y double energia cuando criterio es 3, tambien si distancia no esta en los ragos evaluados... retorna 0
    def calculateDistance(self, residueA, residueB):

        #cuando es glicina tomamos el carbono alfa...
        distance = 0
        atomA = self.getAtomForDistance(residueA)
        atomB = self.getAtomForDistance(residueB)

        distance = atomA - atomB

        if distance < self.distMin or distance> self.distMax:
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
            return self.structure[0][dataSplit[2]][int(dataSplit[1])]['CA']

    #metodo que permite evaluar todas las distancias y modificar la matriz...
    def changeValueMatrix(self):
        self.readMatrix()
        for i in range (len(self.header)):
            for j in range (len(self.header)):
                distance = self.calculateDistance(self.header[i], self.header[j])
                self.matrix[self.header[i]][j] = distance

        #exportamos la matriz...
        print "Export Matrix"
        nameFile = "%s%s" % (self.pathOutput, self.matrixName)
        self.matrix.to_csv(nameFile, index=False)
        
