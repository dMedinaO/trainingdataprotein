'''
clase con la responsabilidad de parsear el archivo csv con el set de datos, extraer la informacion y hacer las
subdivisiones de los grupos...
'''

from proyect.CCProcesFile import procesFile
from proyect.CCProcesFile import document
from proyect.CCMakeGroups import group

class createGroupSplitter(object):

    def __init__(self, nameFile, pathOutput, splitter):

        self.nameFile = nameFile
        self.pathOutput = pathOutput
        self.splitter = splitter
        self.processObject = procesFile.processDataSet(self.nameFile, self.pathOutput, self.splitter)
        self.ListGroup = []#contendra la informacion de los grupos...

    #metodo que permite procesar el set de datos...
    def processData(self):
        #hacemos el procesamiento de los datos...
        self.processObject.processMatrixData()
        self.processObject.checkAttributesInMatrixNotExport()

        self.createGroupsData()

        for i in range(len(self.ListGroup)):
            print "process group: ", self.ListGroup[i].name
            self.ListGroup[i].processAttributesGroup()

    #metodo que permite hacer la busqueda de grupos y generar los elementos del valor de datos...
    def createGroupsData(self):

        #obtenemos el diccionario de informacion...
        dictValues = self.getProporcionesSectorSuperfice()

        for key in dictValues:
            matrixGroup = []
            classList = []
            for example in self.processObject.matrixData:
                if example[13] == dictValues[key]:
                    matrixGroup.append(example[:-1])
                    classList.append(example[-1])

            #instanciamos al objeto...
            self.ListGroup.append(group.groupDescription(key, matrixGroup, classList))

    #metodo que permite obtener las proporciones para el atributo...
    def getValueDict(self, ListData):

        ListUnique = list(set(ListData))
        dictValues = {}
        #hacemos el conteo por cada posibilidad de valor...
        for value in ListUnique:
            cont=0
            for valueList in ListData:
                if value == valueList:
                    cont+=1
            dictValues.update({value:float(cont/float(len(ListData)))})
        return dictValues

    #obtenemos las proporciones para el atributo sector superfice...
    def getProporcionesSectorSuperfice(self):

        sectorSuperficeValue = []

        for element in self.processObject.matrixNotProcess:
            data = element.split(self.splitter)
            sectorSuperficeValue.append(data[13])

        sectorSuperficeValue = sectorSuperficeValue[1:]
        return self.getValueDict(sectorSuperficeValue)
