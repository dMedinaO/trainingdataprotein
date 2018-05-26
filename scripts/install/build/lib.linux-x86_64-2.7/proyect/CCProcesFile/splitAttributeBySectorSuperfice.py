'''
clase que permite generar la sub division del set de datos con respecto al valor de su sector superfice
este script genera diversos set de datos con respecto al tipo sector superfice que posee.

Trabaja en conjunto con la clase documento, para generar el archivo de salida...
'''

from proyect.CCProcesFile import document #para hacer la instancia a la clase de lectura y escritura de archivos...

class splitterSector(object):

    def __init__(self, nameFile, pathOutput, splitter, index):

        self.nameFile = nameFile
        self.index = index
        self.pathOutput = pathOutput
        self.splitter = splitter
        self.matrixNotProcess = self.createMatrixData()
        self.resumeGroup = []

        self.processMatrixData()
        self.getValuesForSectorSuperfice()
    #metodo que permite el procesamiento de los datos
    def createMatrixData(self):

        documentOpen = document.document(self.nameFile, self.pathOutput)
        return documentOpen.readDocument()

    #metodo que permite poder procesar la matriz, genera el header y la data en matriz...
    def processMatrixData(self):

        self.header = self.matrixNotProcess[0].split(self.splitter)#obtenemos el header
        self.header.pop(self.index)#eliminamos el atributo que molesta...

        self.matrixData = []

        for i in range (1, len(self.matrixNotProcess)):
            data = self.matrixNotProcess[i].split(self.splitter)
            self.matrixData.append(data)

    #metodo que permite obtener la lista de atributos del sector superfice
    def getValuesForSectorSuperfice(self):

        self.listSector = []
        for element in self.matrixData:
            self.listSector.append(element[self.index])
        self.listSector = list(set(self.listSector))

    #metodo que permite agregar elementos a un arreglo segun su sector superfice, sin considerar esta columna...
    def addElementsToGroup(self, group):

        matrixGroup = []
        for element in self.matrixData:

            row = []
            if element[self.index] == group:
                for i in range(len(element)):
                    if i != self.index:
                        row.append(element[i])
                matrixGroup.append(row)
        return matrixGroup

    #metodo que permite hacer la division de los grupos...
    def makeSplitterBySector(self):

        for element in self.listSector:
            print "Process Element %s" % element
            matrixGroup = self.addElementsToGroup(element)
            row = [element, len(matrixGroup)]
            self.resumeGroup.append(row)

            #exportamos el documento...
            namePathE = "%s%s_Attribute/" % (self.pathOutput, element)
            nameFileE = "%s_Attribute.csv" % element

            documentObject = document.document(nameFileE, namePathE)
            documentObject.createDir(namePathE)
            documentObject.createExportFileWithPandas(matrixGroup, self.header)
            print "--------------------------------------------------"
        print "Generando resumen..."
        documentValue = document.document('resumeGroups.csv', self.pathOutput).createExportFileWithPandas(self.resumeGroup, ['grupo', 'integrantes'])
