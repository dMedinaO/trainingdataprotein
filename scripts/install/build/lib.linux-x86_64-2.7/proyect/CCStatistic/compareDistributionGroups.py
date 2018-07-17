'''
clase con la responsabilidad de recibir dos archivos csv, extraer la informacion y evaluar mediante test estadisticos
si las distribuciones que estos representan son iguales o no, el obetivo general es comparar las distribuciones maximas de performance
'''

from proyect.CCProcesFile import document
from scipy.stats import mannwhitneyu

class compareDist(object):

    def __init__(self, pathInput, pathOutput, numberGroup):

        self.pathInput = pathInput
        self.pathOutput = pathOutput
        self.numberGroup = numberGroup
        self.ListGroups = ['A', 'B', 'C', 'F', 'H', 'M', 'N', 'O', 'P', 'R', 'T', 'U', 'Z']

    #metodo que permite calcular el factorial...
    def getFactorialData(self, number):

        prod =1
        for i in range (1, number+1):
            prod*=i
        return prod

    #metodo que permite obtener las posibles combinaciones...
    def getPossibleCombination(self):

        num = self.getFactorialData(self.numberGroup)
        div = self.getFactorialData(2)*self.getFactorialData(self.numberGroup-2)

        return int(num/div)

    #metodo que recibe una lista y la transforma a flotante...
    def transformFloat(self, listData):

        for i in range(len(listData)):
            listData[i] = float(listData[i])
        return listData

    #metodo que permite chequear las hipotesis...
    def checkHipotesis(self, valueCorrection, prob):

        if prob <=valueCorrection:
            return "Diferentes"
        else:
            return "Iguales"
    #metodo que permite manejar las comparaciones...
    def handlerCompareProcess(self):

        valueCorrection = (0.05 / self.getPossibleCombination())

        header = ["Element A", "Element B", "statistic", "P-Value", "correction Data", "response"]
        matrixResponse = []
        for i in range (1, self.numberGroup+1):
            for j in range(1, self.numberGroup+1):
                if i != j:
                    rowCompare = []
                    rowCompare.append(i)
                    rowCompare.append(j)
                    #formamos el nombre de los archivos...
                    nameA = "%scsv/histogramData_Group_group_%s_performance_accuracy.csv" % (self.pathInput, self.ListGroups[i-1])
                    nameB = "%scsv/histogramData_Group_group_%s_performance_accuracy.csv" % (self.pathInput, self.ListGroups[j-1])

                    #hacemos las lecturas de los archivos...
                    doc = document.document(nameA, self.pathOutput)
                    dataA = self.transformFloat(doc.readDocument()[1:])

                    doc = document.document(nameB, self.pathOutput)
                    dataB = self.transformFloat(doc.readDocument()[1:])

                    #hacemos el analisis estadistico con man whitney test
                    u, prob = mannwhitneyu(dataA, dataB)
                    rowCompare.append(u)
                    rowCompare.append(prob)
                    rowCompare.append(valueCorrection)
                    rowCompare.append(self.checkHipotesis(valueCorrection, prob))
                    matrixResponse.append(rowCompare)

        #exportamos el documento...
        exportFile = "compareDistributionIntraGroups.csv"

        #exportamos...
        doc2 = document.document(exportFile, self.pathOutput)
        doc2.createExportFileWithPandas(matrixResponse, header)
