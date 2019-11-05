'''
clase que permite poder ejecutar las diversas acciones asociadas al tratamiento de datos, el procesamiento de la
informacion, la generacion de estadisticas y los entrenamientos de modelos...
'''

from proyect.CCProcesFile import procesFile
from proyect.CCStatistic import normalize, createHistogramForAttributeWebView, scatterPlotMatrix, createMatrixCoor
from proyect.CCTraining import naiveBayes, adaBoost, knnAlgorithm, decisionTrees, gradientTreeBoost, nuSVC, SVC, randomForest, performanceScore, processPerformance, mlpClf
from proyect.CCTraining import resumeResult
from proyect.CCStatistic import boxPlotData

import sys
import os
import subprocess

#recibimos los datos de entrada...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]

pathOutputProcessFile = pathOutput+"inputFile/"
command = "mkdir -p %s" % pathOutputProcessFile
subprocess.call(command, shell=True)

#hacemos la instancia al procesamiento de la informacion....
process = procesFile.processDataSet(nameFile, pathOutputProcessFile, ',')
process.processMatrixData()
process.checkAttributesInMatrix()

#generacion de estadisticas... #creacion del path...
pathOutputStatistic = pathOutput+"statistic/"
command = "mkdir -p %s" % pathOutputStatistic
subprocess.call(command, shell=True)

'''
#histogramas... creamos el directorio...
pathHistogram = pathOutputStatistic+"histogram/"
command = "mkdir -p %s" % pathHistogram
subprocess.call(command, shell=True)

for i in range (len(process.header)-1):#para todos los elementos menos la clase...
    dataExport = process.getDataByIndex(i)
    nameFileExport = "%s%s_Histograme.js" % (pathHistogram, process.header[i])
    title = "Histogram for %s" % process.header[i]
    webHistogram = createHistogramForAttributeWebView.createHistograma(dataExport, nameFileExport, title)
    webHistogram.createFile()
'''

#hacemos el scatter plot...
pathScatter = pathOutputStatistic+"scatterPloy/"
command = "mkdir -p %s" % pathScatter
subprocess.call(command, shell=True)

#scatter = scatterPlotMatrix.scatterMatrixPlot( process.matrixData, process.header, pathScatter, process.header[-1])
#scatter.exportScatter()

#hacemos la matriz de correlacion...
pathCorr = pathOutputStatistic+"correlation/"
command = "mkdir -p %s" % pathCorr
subprocess.call(command, shell=True)

correlationOb = createMatrixCoor.correlationMatrix( process.matrixData, process.header, pathCorr, 'Correlation matrix between the features')
correlationOb.exportMatrixCor()

'''
#hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
pathOuputNormaliced = "%sNormaliced/" % pathOutput
command = "mkdir -p %sNormaliced" % pathOutput
subprocess.call(command, shell=True)
normalObject = normalize.NormalizeData(process.header, process.matrixData, pathOuputNormaliced)
normalObject.createMatrixNorm()

#comenzamos con la ejecucion de los algoritmos de aprendizaje supervisado...
#naiveBayesValue = naiveBayes.naiveBayes(normalObject.matrixNormalized, 10)
#adaBoostValue = adaBoost.adaBoost(normalObject.matrixNormalized, 10)
#knnAlgorithmValue = knnAlgorithm.knnAlgorithm(normalObject.matrixNormalized, 10)
#decisionTreesValue = decisionTrees.decisionTrees(normalObject.matrixNormalized, 10)
#gradientTreeBoostValues = gradientTreeBoost.gradientTreeBoost(normalObject.matrixNormalized, 10)
#nuSVCValue = nuSVC.nuSVC(normalObject.matrixNormalized, 10)
#SVCValue = SVC.SVCObjet(normalObject.matrixNormalized, 10)
#randomForestValue = randomForest.randomForest(normalObject.matrixNormalized, 10)

mlpClfValue = mlpClf.mlpModel(normalObject.matrixNormalized, 10)
ListResultAlgorithm = [mlpClfValue]

#hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
pathOuputTraining = "%sTraining/" % pathOutput
command = "mkdir -p %sTraining" % pathOutput
subprocess.call(command, shell=True)

#hacemos la instancia al objeto...
resumen = resumeResult.resumePerformance(ListResultAlgorithm, pathOuputTraining)
'''
