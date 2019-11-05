'''
script que permite ejecutar los algoritmos de gausian naive bayes, multinominal naive bayes y bernulli naive bayes

input: matriz de datos normalizados (csv)
input: header
output: diccionario con la informacion de la performance
'''

from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from proyect.CCTraining import performanceScore
from proyect.CCTraining import processPerformance

class naiveBayes(object):

    def __init__(self, matrix, validator):#constructor de la clase...

        self.validator = validator
        self.matrix = matrix
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
    def applyAlgorithmGaussian(self):
        try:
            clf = GaussianNB()
            clf = clf.fit(self.dataWC, self.classAttribute)
            performanceData = performanceScore.performanceAlgoritmo('GaussianNB', 'Naive Bayes algoritmo', str(self.validator))
            performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,self.validator)
            self.performanceDataList.append(performanceData)
        except:
            pass

    #metodo que permite aplicar el algoritmo como bernulli
    def applyAlgorithmBernoulliNB(self):
        try:
            clf = BernoulliNB()
            clf = clf.fit(self.dataWC, self.classAttribute)
            performanceData = performanceScore.performanceAlgoritmo('BernoulliNB', 'Naive Bayes algoritmo', str(self.validator))
            performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,self.validator)
            self.performanceDataList.append(performanceData)
        except:
            pass

    #metodo que permite procesar la performance...
    def processValuesScore(self):

        #llamamos a las aplicaciones de los algoritmos
        self.applyAlgorithmGaussian()
        self.applyAlgorithmBernoulliNB()
        self.scorePerformance = processPerformance.processPerformance(self.performanceDataList)#instancia...
        self.scorePerformance.getValuesPerformance()
