'''
clase que tiene la responsabilidad de generar n grupos aleatorios, normalizarlos y hacer el entrenamiento con LOU como
forma de validacion...
Nota: Si el numero de grupos es mayor a 7, se divide el set de datos en la cantidad de grupos y al ultimo elemento se le
agrega la parte entera faltante...
'''
import random
import subprocess
from proyect.CCMakeGroups import makeRandomGroup

from proyect.CCProcesFile import document, procesFile
from proyect.CCStatistic import normalize
from proyect.CCTraining.LOU import knnAlgorithm, adaBoost, decisionTrees, gradientTreeBoost, naiveBayes, nuSVC, randomForest, SVC
from proyect.CCTraining.LOU import processResult

class groupRandomGenerator(object):

    def __init__(self, numberGroup, pathOutput, matrixData, header, iterator):

        self.numberGroup = numberGroup
        self.pathOutput = pathOutput
        self.matrixData = matrixData
        self.header = header
        self.iterator = iterator

    #metodo que permite generar las iteraciones...
    def createProcess(self):

        for i in range(1, self.iterator+1):
            #formamos el nombre del directorio...
            namePath = "%s%d_iteration/" % (self.pathOutput, i)
            #print namePath
            self.createDir(namePath)

            self.createRandomIndex()
            self.processGroupRand()


            #comenzamos a crear los directorios para los grupos...
            for group in range(1, self.numberGroup+1):
                namePathGroup = "%sgroup_%d/" % (namePath, group)
                self.createDir(namePathGroup)

                #generamos la matriz del grupo...
                matrixGroup = []
                for row in range(self.ListGroupMembers[group-1]):
                    matrixGroup.append(self.matrixData[row])

                #procesamos la matrix para remover el indice...
                matrixGroupRemove = self.removeSectorSuperfice(matrixGroup)
                #importamos la matriz....
                document.document("matrixRandom.csv", namePathGroup).createExportFileWithPandas(matrixGroupRemove, self.header)

                print "Process documento..."
                process = self.processRandomMatrix(namePathGroup)#procesamos la matrix y generamos la transformacion...
                try:
                    print "Normalice Process..."
                    self.normalizacionData(namePathGroup, process)
                except:
                    pass
                #hacemos el entrenamiento...
                dirDataNormal = namePathGroup+"dataSetNormaliced.csv"
                makeGroupO = makeRandomGroup.makeGroup()
                makeGroupO.trainingModelDataSet(dirDataNormal, namePathGroup)
    #metodo que permite la normalizacion del set de datos...
    def normalizacionData(self, pathValue, process):

        normalObject = normalize.NormalizeData(process.header, process.matrixData, pathValue)
        normalObject.createMatrixNorm()

    #metodo que permite hacer el procesamiento de la matriz generada aleatoriamente...
    def processRandomMatrix(self, dirPath):

        #con el archivo generado podemos procesarlo
        nameDocument = dirPath+"matrixRandom.csv"
        process = procesFile.processDataSet(nameDocument, dirPath, ',')#instancia al procesador de informacion...
        process.processMatrixData()#procesamos la matriz...
        process.checkAttributesInMatrix()#aplicamos la transformacion....
        return process

    #metodo que permite procesar la matriz del grupo para remover el atributo sector superfice
    def removeSectorSuperfice(self, matrix):

        matrixData = []
        for i in range(len(matrix)):
            row =[]
            for j in range(len(matrix[i])):
                if j != 13:
                    row.append(matrix[i][j])
            matrixData.append(row)
        return matrixData

    #metodo que permite crear un directorio...
    def createDir(self, pathDir):
        command = "mkdir -p %s" % pathDir
        subprocess.call(command, shell=True)

    #metodo que permite crear una lista con los indices random...
    def createRandomIndex(self):

        self.indexRandom = []
        for i in range(len(self.matrixData)):
            self.indexRandom.append(i)

        #hacemos shuffle a los indices para que se encuentren desordenados...
        random.shuffle(self.indexRandom)

    #metodo que permite el procesamiento de la data para hacer los grupos aleatorios...
    def processGroupRand(self):
        self.ListGroupMembers = []
        if self.numberGroup <=7:
            while True:
                ListMemberGroup = self.createNumberMembers()
                dataSum = sum(ListMemberGroup)
                if dataSum < len(self.indexRandom)-20:
                    ListMemberGroup.append(len(self.indexRandom)-dataSum)
                    self.ListGroupMembers = ListMemberGroup
                    break
        else:
            dataValue = int(len(self.indexRandom)/self.numberGroup)
            resto = len(self.indexRandom) - (dataValue*self.numberGroup)
            for i in range(self.numberGroup):
                self.ListGroupMembers.append(dataValue)
            self.ListGroupMembers[0]+=resto

    #metodo que permite crear la lista de cantidad de integrantes por grupo, nota: los grupos no pueden tener menos de 20 elementos
    def createNumberMembers(self):

        ListMemberGroup =[]

        for i in range(self.numberGroup-1):
            ListMemberGroup.append(random.randint(20,len(self.indexRandom)))

        return ListMemberGroup
