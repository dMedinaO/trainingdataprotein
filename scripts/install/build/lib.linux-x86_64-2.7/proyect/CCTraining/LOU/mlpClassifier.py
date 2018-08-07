'''
clase que tiene la responsabilidad de entrenar un knn con diversas variables mediante el uso de
la tecnica leave one out...
'''

from proyect.CCTraining.LOU import performance
from proyect.CCTraining.LOU import performanceScoreValues
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import LeaveOneOut, cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix
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

    #hacemos el entrenamiento con leave one out...
    def applyAlgorithm(self):

        accuracy = []
        precision = []
        recall = []
        ListTN = []
        ListFP = []
        ListFN = []
        ListTP = []

        clf = MLPClassifier(hidden_layer_sizes=(self.c1,self.c2,self.c3), activation=self.activation, solver=self.solver, learning_rate=self.learning_rate)
        for i in range(100):

            loocv = LeaveOneOut()
            scores = cross_val_score(clf, self.dataWC, self.classAttribute, cv=loocv, scoring='accuracy')
            accuracy.append(scores.mean())

            scores = cross_val_score(clf, self.dataWC, self.classAttribute, cv=loocv, scoring='precision')
            precision.append(scores.mean())

            scores = cross_val_score(clf, self.dataWC, self.classAttribute, cv=loocv, scoring='recall')
            recall.append(scores.mean())

            predictions = cross_val_predict(clf, self.dataWC, self.classAttribute, cv=loocv)
            tn, fp, fn, tp = confusion_matrix(self.classAttribute, predictions).ravel()
            ListTN.append(tn)
            ListFP.append(fp)
            ListFN.append(fn)
            ListTP.append(tp)

        self.performaceObject.ListAccuracy=accuracy
        self.performaceObject.ListRecall=recall
        self.performaceObject.ListPrecision=precision

        self.performaceObject.ListTN=ListTN
        self.performaceObject.ListFP=ListFP
        self.performaceObject.ListFN=ListFN
        self.performaceObject.ListTP=ListTP

        #hacemos la instancia al performanceScoreValues
        desc = "%s-%s-%s (%d-%d-%d)" % (self.activation, self.solver, self.learning_rate, self.c1, self.c2, self.c3)
        self.performanceValues = performanceScoreValues.performanceScoreValues("MLPClassifier",desc, 'LOU', self.performaceObject)
