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
        self.header = ['algorithm', 'description', 'validation', 'Accuracy', 'Recall', 'Precision', 'Hamming', 'F', 'Cohen']

    #procesamos la informacion y generamos la matriz a exportar...
    def processMatrixValues(self):

        for element in self.listResult:
            row = []

            row.append(element.algorithm)
            row.append(element.description)
            row.append(element.validation)
            row.append(np.mean(element.performance.ListAccuracy))
            row.append(np.mean(element.performance.ListRecall))
            row.append(np.mean(element.performance.ListPrecision))
            row.append(np.mean(element.performance.ListHamming))
            row.append(np.mean(element.performance.ListF))
            row.append(np.mean(element.performance.ListCohen))

            self.matrix.append(row)

    #metodo que permite exportar la matriz con los resultados...
    def exportMatrix(self):

        document.document(self.nameFile, self.pathOutput).createExportFileWithPandas(self.matrix, self.header)
        
