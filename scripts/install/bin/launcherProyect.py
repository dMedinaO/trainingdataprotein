'''
clase que permite poder ejecutar las diversas acciones asociadas al tratamiento de datos, el procesamiento de la
informacion, la generacion de estadisticas y los entrenamientos de modelos...
'''

from proyect.CCProcesFile import procesFile
from proyect.CCStatistic import normalize
from proyect.CCTraining import naiveBayes, adaBoost, knnAlgorithm, decisionTrees, gradientTreeBoost, nuSVC, SVC, randomForest, performanceScore, processPerformance
from proyect.CCTraining import resumeResult

import sys
import os
import subprocess

#funcion que permite agregar los elementos de los resultados al arreglo...
def addElementPerformanceResponse(ListPerformance, listFull):

    for element in ListPerformance:
        listFull.append(element)

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

#hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
pathOuputNormaliced = "%sNormaliced/" % pathOutput
command = "mkdir -p %sNormaliced" % pathOutput
subprocess.call(command, shell=True)
normalObject = normalize.NormalizeData(process.header, process.matrixData, pathOuputNormaliced)
normalObject.createMatrixNorm()

#comenzamos con la ejecucion de los algoritmos de aprendizaje supervisado...
naiveBayesValue = naiveBayes.naiveBayes(normalObject.matrixNormalized)
adaBoostValue = adaBoost.adaBoost(normalObject.matrixNormalized)
knnAlgorithmValue = knnAlgorithm.knnAlgorithm(normalObject.matrixNormalized)
decisionTreesValue = decisionTrees.decisionTrees(normalObject.matrixNormalized)
gradientTreeBoostValues = gradientTreeBoost.gradientTreeBoost(normalObject.matrixNormalized)
nuSVCValue = nuSVC.nuSVC(normalObject.matrixNormalized)
SVCValue = SVC.SVCObjet(normalObject.matrixNormalized)
randomForestValue = randomForest.randomForest(normalObject.matrixNormalized)

ListResultAlgorithm = [naiveBayesValue, adaBoostValue, knnAlgorithmValue, decisionTreesValue, gradientTreeBoostValues, nuSVCValue, SVCValue, randomForestValue]

#hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
pathOuputTraining = "%sTraining/" % pathOutput
command = "mkdir -p %sTraining" % pathOutput
subprocess.call(command, shell=True)

#hacemos la instancia al objeto...
resumen = resumeResult.resumePerformance(ListResultAlgorithm, pathOuputTraining)
