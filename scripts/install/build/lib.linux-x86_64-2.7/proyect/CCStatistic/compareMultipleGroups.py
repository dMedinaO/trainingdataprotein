'''
clase que permite hacer la comparacion entre los grupos y evaluar si son significativos o no...
'''

from scipy.stats import mannwhitneyu
import pandas as pd
from proyect.CCProcesFile import document

class compareGroups(object):

    def __init__(self, pathInput):

        self.pathInput = pathInput
        self.ListGroup = ['A_Attribute','B_Attribute','C_Attribute','F_Attribute','H_Attribute','M_Attribute','N_Attribute','O_Attribute','P_Attribute','R_Attribute','T_Attribute','U_Attribute','Z_Attribute']

    #metodo que permite trabajar con la matriz, quitarle el header y la ultima columna y transformarla a float toda la data...
    def processMatrix(self, matrix):

        matrix = matrix[1:]
        matrixProcess=[]

        for i in range (len(matrix)):
            row = []
            for j in range(len(matrix[i])-1):
                row.append(float(matrix[i][j]))
            matrixProcess.append(row)

        return matrixProcess

    #metodo que permite hacer la lectura de todos los set de datos y los almacena en una lista...
    def readDataSet(self):

        self.ListDataSet = []

        for group in self.ListGroup:
            #formamos el path...
            nameFile = "%s%s/normaliced/dataSetNormaliced.csv" % (self.pathInput, group)
            matrix = document.document(nameFile, 'pathInput').readMatrix()
            self.ListDataSet.append(self.processMatrix(matrix))

    #metodo que permite hacer la comparacion entre los grupos...
    def compareGroupsMWT(self):

        matrixP = []

        for i in range(len(self.ListDataSet)):
            row=[]
            for j in range (len(self.ListDataSet)):
                if i == j:
                    row.append(0)
                else:
                    u, prob = mannwhitneyu(self.ListDataSet[i], self.ListDataSet[j])
                    row.append(prob)

            matrixP.append(row)

        nameDocument = "summaryCompareGroups.csv"
        document.document(nameDocument, self.pathInput).createExportFileWithPandas(matrixP, self.ListGroup)
