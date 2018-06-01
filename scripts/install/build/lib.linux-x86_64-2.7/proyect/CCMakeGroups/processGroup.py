'''
clase que permite procesar la informacion y hacer el manejo de la informacion de los grupos y las distancias y sus respectivos
valores asociados a los puntos de interes...
'''

from proyect.CCMakeGroups import generateSplitterGroup
from proyect.CCMakeGroups import descriptionDistanceGroups
from proyect.CCProcesFile import document

class groupList(object):

    def __init__(self, nameFile, pathOutput, splitter):

        self.nameFile = nameFile
        self.pathOutput = pathOutput
        self.splitter = splitter
        self.splitterObject = generateSplitterGroup.createGroupSplitter(self.nameFile, self.pathOutput, self.splitter)
        self.splitterObject.processData()

    #metodo que permite procesar las distancias...
    def processDistancesObject(self):

        for i in range(len(self.splitterObject.ListGroup)):
            print "Haciendo el calculo de distancias para el grupo: ", self.splitterObject.ListGroup[i].name
            for j in range(len(self.splitterObject.ListGroup)):
                if i != j:
                    descriptionDistanceGroupsObject = descriptionDistanceGroups.distGroupData(self.splitterObject.ListGroup[i], self.splitterObject.ListGroup[j])
                    descriptionDistanceGroupsObject.calculateDistData()
                    #hacemos la actualizacion del grupo i con respecto a las distancias de los grupos j...
                    self.splitterObject.ListGroup[i].dataDistances.update({self.splitterObject.ListGroup[j].name: descriptionDistanceGroupsObject})
            print "Las distancias Calculadas son:"
            self.splitterObject.ListGroup[i].showDistancesForGroup()

    #metodo que permite exportar las distancias a matriz...
    def exportDistancesToMatrix(self):

        matrixData = []
        header = []
        header.append("-")
        for i in range(len(self.splitterObject.ListGroup)):
            row = []
            row.append(self.splitterObject.ListGroup[i].name)
            header.append(self.splitterObject.ListGroup[i].name)
            for j in range(len(self.splitterObject.ListGroup)):
                if i == j:
                    row.append(0)
                else:
                    row.append(self.splitterObject.ListGroup[i].dataDistances[self.splitterObject.ListGroup[j].name].max_max)
            matrixData.append(row)

        #exportamos el documento...
        nameFile = "matrixMaxDistanceOriginal.csv"
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, header)
