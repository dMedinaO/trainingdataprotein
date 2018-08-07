'''
clase que permite poder generar el archivo resumen con la informacion de la performance
'''
from proyect.CCTraining import naiveBayes, adaBoost, knnAlgorithm, decisionTrees, gradientTreeBoost, nuSVC, SVC, randomForest, performanceScore, processPerformance
from proyect.CCProcesFile import document #para hacer la instancia a la clase de lectura y escritura de archivos...

class resumePerformance(object):

    def __init__(self, ListResultAlgorithm, pathOutput):

        self.ListResultAlgorithm = ListResultAlgorithm
        self.DictListFull = []
        self.matrixData = []
        self.header = ['algoritmo', 'description', 'validation', 'accuracy', 'recall', 'precision', 'neg_log_loss', 'f1', 'ftwo_scorer', 'tn', 'fp', 'fn', 'tp']

        self.addElementPerformanceResponse()
        self.addElementMatrix()
        self.exportMatrixResult(pathOutput)

    #funcion que permite agregar los elementos de los resultados al arreglo...
    def addElementPerformanceResponse(self):

        for element in self.ListResultAlgorithm:
            for data in element.scorePerformance.dictValue:
                self.DictListFull.append(data)

    #comenzamos a generar la matriz de datos...
    def addElementMatrix(self):

        for element in self.DictListFull:
            row = []
            for head in self.header:
                row.append(element[head])
            self.matrixData.append(row)

    #metodo que permite exportar la matriz...
    def exportMatrixResult(self, pathOutput):

        document.document('performanceTraining.csv', pathOutput).createExportFileWithPandas(self.matrixData, self.header)
