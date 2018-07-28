'''
script con la responsabilidad de ejecutar el entrenamiento de todos los algoritmos de clasificacion implementados para el set de datos full
con validacion cruzada...
'''
from proyect.CCTraining import naiveBayes, adaBoost, knnAlgorithm, decisionTrees, gradientTreeBoost, nuSVC, SVC, randomForest, performanceScore, processPerformance, mlpClf
from proyect.CCTraining import resumeResult
from proyect.CCProcesFile import document
import sys

#recibimos el set de datos con la data normalizada...
matrixNormalized = sys.argv[1]
pathOutput = sys.argv[2]

matrix = document.document(matrixNormalized, pathOutput).readMatrix()#hacemos la lectura de la matriz de datos...

matrix = matrix[1:]
#process matrix for transform data
for i in range (len(matrix)):
    for j in range (len(matrix[i])):

        if j == len(matrix[i])-1:
            matrix[i][j] = int(matrix[i][j])
        else:
            matrix[i][j] = float(matrix[i][j])

naiveBayesValue = naiveBayes.naiveBayes(matrix, 10)
adaBoostValue = adaBoost.adaBoost(matrix, 10)
knnAlgorithmValue = knnAlgorithm.knnAlgorithm(matrix, 10)
decisionTreesValue = decisionTrees.decisionTrees(matrix, 10)
gradientTreeBoostValues = gradientTreeBoost.gradientTreeBoost(matrix, 10)
nuSVCValue = nuSVC.nuSVC(matrix, 10)
SVCValue = SVC.SVCObjet(matrix, 10)
randomForestValue = randomForest.randomForest(matrix, 10)
mlpClfValue = mlpClf.mlpModel(matrix, 10)

ListResultAlgorithm = [naiveBayesValue, adaBoostValue, knnAlgorithmValue, decisionTreesValue, gradientTreeBoostValues, nuSVCValue, SVCValue, randomForestValue, mlpClfValue]

#hacemos la instancia al objeto...
resumen = resumeResult.resumePerformance(ListResultAlgorithm, pathOutput)
