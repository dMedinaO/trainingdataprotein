'''
clase que permite poder ejecutar las diversas acciones asociadas al tratamiento de datos, el procesamiento de la
informacion, la generacion de estadisticas y los entrenamientos de modelos...
'''

from proyect.CCProcesFile import procesFile, splitAttributeBySectorSuperfice
from proyect.CCStatistic import normalize, createHistogramForAttributeWebView, scatterPlotMatrix, createMatrixCoor
from proyect.CCTraining import naiveBayes, adaBoost, knnAlgorithm, decisionTrees, gradientTreeBoost, nuSVC, SVC, randomForest, performanceScore, processPerformance
from proyect.CCTraining import resumeResult
from proyect.CCTraining import mlpClf

import sys
import os
import subprocess

#recibimos los datos de entrada...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]

print "Process group"
#hacemos la instancia al procesamiento de la informacion para generar los grupos....
createGroups = splitAttributeBySectorSuperfice.splitterSector(nameFile, pathOutput, ',', 13)
createGroups.makeSplitterBySector()

#por cada lista de grupo: crear directorio para el almacenamiento del normalizado
for element in createGroups.resumeGroup:

    print "transform attribute ", element[0]
    pathProcess = "%s%s_Attribute/inputFileProcess/" % (pathOutput, element[0])
    command = "mkdir -p %s" % pathProcess
    subprocess.call(command, shell=True)
    nameFileInput = "%s%s_Attribute/%s_Attribute.csv" % (pathOutput, element[0], element[0])
    #instanciamos a processFile y ejecutamos el procesamiento del archivo...
    process = procesFile.processDataSet(nameFileInput, pathProcess, ',')
    process.processMatrixData()
    process.checkAttributesInMatrix()

    #trabajamos con las instancias para el desarrollo de los graficos de interes....
    #generacion de estadisticas... #creacion del path...
    pathOutputStatistic = "%s%s_Attribute/statistic/" % (pathOutput, element[0])
    command = "mkdir -p %s" % pathOutputStatistic
    subprocess.call(command, shell=True)

    #hacemos la matriz de correlacion...
    pathCorr = pathOutputStatistic+"correlation/"
    command = "mkdir -p %s" % pathCorr
    subprocess.call(command, shell=True)

    correlationOb = createMatrixCoor.correlationMatrix( process.matrixData, process.header, pathCorr, 'Correlation matrix between the features')
    correlationOb.exportMatrixCor()

'''
    #hacemos el scatter plot...
    pathScatter = pathOutputStatistic+"scatterPlot/"
    command = "mkdir -p %s" % pathScatter
    subprocess.call(command, shell=True)

    scatter = scatterPlotMatrix.scatterMatrixPlot( process.matrixData, process.header, pathScatter, process.header[-1])
    scatter.exportScatter()


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


    #normalizamos...
    print "Normaliced attribute ", element[0]
    #hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
    pathNormaliced = "%s%s_Attribute/normaliced/" % (pathOutput, element[0])
    command = "mkdir -p %s" % pathNormaliced
    subprocess.call(command, shell=True)
    normalObject = normalize.NormalizeData(process.header, process.matrixData, pathNormaliced)
    normalObject.createMatrixNorm()

    #entrenamos...
    print "Training attribute", element[0]
    ListResultAlgorithm = []
    mlpValue = mlpClf.mlpModel(normalObject.matrixNormalized,2)
    ListResultAlgorithm.append(mlpValue)

    try:
        #hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
        pathTraining = "%s%s_Attribute/training/" % (pathOutput, element[0])
        command = "mkdir -p %s" % pathTraining
        subprocess.call(command, shell=True)

        #hacemos la instancia al objeto...
        resumen = resumeResult.resumePerformance(ListResultAlgorithm, pathTraining)
    except:
        pass

    try:

        naiveBayesValue = naiveBayes.naiveBayes(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(naiveBayesValue)
    except:
        pass
    try:
        adaBoostValue = adaBoost.adaBoost(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(adaBoostValue)
    except:
        pass
    try:
        knnAlgorithmValue = knnAlgorithm.knnAlgorithm(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(knnAlgorithmValue)
    except:
        pass

    try:
        decisionTreesValue = decisionTrees.decisionTrees(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(decisionTreesValue)
    except:
        pass
    try:
        gradientTreeBoostValues = gradientTreeBoost.gradientTreeBoost(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(gradientTreeBoostValues)
    except:
        pass

    try:
        nuSVCValue = nuSVC.nuSVC(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(nuSVCValue)
    except:
        pass

    try:
        SVCValue = SVC.SVCObjet(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(SVCValue)
    except:
        pass

    try:
        randomForestValue = randomForest.randomForest(normalObject.matrixNormalized,2)
        ListResultAlgorithm.append(randomForestValue)
    except:
        pass
'''