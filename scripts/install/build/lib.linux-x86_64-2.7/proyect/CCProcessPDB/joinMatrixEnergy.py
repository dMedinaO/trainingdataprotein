'''
clase que tiene la responsabilidad de tomar las matrices generadas y crear la sumatoria de estas matrices...
la gracias es poder generar una matriz global de la informacion y a su vez... poder exportar esta matriz
la cual sera o correspondera a la matriz de adyacencia, esto permitira la posterior generacion de los grafos...
'''

from proyect.CCProcessPDB import processPDB, calculateHBondsBestNetwork, parserDegreePhiPsi, calculateCovalentEnergy
from proyect.CCProcesFile import document
from proyect.CCProcessPDB import createGraph

class fullMatrixEnergy(object):

    def __init__(self, processPDBObject, hBondsNetworkValue, covalenteValues, nameFileMatrix, pathOutput):

        self.processPDBObject = processPDBObject
        self.hBondsNetworkValue = hBondsNetworkValue
        self.covalenteValues = covalenteValues
        self.nameFileMatrix = nameFileMatrix
        self.pathOutput = pathOutput
        self.matrixFull = self.processPDBObject.generateMatrixOnes()#generamos la matriz de 0...

    #metodo que permite procesar cada matriz y hacer la sumatoria de los elementos...
    def createFullMatrix(self):

        lenValue = len(self.matrixFull)
        for i in range(lenValue):
            for j in range(1, lenValue+1):
                self.matrixFull[i][j] = self.hBondsNetworkValue.matrixData[i][j] + self.covalenteValues.matrixData[i][j]
        #exportamos el documento...
        document.document(self.nameFileMatrix, self.pathOutput).createExportFileWithPandas(self.matrixFull, self.processPDBObject.header)

    #metodo que permite procesar una nueva matriz, pero eliminando la ultima columna...
    def createMatrixRemoveCol(self):

        headerData = self.processPDBObject.header[1:]
        matrixValue = []

        for element in self.matrixFull:
            matrixValue.append(element[1:])
        document.document('matrixFullForHeatMap.csv', self.pathOutput).createExportFileWithPandas(matrixValue, headerData)

    #metodo que permite trabajar con los elementos de la matriz generada para crear grafos...
    def createGraphData(self):

        self.graphCreator = createGraph.createGraph(self.matrixFull, self.processPDBObject.header, self.pathOutput)
        self.graphCreator.createGraphExportJS()
        #self.graphCreator.addNodesToGraph()
        #self.graphCreator.addEdgeToGraph()
        #self.graphCreator.showGraph()
        #self.graphCreator.searchSubGrafos()
