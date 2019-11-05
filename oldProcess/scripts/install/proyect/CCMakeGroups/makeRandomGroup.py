'''
clase con la responsabilidad de generar grupos aleatorios con las mismas caracteristicas que los grupos que son generados
por la division por sector superfice...
'''

import subprocess
import random
from proyect.CCProcesFile import document
from proyect.CCProcesFile import procesFile
from proyect.CCStatistic import normalize
from proyect.CCTraining.LOU import knnAlgorithm, adaBoost, decisionTrees, gradientTreeBoost, naiveBayes, nuSVC, randomForest, SVC
from proyect.CCTraining.LOU import processResult

class makeGroup(object):

    def __init__(self, dictGroup, matrixData, header, path):

        self.dictGroup = dictGroup
        self.matrixData = matrixData
        self.header = header
        self.path = path

        self.processGroup()

    def __init__(self):

        print "void building"

    #metodo que permite generar los grupos dado el diccionario obtenido...
    def processGroup(self):

        for element in self.dictGroup:
            self.createGroup(element, self.dictGroup[element])

    #metodo que permite generar los grupos con respecto a la informacion del diccionario...
    def createGroup(self, nameGroup, elements):

        print "Create directory for group..."
        dirPath = "%s%s_random/" % (self.path, nameGroup)
        self.createDirPath(dirPath)#creamos el directorio
        matrixRandom = self.createRandomMatrix(elements)#creamos los elementos aleatorios...

        #generamos el archivo de salida...
        print "Create document input for random group..."
        document.document('dataSetRandom.csv', dirPath).createExportFileWithPandas(matrixRandom, self.header)
        print "Process documento..."
        process = self.processRandomMatrix(dirPath)#procesamos la matrix y generamos la transformacion...
        try:
            print "Normalice Process..."
            self.normalizacionData(dirPath, process)
        except:
            pass
        try:
            #creamos el directorio de entrenamiento...
            print "Training Data Set..."
            dirDataNormal = dirPath+"dataSetNormaliced.csv"
            self.trainingModelDataSet(dirDataNormal, dirPath)
        except:
            pass

    #metodo que permite poder implementar el entrenamiento del modelo, las validaciones seran con LOU
    def trainingModelDataSet(self, dirDataNormal, dirDataTraining):

        process = procesFile.processDataSet(dirDataNormal, 'pathOutput', ',')
        process.processMatrixData()
        ListResultAlgorithm = []
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
        #aplicamos redes neuronales...
        for activation in ['identity', 'logistic', 'tanh', 'relu']:
            for solver in ['lbfgs', 'sgd', 'adam']:
                for learning_rate in ['constant', 'invscaling', 'adaptive']:
                    ListCapas = [5, 10, 15]
                    for c1 in ListCapas:
                        for c2 in ListCapas:
                            for c3 in ListCapas:
                                try:
                                    print "MLPClassifier, activation: %s, solver: %s, learning_rate: %s %dX%dX%d" % (activation, solver, learning_rate, c1, c2, c3)
                                    mlp = mlpClassifier.mlpClassifier(process.matrixData, activation, solver, learning_rate, c1, c2, c3)
                                    mlp.applyAlgorithm()
                                    ListResultAlgorithm.append(mlp.performanceValues)
                                except:
                                    pass

        #procesamos la salida...
        nameFile = "performanceTrainingWithLOU.csv"
        #procesamos los resultados...
        resultProcess = processResult.exportResult(ListResultAlgorithm, dirDataTraining, nameFile)
        resultProcess.processMatrixValues()
        resultProcess.exportMatrix()

    #metodo que permite la normalizacion del set de datos...
    def normalizacionData(self, pathValue, process):

        normalObject = normalize.NormalizeData(process.header, process.matrixData, pathValue)
        normalObject.createMatrixNorm()

    #metodo que permite hacer el procesamiento de la matriz generada aleatoriamente...
    def processRandomMatrix(self, dirPath):

        #con el archivo generado podemos procesarlo
        nameDocument = dirPath+"dataSetRandom.csv"
        process = procesFile.processDataSet(nameDocument, dirPath, ',')#instancia al procesador de informacion...
        process.processMatrixData()#procesamos la matriz...
        process.checkAttributesInMatrix()#aplicamos la transformacion....
        return process
    #metodo que permite extraer elementos de la matriz principal...
    def createRandomMatrix(self, numberElement):

        matrixRandom = []
        for i in range(numberElement):
            randomValue = random.randrange(len(self.matrixData))
            matrixRandom.append(self.matrixData[randomValue])
        return matrixRandom

    #metodo que permite crear un directorio asociado al grupo...
    def createDirPath(self, pathValue):
        command = "mkdir -p %s" % pathValue
        subprocess.call(command, shell=True)
