'''
clase con la responsabilidad de evaluar los modelos seleccionados para el grupo A y
compararlos con los del resto de los grupos, genera un archivo resumen por cada entrenamiento de grupo diferente...
'''
import pandas as pd
import numpy as np

from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.svm import NuSVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from proyect.CCProcesFile import document

class evaluacionCruzada(object):

    def __init__(self, pathInput, pathOutput):

        self.pathOutput = pathOutput
        self.pathInput = pathInput
        self.listGroup = ['1', '2', '3', '4', '5', '6', '7']
        nameFile = self.pathInput+"8/8.csv"
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
    def createPredictForGroup(self, group):

        #formamos el path...
        nameFile = self.pathInput+group+"/"+group+".csv"
        dataSet, classList = self.getValuesInDataSet(nameFile)

        listDesc = ['relu-sgd-invscaling (15-5-5)','750- AdaBoostClassifier', 'gini - 10', 'gini - 20', 'gini - 50', 'gini - 100', 'gini - 150', 'entropy - 10', 'entropy - 20', 'entropy - 50']
        listAlgth = ['MLPClassifier','SAMME.R','RandomForestClassifier','RandomForestClassifier','RandomForestClassifier','RandomForestClassifier','RandomForestClassifier','RandomForestClassifier','RandomForestClassifier','RandomForestClassifier']
        actualData = [0.9,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8]

        clf = []## NOTE: solo se trabajara con un maximo de 5 clasificadores...

        clf.append(MLPClassifier(hidden_layer_sizes=(15,5,5), activation='relu', solver='sgd', learning_rate='invscaling'))
        clf.append(AdaBoostClassifier(n_estimators=750, algorithm='SAMME.R'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=10, n_jobs=-1, criterion='gini'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=20, n_jobs=-1, criterion='gini'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=50, n_jobs=-1, criterion='gini'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=100, n_jobs=-1, criterion='gini'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=150, n_jobs=-1, criterion='gini'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=10, n_jobs=-1, criterion='entropy'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=20, n_jobs=-1, criterion='entropy'))
        clf.append(RandomForestClassifier(max_depth=2, random_state=0, n_estimators=50, n_jobs=-1, criterion='entropy'))

        matrixResult = []

        for i in range (len(clf)):
            clf[i] = clf[i].fit(self.dataSetTraining, self.classLearning)
            predict = clf[i].predict(dataSet)
            scoredata = clf[i].score(dataSet, classList)
            row = [listAlgth[i], listDesc[i], actualData[i], scoredata]
            matrixResult.append(row)

        #exportamos el resultado...
        nameDoc = "exportResultPredict_%s.csv" % group
        document.document(nameDoc, self.pathOutput).createExportFileWithPandas(matrixResult, ["algorithm", "desc", "actualScore", "new score"])

    #metodo que permite hacer el procesamiento de todos los grupos...
    def processGroup(self):

        for element in self.listGroup:
            print "Process group: ", element
            self.createPredictForGroup(element)
