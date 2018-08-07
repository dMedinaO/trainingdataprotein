'''
clase con la responsabilidad de obtener todas las performances y ejecutar las siguientes acciones:

1. Histograma de performance.
2. Obtener valores outliers de la muestra.
3. Obtener los algoritmos con los mejores resultados y hacer cuadro resumen.
4. Obtener las estadisticas de la ejecucion
5. exportar los resultados a tabla resumen.

# NOTE:  solo la performance de Accuracy sera la que sera considerada, por otro lado, los algoritmos con mejores resultados, se utilizaran para obtener
sus graficas, curvas roc, matriz de confusion, y todos los resultados que sirvan para denotar los valores obtenidos...
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from proyect.CCProcesFile import document

class processPerformance(object):

    def __init__(self, dataProcess, pathOutput, valueHeader, stdValue):

        self.dataProcess = dataProcess
        self.pathOutput = pathOutput
        self.valueHeader = valueHeader
        self.stdValue = stdValue

    #metodo que permite obtener la informacion y hacer el histograma...
    def processInfo(self):

        self.data = pd.read_csv(self.dataProcess)

        #process histogram...
        title = "Histogram for performance distribution"
        label = self.valueHeader
        nameExport = "%sHist.png" % self.pathOutput
        print "Create histogram data..."
        self.createHistogram(self.data[self.valueHeader], nameExport, label, title)

        print "Create summary data..."
        self.createSummaryStatistic()

        print "Process outliers..."
        self.getBestModel()

    #metodo que permite generar el histograma...
    def createHistogram(self, listData, nameExport, label, title):
        plt.figure()
        sns.set(color_codes=True)
        sns.set(style="ticks")
        sns_plot = sns.distplot( listData , color="red", label=label, kde=False, rug=True)
        sns.plt.legend()
        sns.plt.title(title)
        sns_plot.figure.savefig(nameExport)

    #metodo que permite crear el resumen estadistico de la distribucion...
    def createSummaryStatistic(self):

        minData = min(self.data[self.valueHeader])
        maxData = max(self.data[self.valueHeader])
        meanData = np.mean(self.data[self.valueHeader])
        stdData = np.std(self.data[self.valueHeader])
        varData = np.var(self.data[self.valueHeader])

        header = ['Statistic', 'Value']
        #creamos un array lo exportamos a un data frame y generamos el resultado...
        summaryData = [['Mean', meanData], ['Std', stdData], ['Max', maxData], ['Min', minData], ['Var', varData]]

        document.document("statisticSummary.csv", self.pathOutput).createExportFileWithPandas(summaryData, header)

    #metodo que permite obtener los outliers...
    def getOuliersDistribution(self):

        stdData = np.std(self.data[self.valueHeader])
        meanData= np.mean(self.data[self.valueHeader])

        outliers = [x for x in self.data[self.valueHeader] if (x <= meanData -  self.stdValue * stdData)]

        if len(outliers) == 0:
            outliers.append(max(self.data[self.valueHeader]))

        return outliers

    #metodo que permite obtener los algoritmos que representan un outlier y ejecutar funciones con ellos...
    def getBestModel(self):

        outliers = self.getOuliersDistribution()

        header = ['Algorithm',	'Description',	self.valueHeader]
        matrix =[]

        for outlier in outliers:
            for i in range (len(self.data[self.valueHeader])):
                row = []
                if self.data[self.valueHeader][i] <=outlier:
                    row.append(self.data['algoritmo'][i])
                    row.append(self.data['description'][i])
                    row.append(self.data[self.valueHeader][i])

                    if row not in matrix:
                        matrix.append(row)

        #generamos el export...
        document.document("bestModels.csv", self.pathOutput).createExportFileWithPandas(matrix, header)
