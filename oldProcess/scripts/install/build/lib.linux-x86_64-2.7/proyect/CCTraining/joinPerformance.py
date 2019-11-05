'''
clase con la responsabilidad de poder unir los procesos de entrenamiento con el fin de poder obtener cada lista de resultados
y calcular los promedios para la muestra general...
'''

import sys
import pandas as pd
import numpy as np
from proyect.CCProcesFile import document

class joinPerformance(object):

    def __init__(self, pathData):

        self.pathData = pathData

    #metodo que permite hacer las multiples lecturas de archivo y almacenar la data en un array...
    def getDataFromCSV(self):

        joinedProcess = []
        for i in range (1, 11):
            nameFile = "%s%d.csv" % (self.pathData, i)
            dataMatrix = pd.read_csv(nameFile)
            joinedProcess.append(dataMatrix)
        return joinedProcess

    #metodo que permita hacer los calculos correspondientes segun la columna y fila que corresponda...
    def processData(self):

        self.matrixData = [] #contendra la nueva matriz...
        matrixFull = self.getDataFromCSV()

        header = ['algorithm',	'description', 'validation', 'Accuracy_Mean', 'Accuracy_SD', 'Accuracy_Var', 'Accuracy_MIN', 'Accuracy_MAX', 'recall_Mean', 'recall_SD', 'recall_Var', 'recall_MIN', 'recall_MAX', 'precision_Mean', 'precision_SD', 'precision_Var', 'precision_MIN', 'precision_MAX', 'tn', 'fp', 'fn', 'tp']
        for i in range (len(matrixFull[0])):

            row = []
            row.append(matrixFull[0]['algorithm'][i])#algorithm
            row.append(matrixFull[0]['description'][i])#description
            row.append(matrixFull[0]['validation'][i])#validation

            Accuracy_Mean = []
            Accuracy_SD = []
            Accuracy_Var = []
            Accuracy_MIN = []
            Accuracy_MAX = []
            recall_Mean = []
            recall_SD = []
            recall_Var = []
            recall_MIN = []
            recall_MAX = []
            precision_Mean = []
            precision_SD = []
            precision_Var = []
            precision_MIN = []
            precision_MAX = []
            tn = []
            fp = []
            fn = []
            tp = []

            for j in range (len(matrixFull)):
                Accuracy_Mean.append(matrixFull[j]['Accuracy_Mean'][i])
                Accuracy_SD.append(matrixFull[j]['Accuracy_SD'][i])
                Accuracy_Var.append(matrixFull[j]['Accuracy_Var'][i])
                Accuracy_MIN.append(matrixFull[j]['Accuracy_MIN'][i])
                Accuracy_MAX.append(matrixFull[j]['Accuracy_MAX'][i])
                recall_Mean.append(matrixFull[j]['recall_Mean'][i])
                recall_SD.append(matrixFull[j]['recall_SD'][i])
                recall_Var.append(matrixFull[j]['recall_Var'][i])
                recall_MIN.append(matrixFull[j]['recall_MIN'][i])
                recall_MAX.append(matrixFull[j]['recall_MAX'][i])
                precision_Mean.append(matrixFull[j]['precision_Mean'][i])
                precision_SD.append(matrixFull[j]['precision_SD'][i])
                precision_Var.append(matrixFull[j]['precision_Var'][i])
                precision_MIN.append(matrixFull[j]['precision_MIN'][i])
                precision_MAX.append(matrixFull[j]['precision_MAX'][i])
                tn.append(matrixFull[j]['tn'][i])
                fp.append(matrixFull[j]['fp'][i])
                fn.append(matrixFull[j]['fn'][i])
                tp.append(matrixFull[j]['tp'][i])

            row.append(np.mean(Accuracy_Mean))
            row.append(np.mean(Accuracy_SD))
            row.append(np.mean(Accuracy_Var))
            row.append(min(Accuracy_MIN))
            row.append(max(Accuracy_MAX))
            row.append(np.mean(recall_Mean))
            row.append(np.mean(recall_SD))
            row.append(np.mean(recall_Var))
            row.append(min(recall_MIN))
            row.append(max(recall_MAX))
            row.append(np.mean(precision_Mean))
            row.append(np.mean(precision_SD))
            row.append(np.mean(precision_Var))
            row.append(min(precision_MIN))
            row.append(max(precision_MAX))
            row.append(np.mean(tn))
            row.append(np.mean(fp))
            row.append(np.mean(fn))
            row.append(np.mean(tp))

            self.matrixData.append(row)

        #exportamos la data de interes...
        document.document("joinedTraining.csv" ,self.pathData).createExportFileWithPandas(self.matrixData, header)

def main():

    dataProcess = joinPerformance(sys.argv[1])
    dataProcess.processData()

    return 0

if __name__ == '__main__':
    main()
