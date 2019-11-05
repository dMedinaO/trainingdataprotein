'''
clase con la responsabilidad de evaluar los modelos seleccionados para el grupo A y
compararlos con los del resto de los grupos, genera un archivo resumen por cada entrenamiento de grupo diferente...
'''
import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import NuSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import LeaveOneOut

from sklearn.svm import NuSVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import NuSVC, SVC
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from proyect.CCProcesFile import document

class evaluacionCruzada(object):

    def __init__(self, pathInput, pathOutput):

        self.pathOutput = pathOutput
        self.pathInput = pathInput
        self.ListName = ['group2_Full.csv','group1_Full.csv','group3_Full.csv','group4_Full.csv','group6_Full.csv','group7_Full.csv']
        self.listGroup = ['grupo2','grupo1','grupo3','grupo4','grupo6','grupo7']
        nameFile = self.pathInput+"grupo3/group3_Full.csv"
        self.dataSetTraining, self.classLearning = self.getValuesInDataSet(nameFile)

    #metodo que permite poder obtener las clases y la data...
    def getValuesInDataSet(self, group):

        dataSet = document.document(group, '').readMatrix()
        dataSet = dataSet[1:]
        dataSet = self.transformData(dataSet)

        classList = []
        dataValues = []

        for element in dataSet:
            dataValues.append(element[:-1])
            classList.append(element[-1])

        return dataValues, classList

    #metodo que permite transformar la data en enteros o floats...
    def transformData(self, dataSet):

        for i in range (len(dataSet)):
            for j in range (len(dataSet[i])):
                if j < len(dataSet[i])-1:
                    dataSet[i][j] = float(dataSet[i][j])
                else:
                    dataSet[i][j] = int(dataSet[i][j])
        return dataSet

    #metodo que permite hacer la prediccion por grupo...
    def createPredictForGroup(self, group, name):

        #formamos el path...
        nameFile = self.pathInput+group+"/"+name
        dataSet, classList = self.getValuesInDataSet(nameFile)

        #listDesc = ['logistic-adam-invscaling (10-5-10)', 'GaussianNB', 'BernoulliNB', 'linear', 'sigmoid', 'gini - 10', 'gini - 20', 'gini - 200']
        #listAlgth = ['MLPClassifier', 'Naive Bayes','Naive Bayes', 'SVC', 'SVC', 'RandomForestClassifier','RandomForestClassifier','RandomForestClassifier']
        #actualData = [0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75]

        listDesc = ['identity-lbfgs-constant (10-15-15)']
        listAlgth = ['MLP']
        #actualData = 0.79
        actualData = 0.6

        clf = []## NOTE: solo se trabajara con un maximo de 10 clasificadores...
        #clf.append(BernoulliNB())
        #clf.append(GaussianNB())
        clf.append(MLPClassifier(hidden_layer_sizes=(15,10,10), activation='identity', solver='lbfgs', learning_rate='constant'))
        #clf.append(KNeighborsClassifier(n_neighbors=2,metric='minkowski',algorithm='auto',weights='uniform', n_jobs=-1))
        #clf.append(KNeighborsClassifier(n_neighbors=2,metric='euclidean',algorithm='auto',weights='uniform', n_jobs=-1))
        #clf.append(KNeighborsClassifier(n_neighbors=2,metric='minkowski',algorithm='ball_tree',weights='uniform', n_jobs=-1))
        #clf.append(KNeighborsClassifier(n_neighbors=2,metric='euclidean',algorithm='ball_tree',weights='uniform', n_jobs=-1))


        #clf.append(SVC(kernel='rbf', degree=3, gamma=10, probability=True))
        #clf.append(SVC(kernel='linear', degree=3, gamma=10, probability=True))
        #clf.append(SVC(kernel='sigmoid', degree=3, gamma=10, probability=True))

        #clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=10, n_jobs=-1, criterion='gini'))
        #clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=100, n_jobs=-1, criterion='gini'))
        #clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=150, n_jobs=-1, criterion='gini'))

        matrixResult = []

        for i in range (len(clf)):
            clf[i] = clf[i].fit(self.dataSetTraining, self.classLearning)
            predict = clf[i].predict(dataSet)
            scoredata = clf[i].score(dataSet, classList)
            #row = [listAlgth[i], listDesc, actualData, scoredata]
            row = [listAlgth[i], listDesc[i], actualData, scoredata]
            matrixResult.append(row)

        #exportamos el resultado...
        nameDoc = "exportResultPredict_%s.csv" % group
        document.document(nameDoc, self.pathOutput).createExportFileWithPandas(matrixResult, ["algorithm", "desc", "actualScore", "new score"])

    #metodo que permite hacer el procesamiento de todos los grupos...
    def processGroup(self):

        for i in range (len(self.listGroup)):
            print "Process group: ", self.listGroup[i]
            self.createPredictForGroup(self.listGroup[i], self.ListName[i])
