'''
script que permite ejecutar los algoritmos de gausian naive bayes, multinominal naive bayes y bernulli naive bayes

input: matriz de datos normalizados (csv)
output: diccionario con la informacion de la performance
'''

from sklearn.svm import NuSVC
from proyect.CCTraining import performanceScore
from proyect.CCTraining import processPerformance

class nuSVC(object):

    def __init__(self, matrix, validator):#constructor de la clase...

        self.validator = validator
        self.matrix = matrix
        self.kernelList = ['linear', 'poly', 'rbf', 'sigmoid']
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

        for kernel in self.kernelList:
            print "NuSVC, kernel: %s" % kernel
            clf = NuSVC(kernel=kernel, degree=3, gamma=10, probability=True)
            clf = clf.fit(self.dataWC, self.classAttribute)
            descripcion = "nuSVC"
            performanceData = performanceScore.performanceAlgoritmo(kernel, descripcion, str(self.validator))
            performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,self.validator)
            self.performanceDataList.append(performanceData)

    #metodo que permite procesar la performance...
    def processValuesScore(self):

        #llamamos a las aplicaciones de los algoritmos
        self.applyAlgorithm()
        self.scorePerformance = processPerformance.processPerformance(self.performanceDataList)#instancia...
        self.scorePerformance.getValuesPerformance()
