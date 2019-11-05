'''
clase que tiene la responsabilidad de tomar la lista de resultados obtenidos,
generar una matriz y un header y exportar el resultado al path correspondiente...
'''

from proyect.CCProcesFile import document
import numpy as np

class exportResult(object):

    def __init__(self, listResult, pathOutput, nameFile):

        self.listResult = listResult
        self.pathOutput = pathOutput
        self.nameFile = nameFile
        self.matrix = []
        self.header = ['algorithm', 'description', 'validation', 'Accuracy_Mean', 'Accuracy_SD', 'Accuracy_Var', 'Accuracy_MIN', 'Accuracy_MAX', 'recall_Mean', 'recall_SD', 'recall_Var', 'recall_MIN', 'recall_MAX', 'precision_Mean', 'precision_SD', 'precision_Var', 'precision_MIN', 'precision_MAX', 'tn', 'fp', 'fn', 'tp']

    #procesamos la informacion y generamos la matriz a exportar...
    def processMatrixValues(self):

        for element in self.listResult:
            row = []

            row.append(element.algorithm)
            row.append(element.description)
            row.append(element.validation)
            row.append(np.mean(element.performance.ListAccuracy))
            row.append(np.std(element.performance.ListAccuracy))
            row.append(np.var(element.performance.ListAccuracy))
            row.append(min(element.performance.ListAccuracy))
            row.append(max(element.performance.ListAccuracy))

            row.append(np.mean(element.performance.ListRecall))
            row.append(np.std(element.performance.ListRecall))
            row.append(np.var(element.performance.ListRecall))
            row.append(min(element.performance.ListRecall))
            row.append(max(element.performance.ListRecall))

            row.append(np.mean(element.performance.ListPrecision))
            row.append(np.std(element.performance.ListPrecision))
            row.append(np.var(element.performance.ListPrecision))
            row.append(min(element.performance.ListPrecision))
            row.append(max(element.performance.ListPrecision))

            row.append(np.mean(element.performance.ListTN))
            row.append(np.mean(element.performance.ListFP))
            row.append(np.mean(element.performance.ListFN))
            row.append(np.mean(element.performance.ListTP))

            self.matrix.append(row)

    #metodo que permite exportar la matriz con los resultados...
    def exportMatrix(self):

        document.document(self.nameFile, self.pathOutput).createExportFileWithPandas(self.matrix, self.header)
