'''
clase que permite tomar las distribuciones de performance, leerlas y obtener el algoritmo que corresponde junto con los parametros de interes para aplicar
el modelo a nuevos set de datos...
pathResponse es donde se encuentran los csv con las mejores performance...
pathRoot es donde se encuentran las iteraciones para acceder a las medidas de desempeno...
'''

from proyect.CCModels import modelSelected
from proyect.CCProcesFile import document
import numpy as np
import subprocess
import pandas as pd
import sys

class bestModel(object):

    def __init__(self, pathResponse, group, pathRoot, pathOutput):

        self.pathResponse = pathResponse
        self.pathRoot = pathRoot
        self.group = group
        self.pathOutput = pathOutput
        self.dictOutliers = {}
        self.ListModels = []
        self.ListGroups = ['A', 'B', 'C', 'F', 'H', 'M', 'N', 'O', 'P', 'R', 'T', 'U', 'Z']
    #metodo que recibe una lista y la transforma a flotante...
    def transformFloat(self, listData):

        for i in range(len(listData)):
            listData[i] = float(listData[i])
        return listData

    #metodo que genera la lectura del archivo de las distribuciones...
    def getBestPerformanceDist(self):

        print "searching outliers in sampling"
        for i in range (1, self.group+1):

            print "Process group ", i
            #por cada grupo obtenemos la informacion...
            nameFile = "%scsv/histogramData_Group_group_%s_performance_accuracy.csv" % (self.pathResponse, self.ListGroups[i-1])
            doc = document.document(nameFile, '')
            data = doc.readDocument()[1:]

            #searching outliers
            self.dictOutliers.update({self.ListGroups[i-1]:self.getOutliersForGroup(data)})

    #metodo que permite tener los outliers para el grupo...
    def getOutliersForGroup(self, data):

        data = self.transformFloat(data)
        mean = np.mean(data)
        std = np.std(data)

        outliers = [x for x in data if (x >= mean + 1.5 * std)]

        return outliers

    #metodo que recibe el nombre de un archivo y hace la busqueda de la performance para obtener los resultados de interes...
    def getParams(self, nameFile, performance):

        #leemos el documento
        df = pd.read_csv(nameFile)
        matrixResponse = []
        for i in range (len(df['Accuracy'])):
            if performance == df['Accuracy'][i]:
                row = []
                row.append(df['algorithm'][i])
                row.append(df['description'][i])

                matrixResponse.append(row)
            else:
                dif = abs(performance-df['Accuracy'][i])
                if dif <=0.0001:
                    row = []
                    row.append(df['algorithm'][i])
                    row.append(df['description'][i])

                    matrixResponse.append(row)
        return matrixResponse

    #metodo que permite buscar los parametros y el algoritmo ademas de la iteracion en la que se encuentra de cada outliers...
    def searchParamForOutlier(self):

        for key in self.dictOutliers:

            #formamos el path...
            print "created dir ", key
            pathCreated = "%s%s/" % (self.pathOutput, key)
            command = "mkdir -p %s" % pathCreated
            subprocess.call(command, shell=True)

            #comenzamos la busqueda de cada outlier en cada iteracion para obtener los parametros, no se hara un break debido a que puede que distintas muestras den el mismo performance...
            for i in range (1, 101):
                #formamos el path con el archivo de interes...
                pathInput = "%s%d_iteration/group_%s/performanceTrainingWithLOU.csv" % (self.pathRoot, i, key)
                for performance in self.dictOutliers[key]:
                    response = self.getParams(pathInput, performance)
                    #hacemos la insercion de elementos a la lista de diccionarios...
                    for element in response:
                        #instanciamos al objeto...
                        modelO = modelSelected.modelData(element[0], element[1], 'LOU', performance, key, i)
                        self.ListModels.append(modelO)

    #metodo que permite recibir la lista y exportar el archivo...
    def exportDocument(self):
        print "Export document"
        for i in range (1, self.group+1):
            matrixExport = []
            for element in self.ListModels:
                if element.group == self.ListGroups[i-1]:
                    row = [element.algorithm, element.description, element.validation, element.accuracy, element.group, element.iterator]
                    matrixExport.append(row)
            nameDoc = "resumeOutlierGroup_%d.csv" % i
            doc = document.document(nameDoc, self.pathOutput+self.ListGroups[i-1]+"/")
            doc.createExportFileWithPandas(matrixExport, ['algorithm', 'description', 'validation', 'accuracy', 'group', 'iterator'])
