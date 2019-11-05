'''
clase que permite representar a un modelo...
'''

from proyect.CCProcesFile import document

class modelGroup(object):

    def __init__(self, model, algorithm, description):

        self.algorithm = algorithm
        self.description = description
        self.model = model
        self.silohuette = 0
        self.calinski = 0

    #metodo que permite exportar la data de los grupos y generar los set de datos...
    def exportData(self, dataSet, header, pathOutput):

        examples1 = []
        examples0 = []

        for i in range (len(self.model.labels_)):
            if self.model.labels_[i] == 0:
                examples0.append(dataSet[i])
            else:
                examples1.append(dataSet[i])
        nameFile1 = "group0.csv"
        nameFile2 = "group1.csv"
        document.document(nameFile1, pathOutput).createExportFileWithPandas(examples0, header)
        document.document(nameFile2, pathOutput).createExportFileWithPandas(examples1, header)

    #metodo que permite exportar la data del resumen...
    def createSummary(self, pathOutput):

        nameFile = "summaryProcess.csv"
        matrix = [["algorithm", self.algorithm], ["description", self.description], ["silohuette", self.silohuette], ["calinski", self.calinski]]
        header = ["data", "value"]
        document.document(nameFile, pathOutput).createExportFileWithPandas(matrix, header)
