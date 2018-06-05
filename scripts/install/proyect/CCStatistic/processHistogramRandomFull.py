'''
clase con la responsabilidad de procesar los archivos de performance para cada grupo, en cada iteracion,
obtener la mejor dependiendo de la performance y poder trabajar con ella para procesar la data de interes...
'''

from proyect.CCStatistic import performanceRandom
from proyect.CCProcesFile import document
import subprocess

class processHistogramRandom(object):

    def __init__(self, pathInput, pathOutput, iteration, groupsNumber, splitter):

        self.pathInput = pathInput
        self.pathOutput = pathOutput
        self.iteration = iteration
        self.groupsNumber = groupsNumber
        self.splitter = splitter
        self.performanceObjectList = []

    #metodo que permite parsear la matriz...
    def parserMatrix(self, matrixData):

        matrixParser = []
        for element in matrixData:
            data = element.split(self.splitter)
            matrixParser.append(data)
        return matrixParser

    #metodo que permite trabajar con la matriz y encontrar el mayor valor para una columna...
    def getMaxValueCol(self, matrixData, index):

        maxValue = -1
        listData = []
        for element in matrixData:
            listData.append(float(element[index]))

        try:
            maxValue = max(listData)
        except:
            pass

        return maxValue

    #trabajamos con la informacion, generamos las iteraciones y hacemos el procesamiento de los datos...
    def processData(self):

        for i in range(1, self.iteration+1):#comenzamos con la lectura de cada documento..
            for j in range(1, self.groupsNumber+1):
                pathRead = "%s%d_iteration/%d/training/fullJoin.csv" % (self.pathInput, i, j)
                matrixData = document.document(pathRead, 'pathOutput').readDocument()#obtenemos la matriz
                matrixParser = self.parserMatrix(matrixData)#la parseamos
                maxAccuracy = self.getMaxValueCol(matrixParser, 4)
                maxR_call = self.getMaxValueCol(matrixParser, 5)
                maxPrecission = self.getMaxValueCol(matrixParser, 6)

                if maxAccuracy != -1 and maxR_call != -1 and maxPrecission != -1:
                    #instanciamos al objeto... y lo agregamos a la lista...
                    self.performanceObjectList.append(performanceRandom.performanceGroup(j, maxAccuracy, maxR_call, maxPrecission))

    #metodo que permite trabajar por grupos y por performance para generar el histograma...
    def generateDataExportForHistogram(self, group, performance, nameFile):

        dataMatrix = []
        header = ['dataInfo']
        #agregamos los elementos a la matriz segun la performance correspondiente...
        for element in self.performanceObjectList:
            if element.groupNumber == group:
                if performance == 0:
                    dataMatrix.append(element.accuracy)
                if performance == 1:
                    dataMatrix.append(element.r_call)
                if performance == 2:
                    dataMatrix.append(element.precission)
        #exportamos el archivo...
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(dataMatrix, header)

    #metodo que permite procesar la generacion de los histogramas...
    def processHistogramGeneration(self):

        listPerformance = ['accuracy', 'r_call', 'precission']
        for i in range(1, self.groupsNumber+1):
            for j in range(len(listPerformance)):
                #formamos el nombre del archivo de salida...
                nameFile = "histogramData_Group_%d_performance_%s.csv" % (i, listPerformance[j])
                nameFilePicture = "%shistogramData_Group_%d_performance_%s.svg" % (self.pathOutput,i, listPerformance[j])
                print "process file: ", nameFile
                self.generateDataExportForHistogram(i, j, nameFile)

                nameFileFull = "%s%s" % (self.pathOutput, nameFile)

                #hacemos la llamada a sistema para la ejecucion del resource R...
                command = "Rscript /home/dmedina/Escritorio/MisProyectos/UChileProyects/trainingdataprotein/scripts/install/resource/rScripts/histogram.R %s %s %s" % (nameFileFull, nameFilePicture, listPerformance[j])
                subprocess.call(command, shell=True)
