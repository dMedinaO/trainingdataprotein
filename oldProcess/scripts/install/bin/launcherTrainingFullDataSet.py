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
cv = int(sys.argv[3])

matrix = document.document(matrixNormalized, pathOutput).readMatrix()#hacemos la lectura de la matriz de datos...

matrix = matrix[1:]
#process matrix for transform data
for i in range (len(matrix)):
    for j in range (len(matrix[i])):

        if j == len(matrix[i])-1:
            matrix[i][j] = int(matrix[i][j])
        else:
            matrix[i][j] = float(matrix[i][j])

naiveBayesValue = naiveBayes.naiveBayes(matrix, cv)
adaBoostValue = adaBoost.adaBoost(matrix, cv)
knnAlgorithmValue = knnAlgorithm.knnAlgorithm(matrix, cv)
decisionTreesValue = decisionTrees.decisionTrees(matrix, cv)
gradientTreeBoostValues = gradientTreeBoost.gradientTreeBoost(matrix, cv)
nuSVCValue = nuSVC.nuSVC(matrix, cv)
SVCValue = SVC.SVCObjet(matrix, cv)
randomForestValue = randomForest.randomForest(matrix, cv)
mlpClfValue = mlpClf.mlpModel(matrix, cv)

ListResultAlgorithm = [naiveBayesValue, adaBoostValue, knnAlgorithmValue, decisionTreesValue, gradientTreeBoostValues, nuSVCValue, SVCValue, randomForestValue, mlpClfValue]

#hacemos la instancia al objeto...
resumen = resumeResult.resumePerformance(ListResultAlgorithm, pathOutput)
