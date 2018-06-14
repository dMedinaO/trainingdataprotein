'''
Clase que tiene la responsabilidad de generar los elementos aleatorios del grupo 13...
genera elementos aleatorios con considerar el atributo sector superfice...
'''
import random
import subprocess
from proyect.CCMakeGroups import makeRandomGroup

from proyect.CCProcesFile import document, procesFile
from proyect.CCStatistic import normalize
from proyect.CCTraining.LOU import knnAlgorithm, adaBoost, decisionTrees, gradientTreeBoost, naiveBayes, nuSVC, randomForest, SVC
from proyect.CCTraining.LOU import processResult

class groupRandomGenerator(object):

    def __init__(self, numberGroup, pathOutput, matrixData, header, iterator, dictGroup):

        self.numberGroup = numberGroup
        self.pathOutput = pathOutput
        self.matrixData = matrixData
        self.header = header
        self.dictGroup = dictGroup
        self.iterator = iterator

    #metodo que permite generar las iteraciones...
    def createProcess(self):

        for i in range(1, self.iterator+1):
            #formamos el nombre del directorio...
            namePath = "%s%d_iteration/" % (self.pathOutput, i)
            #print namePath
            self.createDir(namePath)
            self.createRandomIndex()

            #por cada elemento en el diccionario:
            for group in self.dictGroup:
                namePathGroup = "%sgroup_%s/" % (namePath, group)
                self.createDir(namePathGroup)

                #generamos la matriz del grupo...
                matrixGroup = []
                actualPos=0
                for row in range(self.dictGroup[group]):#cada elemento en la cantidad...
                    matrixGroup.append(self.matrixData[self.indexRandom[actualPos]])
                    actualPos+=1

                #importamos la matriz....
                document.document("matrixRandom.csv", namePathGroup).createExportFileWithPandas(matrixGroup, self.header)

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
