'''
clase que tiene la responsabilidad de entrenar un knn con diversas variables mediante el uso de
la tecnica leave one out...
'''

from proyect.CCTraining.LOU import performance
from proyect.CCTraining.LOU import performanceScoreValues
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import LeaveOneOut
import numpy as np

class mlpClassifier(object):

    def __init__(self, matrix, activation, solver, learning_rate, c1, c2, c3):

        self.matrix = matrix
        self.activation = activation
        self.solver = solver
        self.learning_rate = learning_rate
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.dataWC = []
        self.classAttribute = []
        self.convertToFloat()
        self.getClassAndAttributes()
        self.performaceObject = performance.performanceTraining()#para almacenar las performance...

    #metodo para transformar todos los elementos del set de datos a float...
    def convertToFloat(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])-1):
                self.matrix[i][j] = float(self.matrix[i][j])
                self.matrix[i][len(self.matrix[i])-1] = int(self.matrix[i][len(self.matrix[i])-1])

    #metodo que permite separar los atributos, dejando en un array las clases y en otro los valores...
    def getClassAndAttributes(self):

        for element in self.matrix:
            self.dataWC.append(element[:-1])
            self.classAttribute.append(element[-1])

    #metodo que permite estimar las performance del algorithm...
    def processPerformance(self, clf, x_test, y_test):

        prediction = clf.predict(x_test)
        self.performaceObject.calculatePerformance(y_test, prediction)

    #hacemos el entrenamiento con leave one out...
    def applyAlgorithm(self):

        for i in range(len(self.dataWC)):

            #obtenemos el test y su clase...
            x_test = []
            y_test = []
            x_test.append(self.dataWC[i])
            y_test.append(self.classAttribute[i])

            #formamos el training...
            x_training = []
            y_training = []
            for j in range(len(self.dataWC)):
                if i != j:
                    x_training.append(self.dataWC[j])
                    y_training.append(self.classAttribute[j])

            #aplicamos el entrenamiento...
            clf = MLPClassifier(hidden_layer_sizes=(self.c1,self.c2,self.c3), activation=self.activation, solver=self.solver, learning_rate=self.learning_rate)
            clf = clf.fit(x_training, y_training)

            self.processPerformance(clf, x_test, y_test)

        #hacemos la instancia al performanceScoreValues
        desc = "%s-%s-%s (%d-%d-%d)" % (self.activation, self.solver, self.learning_rate, self.c1, self.c2, self.c3)
        self.performanceValues = performanceScoreValues.performanceScoreValues("MLPClassifier",desc, 'LOU', self.performaceObject)
