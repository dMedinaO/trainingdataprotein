'''
clase que permite poder evaluar las divisiones de los grupos generados, esto permite aplicar los coeficientes de
siluetas y los de kalinzki-harabaz, para evaluar solapamiento de datos.
'''
from proyect.CCProcesFile import document #para hacer la instancia a la clase de lectura y escritura de archivos...
from proyect.CCClustering import createGraphicSilhouette
import numpy as np

class evaluateSplitSectorSuperfice(object):

    #constructor de la clase
    def __init__(self, nameFile, pathOutput, splitter, index):
        super(evaluateSplitSectorSuperfice, self).__init__()
        self.index = index
        self.nameFile = nameFile
        self.pathOutput = pathOutput
        self.splitter = splitter
        self.matrixNotProcess = self.createMatrixData()
        self.processMatrixData()
        self.checkAttributesInMatrix()

    #metodo que permite el procesamiento de los datos
    def createMatrixData(self):

        documentOpen = document.document(self.nameFile, self.pathOutput)
        return documentOpen.readDocument()

    #metodo que permite poder procesar la matriz, genera el header y la data en matriz...
    def processMatrixData(self):

        self.header = self.matrixNotProcess[0].split(self.splitter)#obtenemos el header
        self.matrixData = []

        for i in range (1, len(self.matrixNotProcess)):
            data = self.matrixNotProcess[i].split(self.splitter)
            self.matrixData.append(data)

    #metodo que permite modificar el valor del atributo clase, los cambia por: 0:D 1:N, esto permite la evaluacion del entrenamiento
    def changeValueClassAttribute(self):

        for i in range(len(self.matrixData)):
            if self.matrixData[i][-1] == 'D':
                self.matrixData[i][-1] = 0
            else:
                self.matrixData[i][-1] = 1

    #metodo que permite identificar la posiciones de los indices en los que la matrix tiene atributos discretos
    def getIndexDiscreteAttributes(self):

        listIndex = []

        for i in range (len(self.header)-1):
            try:
                data = float(self.matrixData[0][i])
            except:
                listIndex.append(i)
                pass
        return listIndex

    #metodo que permite crear un diccionario con respecto a la data del sector superfice...
    def createDirForSector(self, listAttribute):

        dictData = {}
        for i in range(len(listAttribute)):
            dictData.update({listAttribute[i]:i})
        return dictData

    #metodo que permite obtener los grupos con indices del 0 al largo...
    def getDataGroup(self):

        ListData = []
        ListUnique = []
        for element in self.matrixData:
            ListData.append(element[self.index])
            ListUnique.append(element[self.index])
        ListUnique = list(set(ListUnique))
        dictValues = self.createDirForSector(ListUnique)
        self.groupLabel = []
        for element in ListData:
            self.groupLabel.append(dictValues[element])

    #metodo que permite remover el atributo sector superfice porque no entrega informacion relativa...
    def removeIndexValue(self):

        for i in range(len(self.matrixData)):
            self.matrixData[i].pop(self.index)

    #obtenemos la lista segun el indice y hacemos los calculos de conversion...
    def getValuesAttributes(self, index):

        ListData = []
        ListUnique = []
        dictValues = {}
        for element in self.matrixData:
            ListData.append(element[index])
            ListUnique.append(element[index])

        ListUnique = list(set(ListUnique))

        #hacemos el conteo por cada posibilidad de valor...
        for value in ListUnique:
            cont=0
            for valueList in ListData:
                if value == valueList:
                    cont+=1
            dictValues.update({value:float(cont/float(len(ListData)))})
        return dictValues

    #metodo que permite poder modificar los valores segun la transformacion...
    def changeValuesAttributeByIndex(self, index, dictValues):

        for i in range(len(self.matrixData)):
            self.matrixData[i][index] = dictValues[self.matrixData[i][index]]

    #metodo que permite hacer la transformacion a float de la matrix...
    def transformToFloat(self):

        for i in range(len(self.matrixData)):
            for j in range(len(self.matrixData[i])-1):
                self.matrixData[i][j] = float(self.matrixData[i][j])

    #metodo que permite tomar la matriz de datos y evaluar las columnas, si son numericas, las deja de igual forma,
    #en caso contrario aplica la transformacion de datos, con respecto a la incidencia de ellos, ademas, el atributo clase, lo
    #modifica para que sean 0 y 1, 0: D y 1:N
    def checkAttributesInMatrix(self):

        self.changeValueClassAttribute()#hacemos el cambio del atributo clase...
        self.getDataGroup()#obtenemos los grupos...
        listIndex = self.getIndexDiscreteAttributes()#obtenemos los indices de atributos discretos

        #hacemos las modificaciones correspondientes
        for index in listIndex:
            dictValues = self.getValuesAttributes(index)
            self.changeValuesAttributeByIndex(index, dictValues)

        self.removeIndexValue()#removemos el atributo index...
        self.transformToFloat()#hacemos la modificaciones para transformacion a float

        clusterGroup = list(set(self.groupLabel))

        #hacemos el grafico e imprimimos los valores...
        graphic = createGraphicSilhouette.graphicSilhouette(self.matrixData, self.groupLabel, len(clusterGroup), clusterGroup)
        graphic.createGraphic()
        print "Coeficiente siluetas: ", graphic.silhouette_avg
