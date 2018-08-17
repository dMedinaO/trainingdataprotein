'''
clase que tiene la responsabilidad de entrenar un knn con diversas variables mediante el uso de
la tecnica leave one out...
'''

from proyect.CCTraining.LOU import performance
from proyect.CCTraining.LOU import performanceScoreValues
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut, cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix

import numpy as np

class decisionTrees(object):

    def __init__(self, matrix, criterion, splitter):

        self.matrix = matrix
        self.criterion = criterion
        self.splitter = splitter
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

        clf = DecisionTreeClassifier(random_state=0, criterion=self.criterion, splitter=self.splitter)
        for i in range(10):
            print "Iteration ", i
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
        desc = "DecisionTreeClassifier %s %s" % (self.criterion, self.splitter)
        self.performanceValues = performanceScoreValues.performanceScoreValues(self.criterion,desc, 'LOU', self.performaceObject)
