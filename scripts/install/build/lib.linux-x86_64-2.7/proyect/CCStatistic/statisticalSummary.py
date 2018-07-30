'''
clase con la responsabilidad de generar un resumen estadistico del set de datos de interes...
por cada atributo en el set de datos que sea diferente a la clase y no sea del tipo discreto...
'''

import pandas as pd
import numpy as np
from proyect.CCProcesFile import document

class statisticalSummary(object):

    def __init__(self, dataSetName, pathOutput):

        self.dataSet = pd.read_csv(dataSetName)
        self.pathOutput = pathOutput
        self.featureList = ['SaccW', 'SaccM', 'yDDG', 'ProteinPropens', 'Positionaccept', 'MOSST', 'Functionalrelevancefunction']

    #metodo que permite hacer los estadisticos por cada componente en el set de datos...
    def createStatiticalForFeature(self, feature):

        meanData = np.mean(self.dataSet[feature])
        varData = np.var(self.dataSet[feature])
        stdData = np.std(self.dataSet[feature])
        minData = min(self.dataSet[feature])
        maxData = max(self.dataSet[feature])
        row = [feature, meanData, varData, stdData, minData, maxData]
        return row

    #metodo que permite crear el set de datos de estadistico...
    def generateStatisticalSummary(self):

        matrixResponse = []

        for feature in self.featureList:
            matrixResponse.append(self.createStatiticalForFeature(feature))

        header = ["feature", "mean", "var", "std", "min", "max"]
        document.document("statisticalSummary.csv", self.pathOutput).createExportFileWithPandas(matrixResponse, header)
