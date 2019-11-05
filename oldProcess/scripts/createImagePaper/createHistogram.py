'''
script que permite crear histogramas con distintas visualizaciones asociadas al set de datos de interes...
Considerando las distintas metricas de un distribuidor de desempeno...
'''

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#funcio que permite crear una fila de un dataset...
def createRowDataSet(dataset, keyData, index):

    row = []

    for element in keyData:
        row.append(dataset[element][index])
    return row

#funcion que permite generar una matriz con los datos del dataframe
def createMatrixData(dataset, keyData):

    matrixValue = []

    for i in range (len(dataset)):
        matrixValue.append(createRowDataSet(dataset, keyData, i))

    return matrixValue

#funcion que permite crear un histograma...
def createHistogram(dataSet, key, nameExport, title):

    plt.figure()
    sns.set(color_codes=True)
    sns.set(style="ticks")
    sns_plot = sns.distplot( dataSet[key] , color="olive", label=key, kde=False, rug=True)
    sns.plt.legend()
    sns.plt.title(title)
    sns_plot.figure.savefig(nameExport)

#funcion que permite crear un histograma por set de datos...
def createHistogramByDataSet(dataSet, nameExport):
    plt.figure();
    sns.set(color_codes=True)
    sns.set(style="ticks")
    dataSet.plot.hist(alpha=0.5, bins=15)
    sns.plt.legend()
    sns.plt.title("Histogram for performance in model")
    plt.savefig(nameExport)

#recibimos los datos de entrada...
dataSet = pd.read_csv(sys.argv[1])
pathOutput = sys.argv[2]

#manipulamos el set de datos solo para considerar los elementos de interes...
matrixValue = createMatrixData(dataSet, ['Accuracy', 'Recall', 'Precision'])
dataSetInteres = pd.DataFrame(matrixValue, columns=['Accuracy', 'Recall', 'Precision'])

createHistogramByDataSet(dataSetInteres, pathOutput+"Histogram_Multiple.png")

for element in dataSetInteres:
    title = "Histogram for %s values" % element
    nameExport = pathOutput+element+"_Histogram.png"
    createHistogram(dataSetInteres, element, nameExport, title)
