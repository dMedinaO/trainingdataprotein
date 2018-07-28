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

    def __init__(self, dataProcess, pathOutput):

        self.dataProcess = dataProcess
        self.pathOutput = pathOutput

    #metodo que permite obtener la informacion y hacer el histograma...
    def processInfo(self):

        self.data = pd.read_csv(self.dataProcess)

        #process histogram...
        title = "Histogram for performance distribution"
        label = "Accuracy"
        nameExport = "%sHist.png" % self.pathOutput
        print "Create histogram data..."
        self.createHistogram(self.data['Accuracy'], nameExport, label, title)

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

        minData = min(self.data['Accuracy'])
        maxData = max(self.data['Accuracy'])
        meanData = np.mean(self.data['Accuracy'])
        stdData = np.std(self.data['Accuracy'])
        varData = np.var(self.data['Accuracy'])

        header = ['Statistic', 'Value']
        #creamos un array lo exportamos a un data frame y generamos el resultado...
        summaryData = [['Mean', meanData], ['Std', stdData], ['Max', maxData], ['Min', minData], ['Var', varData]]

        document.document("statisticSummary.csv", self.pathOutput).createExportFileWithPandas(summaryData, header)

    #metodo que permite obtener los outliers...
    def getOuliersDistribution(self):

        stdData = np.std(self.data['Accuracy'])
        meanData= np.mean(self.data['Accuracy'])

        outliers = [x for x in self.data['Accuracy'] if (x >= meanData + 1.5 * stdData)]

        return outliers

    #metodo que permite obtener los algoritmos que representan un outlier y ejecutar funciones con ellos...
    def getBestModel(self):

        outliers = self.getOuliersDistribution()

        header = ['Algorithm',	'Description',	'Accuracy']
        matrix =[]

        for outlier in outliers:
            for i in range (len(self.data['Accuracy'])):
                row = []
                if self.data['Accuracy'][i] >=outlier:
                    row.append(self.data['algorithm'][i])
                    row.append(self.data['description'][i])
                    row.append(self.data['Accuracy'][i])

                    if row not in matrix:
                        matrix.append(row)

        #generamos el export...
        document.document("bestModels.csv", self.pathOutput).createExportFileWithPandas(matrix, header)
