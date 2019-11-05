'''
clase que tiene la responsabilidad de entrenar un knn con diversas variables mediante el uso de
la tecnica leave one out...
'''

from proyect.CCTraining.LOU import performance
from proyect.CCTraining.LOU import performanceScoreValues
from sklearn.svm import NuSVC
from sklearn.model_selection import LeaveOneOut, cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix
import numpy as np

class nuSVC(object):

    def __init__(self, matrix, kernel):

        self.matrix = matrix
        self.kernel = kernel
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

        accuracy = []
        precision = []
        recall = []
        ListTN = []
        ListFP = []
        ListFN = []
        ListTP = []

        clf = NuSVC(kernel=self.kernel, degree=3, gamma=10, probability=True)
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
        desc = "kernel: %s" % self.kernel
        self.performanceValues = performanceScoreValues.performanceScoreValues("NuSVC",desc, 'LOU', self.performaceObject)
