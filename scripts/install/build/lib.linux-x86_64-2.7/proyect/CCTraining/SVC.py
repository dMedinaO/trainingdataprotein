'''
script que permite ejecutar los algoritmos de gausian naive bayes, multinominal naive bayes y bernulli naive bayes

input: matriz de datos normalizados (csv)
output: diccionario con la informacion de la performance
'''

from sklearn.svm import SVC
from proyect.CCTraining import performanceScore
from proyect.CCTraining import processPerformance

class SVCObjet(object):

    def __init__(self, matrix):#constructor de la clase...

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
            print "SVC, kernel: %s" % kernel
            clf = SVC(kernel=kernel, degree=3, gamma=10, probability=True)
            clf = clf.fit(self.dataWC, self.classAttribute)
            descripcion = "SVC"
            performanceData = performanceScore.performanceAlgoritmo(kernel, descripcion, 'CV=10')
            performanceData.estimatedMetricsPerformance(clf, self.dataWC, self.classAttribute,10)
            self.performanceDataList.append(performanceData)

    #metodo que permite procesar la performance...
    def processValuesScore(self):

        #llamamos a las aplicaciones de los algoritmos
        self.applyAlgorithm()
        self.scorePerformance = processPerformance.processPerformance(self.performanceDataList)#instancia...
        self.scorePerformance.getValuesPerformance()
