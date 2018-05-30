'''
script que permite procesar los entrenamientos de modelos mediante la aplicacion de LeaveOneOut
recibe como entrada un archivo con la informacion de los grupos, accede a cada directorio
y procesa la informacion existente...

Trabaja con la data normalizada...

Como salida, genera un archivo de entrenamiento por cada divisor...
'''
from proyect.CCProcesFile import procesFile
from proyect.CCTraining.LOU import knnAlgorithm, adaBoost, decisionTrees, gradientTreeBoost, naiveBayes, nuSVC, randomForest, SVC
from proyect.CCTraining.LOU import processResult

import sys
import pandas as pd

#recibimos los datos de entrada...
namePathInput = sys.argv[1]
nameCSV= sys.argv[2]
nameFileCSV = namePathInput+nameCSV

#hacemos la lectura del archivo
df = pd.read_csv(nameFileCSV, sep=',')

#por cada grupo hacemos el entrenamiento...
for i in range(len(df['grupo'])):
    ListResultAlgorithm = []
    #accedemos al directorio...
    dirData = namePathInput+df['grupo'][i]+"_Attribute/"
    dirDataNormal = dirData+"normaliced/dataSetNormaliced.csv"

    process = procesFile.processDataSet(dirDataNormal, 'pathOutput', ',')
    process.processMatrixData()

    try:
        #aplicamos naiveBayes
        print "Apply GaussianNB"
        naiveBayesGB = naiveBayes.naiveBayes(process.matrixData)
        naiveBayesGB.applyAlgorithmGaussian()
        ListResultAlgorithm.append(naiveBayesGB.performanceValues)
    except:
        pass
    try:
        print "Apply BernoulliNB"
        naiveBayesBB = naiveBayes.naiveBayes(process.matrixData)
        naiveBayesBB.applyAlgorithmBernoulliNB()
        ListResultAlgorithm.append(naiveBayesBB.performanceValues)
    except:
        pass

    #aplicamos SVC
    for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
        try:
            print "Apply SVC %s" % kernel
            SVCValues = SVC.SVCObjet(process.matrixData, kernel)
            SVCValues.applyAlgorithm()
            ListResultAlgorithm.append(SVCValues.performanceValues)
        except:
            pass

    #aplicamos randomForest
    for criterion in ['gini', 'entropy']:
        for estimator in [10, 20, 50, 100, 150, 200, 250, 500, 750, 1000, 1500]:
            try:
                print "Apply randomForest %s, %d" % (criterion, estimator)
                randomForestValues = randomForest.randomForest(process.matrixData, criterion, estimator)
                randomForestValues.applyAlgorithm()
                ListResultAlgorithm.append(randomForestValues.performanceValues)
            except:
                pass

    #aplicamos NuSVC
    for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
        try:
            print "Apply NuSVC %s" % kernel
            nuSVCValues = nuSVC.nuSVC(process.matrixData, kernel)
            nuSVCValues.applyAlgorithm()
            ListResultAlgorithm.append(nuSVCValues.performanceValues)
        except:
            pass
    #aplicamos arboles de decision...
    for estimator in [10, 20, 50, 100, 150, 200, 250, 500, 750, 1000, 1500]:
        try:
            print "Apply GradientBoostingClassifier %d" % estimator
            gradientTreeBoostValue = gradientTreeBoost.gradientTreeBoost(process.matrixData, estimator)
            gradientTreeBoostValue.applyAlgorithm()
            ListResultAlgorithm.append(gradientTreeBoostValue.performanceValues)
        except:
            pass

    #aplicamos arboles de decision...
    for criterion in ['gini', 'entropy']:
        for splitter in ['best', 'random']:
            try:
                print "Apply DecisionTreeClassifier %s %s" % (criterion, splitter)
                decisionTreesValue = decisionTrees.decisionTrees(process.matrixData, criterion, splitter)
                decisionTreesValue.applyAlgorithm()
                ListResultAlgorithm.append(decisionTreesValue.performanceValues)
            except:
                pass

    #aplicamos adaBoost...
    for algorithm in ['SAMME', 'SAMME.R']:
        for estimator in [10, 20, 50, 100, 150, 200, 250, 500, 750, 1000, 1500]:
            try:
                print "Apply adaBoost: %d, %s" % (estimator, algorithm)
                adaBoostValue = adaBoost.adaBoostLOU(process.matrixData, algorithm, estimator)
                adaBoostValue.applyAlgorithm()
                ListResultAlgorithm.append(adaBoostValue.performanceValues)
            except:
                pass

    #aplicamos knn...
    for algorithm in ['auto', 'ball_tree', 'kd_tree', 'brute']:
        for weight in ['uniform', 'distance']:
            for metric in ['minkowski', 'euclidean']:
                for i in range(2, 5):
                    try:
                        print "Apply KNN: %d, %s, %s, %s" % (i, algorithm, weight, metric)
                        knn = knnAlgorithm.knnAlgorithmLOU(process.matrixData, algorithm, weight, metric, i)
                        knn.applyAlgorithm()
                        ListResultAlgorithm.append(knn.performanceValues)
                    except:
                        pass
    #procesamos la salida...
    dirDataTraining = dirData+"training/"
    nameFile = "performanceTrainingWithLOU.csv"
    #procesamos los resultados...
    resultProcess = processResult.exportResult(ListResultAlgorithm, dirDataTraining, nameFile)
    resultProcess.processMatrixValues()
    resultProcess.exportMatrix()
