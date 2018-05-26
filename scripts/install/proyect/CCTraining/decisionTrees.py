'''
script que permite ejecutar los algoritmos de gausian naive bayes, multinominal naive bayes y bernulli naive bayes

input: matriz de datos normalizados (csv)
output: diccionario con la informacion de la performance
'''

from sklearn.tree import DecisionTreeClassifier
from proyect.CCTraining import performanceScore
from proyect.CCTraining import processPerformance

class decisionTrees(object):

    def __init__(self, matrix, validator):#constructor de la clase...

        self.validator = validator
        self.matrix = matrix
        self.criterionList = ['gini', 'entropy']
        self.spliterList = ['best', 'random']

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

        for criterion in self.criterionList:
            for splitter in self.spliterList:
                print "DecisionTreeClassifier, criterion %s, splitter: %s" % (criterion, splitter)
                clf = DecisionTreeClassifier(random_state=0, criterion=criterion, splitter=splitter)
                clf = clf.fit(self.dataWC, self.classAttribute)
                descripcion = "DecisionTreeClassifier splitter:%s" % splitter
                performanceData = performanceScore.performanceAlgoritmo(criterion, descripcion, str(self.validator))
                performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,self.validator)
                self.performanceDataList.append(performanceData)

    #metodo que permite procesar la performance...
    def processValuesScore(self):

        #llamamos a las aplicaciones de los algoritmos
        self.applyAlgorithm()
        self.scorePerformance = processPerformance.processPerformance(self.performanceDataList)#instancia...
        self.scorePerformance.getValuesPerformance()
