'''
script que permite ejecutar los algoritmos de gausian naive bayes, multinominal naive bayes y bernulli naive bayes

input: matriz de datos normalizados (csv)
output: diccionario con la informacion de la performance
'''

from sklearn.ensemble import AdaBoostClassifier
from proyect.CCTraining import performanceScore
from proyect.CCTraining import processPerformance

class adaBoost(object):

    def __init__(self, matrix):#constructor de la clase...

        self.matrix = matrix
        self.algorithmList = ['SAMME', 'SAMME.R']
        self.n_estimatorsList = [10, 20, 50, 100, 150, 200, 250, 500, 750, 1000, 1500]
        self.classAttribute = []
        self.dataWC = []
        self.getClassAndAttributes()
        self.performanceDataList = []#lista con los resultados de las performance...
        self.processValuesScore()#hacemos las ejecuciones correspondientes...

    #metodo que permite separar los atributos, dejando en un array las clases y en otro los valores...
    def getClassAndAttributes(self):

        for element in self.matrix:
            self.dataWC.append(element[:-1])
            self.classAttribute.append(element[-1])

    #metodo que permite aplicar el algoritmo como GaussianNB...
    def applyAlgorithm(self):

        for value in self.algorithmList:
            for estimator in self.n_estimatorsList:
                print "AdaBoostClassifier, algorithm: %s, estimator: %d" % (value, estimator)
                clf = AdaBoostClassifier(n_estimators=estimator, algorithm=value)
                clf = clf.fit(self.dataWC, self.classAttribute)
                descripcion = "AdaBoostClassifier con %d estimadores" % estimator
                performanceData = performanceScore.performanceAlgoritmo(value, descripcion, 'CV=10')
                performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,10)
                self.performanceDataList.append(performanceData)

    #metodo que permite procesar la performance...
    def processValuesScore(self):

        #llamamos a las aplicaciones de los algoritmos
        self.applyAlgorithm()
        self.scorePerformance = processPerformance.processPerformance(self.performanceDataList)#instancia...
        self.scorePerformance.getValuesPerformance()
