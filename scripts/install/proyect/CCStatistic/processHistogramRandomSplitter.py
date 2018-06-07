'''
clase con la responsabilidad de procesar los archivos de performance para cada grupo, en cada iteracion,
obtener la mejor dependiendo de la performance y poder trabajar con ella para procesar la data de interes...
'''

from proyect.CCStatistic import performanceRandom
from proyect.CCProcesFile import document
import subprocess

class processHistogramRandomSplitter(object):

    def __init__(self, pathInput, pathOutput, iteration, splitter):

        self.pathInput = pathInput
        self.pathOutput = pathOutput
        self.iteration = iteration
        self.splitter = splitter
        self.performanceObjectList = []
        self.ListGroups = ['A_random', 'B_random', 'C_random', 'F_random', 'H_random', 'M_random', 'N_random', 'O_random', 'P_random', 'R_random', 'T_random', 'U_random', 'Z_random']

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
            for element in self.ListGroups:
                pathRead = "%siteration_%d/%s/performanceTrainingWithLOU.csv" % (self.pathInput, i, element)
                matrixData = document.document(pathRead, 'pathOutput').readDocument()#obtenemos la matriz
                matrixParser = self.parserMatrix(matrixData)#la parseamos
                matrixParser = matrixParser[1:]
                maxAccuracy = self.getMaxValueCol(matrixParser, 3)
                maxR_call = self.getMaxValueCol(matrixParser, 4)
                maxPrecission = self.getMaxValueCol(matrixParser, 5)

                if maxAccuracy != -1 and maxR_call != -1 and maxPrecission != -1:
                    #instanciamos al objeto... y lo agregamos a la lista...
                    self.performanceObjectList.append(performanceRandom.performanceGroup(element, maxAccuracy, maxR_call, maxPrecission))

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
        for element in self.ListGroups:
            for j in range(len(listPerformance)):
                #formamos el nombre del archivo de salida...
                nameFile = "histogramData_Group_%s_performance_%s.csv" % (element, listPerformance[j])
                nameFilePicture = "%shistogramData_Group_%s_performance_%s.svg" % (self.pathOutput,element, listPerformance[j])
                print "process file: ", nameFile
                self.generateDataExportForHistogram(element, j, nameFile)

                nameFileFull = "%s%s" % (self.pathOutput, nameFile)

                #hacemos la llamada a sistema para la ejecucion del resource R...
                command = "Rscript /home/dmedina/Escritorio/MisProyectos/UChileProyects/trainingdataprotein/scripts/install/resource/rScripts/histogram.R %s %s %s" % (nameFileFull, nameFilePicture, listPerformance[j])
                subprocess.call(command, shell=True)
