'''
clase con la responsabilidad de recibir un archivo csv con las medidas maximas obtenidas en cada iteracion para cada grupo y facilita la
generacion de informacion estadistica de la misma...
'''

from proyect.CCProcesFile import document
import numpy as np

class processStatisticDist(object):

    def __init__(self, group, pathOutput, pathFile):

        self.group = group
        self.pathOutput = pathOutput
        self.pathFile = pathFile
        #self.ListGroups = ['A', 'B', 'C', 'F', 'H', 'M', 'N', 'O', 'P', 'R', 'T', 'U', 'Z']

    #metodo que permite manejar las variables y obtener la informacion...
    def handlerStatistic(self):

        for i in range (1, self.group+1):

            print "Process group ", i
            #por cada grupo obtenemos la informacion...
            nameFile = "%scsv/histogramData_Group_group_%s_performance_accuracy.csv" % (self.pathFile, i)
            doc = document.document(nameFile, self.pathOutput)
            data = self.transformFloat(doc.readDocument()[1:])

            #obtenemos estadisticas de la lista generada...
            mean = ['mean',np.mean(data)]
            maxData = ['max', max(data)]
            minData = ['min', min(data)]
            varData = ['var', np.var(data)]
            stdData = ['std', np.std(data)]

            #formamos la lista nueva...
            dataExport = [mean, maxData, minData, varData, stdData]

            #nameFile Export...
            exportFile = "statistic_Resume_group_%s.csv" %i
            header = ['statistic', 'value']

            #exportamos...
            doc2 = document.document(exportFile, self.pathOutput)
            doc2.createExportFileWithPandas(dataExport, header)


    #metodo que recibe una lista y la transforma a flotante...
    def transformFloat(self, listData):

        for i in range(len(listData)):
            listData[i] = float(listData[i])
        return listData
