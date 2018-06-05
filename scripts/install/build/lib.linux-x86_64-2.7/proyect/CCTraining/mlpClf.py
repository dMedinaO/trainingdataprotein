'''
clase que permite aplicar el algoritmo de MLP  a los diferentes set de datos...
'''
from sklearn.neural_network import MLPClassifier

from proyect.CCTraining import performanceScore
from proyect.CCTraining import processPerformance

class mlpModel(object):

    def __init__(self, matrix, validator):#constructor de la clase...

        self.validator = validator
        self.matrix = matrix
        self.activationList = ['identity', 'logistic', 'tanh', 'relu']
        self.solverList = ['lbfgs', 'sgd', 'adam']
        self.learning_rateList = ['constant', 'invscaling', 'adaptive']
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

        for activation in self.activationList:
            for solver in self.solverList:
                for learning_rate in self.learning_rateList:
                    try:
                        print "MLPClassifier, activation: %s, solver: %s, learning_rate: %s" % (activation, solver, learning_rate)
                        clf = MLPClassifier(hidden_layer_sizes=(30,30,30), activation=activation, solver=solver, learning_rate=learning_rate)
                        clf = clf.fit(self.dataWC, self.classAttribute)
                        descripcion = "MLPClassifier, activation: %s, solver: %s, learning_rate: %s" % (activation, solver, learning_rate)
                        performanceData = performanceScore.performanceAlgoritmo('MLP', descripcion, str(self.validator))
                        performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,self.validator)
                        self.performanceDataList.append(performanceData)
                    except:
                        pass

    #metodo que permite procesar la performance...
    def processValuesScore(self):

        #llamamos a las aplicaciones de los algoritmos
        self.applyAlgorithm()
        self.scorePerformance = processPerformance.processPerformance(self.performanceDataList)#instancia...
        self.scorePerformance.getValuesPerformance()
