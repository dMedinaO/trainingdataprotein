'''
clase que tiene la responsabilidad de entrenar un knn con diversas variables mediante el uso de
la tecnica leave one out...
'''

from proyect.CCTraining.LOU import performance
from proyect.CCTraining.LOU import performanceScoreValues
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneOut
import numpy as np

class randomForest(object):

    def __init__(self, matrix, criterion, estimator):

        self.matrix = matrix
        self.criterion = criterion
        self.estimator = estimator
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
            clf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=self.estimator, n_jobs=-1, criterion=self.criterion)
            clf = clf.fit(x_training, y_training)

            self.processPerformance(clf, x_test, y_test)

        #hacemos la instancia al performanceScoreValues
        desc = "%s - %d" % (self.criterion, self.estimator)
        self.performanceValues = performanceScoreValues.performanceScoreValues("RandomForestClassifier",desc, 'LOU', self.performaceObject)