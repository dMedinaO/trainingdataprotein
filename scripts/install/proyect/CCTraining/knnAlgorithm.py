'''
script que permite ejecutar los algoritmos de gausian naive bayes, multinominal naive bayes y bernulli naive bayes

input: matriz de datos normalizados (csv)
output: diccionario con la informacion de la performance
'''

from sklearn.neighbors import KNeighborsClassifier
from proyect.CCTraining import performanceScore
from proyect.CCTraining import processPerformance

class knnAlgorithm(object):

    def __init__(self, matrix, validator):#constructor de la clase...

        self.validator = validator
        self.matrix = matrix
        self.algorithmList = ['auto', 'ball_tree', 'kd_tree', 'brute']
        self.weightsList = ['uniform', 'distance']
        self.metricList = ['minkowski', 'euclidean']

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
            for weight in self.weightsList:
                for metric in self.metricList:
                    for i in range(1,10):#numero de vecinos
                        print "KNN, algorithm: %s, weight: %s, metric: %s, nearest:%d" % (value, weight, metric, i)
                        clf = KNeighborsClassifier(n_neighbors=i,metric=metric,algorithm=value,weights=weight, n_jobs=-1)
                        clf = clf.fit(self.dataWC, self.classAttribute)
                        descripcion = "KNN con %d vecinos peso: %s metrica: %s" % (i, weight, metric)
                        performanceData = performanceScore.performanceAlgoritmo(value, descripcion, str(self.validator))
                        performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,self.validator)
                        self.performanceDataList.append(performanceData)

    #metodo que permite procesar la performance...
    def processValuesScore(self):

        #llamamos a las aplicaciones de los algoritmos
        self.applyAlgorithm()
        self.scorePerformance = processPerformance.processPerformance(self.performanceDataList)#instancia...
        self.scorePerformance.getValuesPerformance()
