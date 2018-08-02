'''
clase con la responsabilidad de evaluar los modelos seleccionados para el grupo A y
compararlos con los del resto de los grupos, genera un archivo resumen por cada entrenamiento de grupo diferente...
'''
import pandas as pd
import numpy as np

from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.svm import NuSVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from proyect.CCProcesFile import document

class evaluacionCruzada(object):

    def __init__(self, pathInput, pathOutput):

        self.pathOutput = pathOutput
        self.pathInput = pathInput
        self.listGroup = ['1', '2', '3', '4', '5', '6', '8']
        nameFile = self.pathInput+"7/7.csv"
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

        listDesc = ['tanh-sgd-invscaling (5-5-5)','tanh-sgd-invscaling (5-15-10)','relu-lbfgs-invscaling (10-10-15)','relu-adam-constant (5-15-5)','kernel: rbf','logistic-sgd-invscaling (15-10-5)','relu-lbfgs-adaptive (5-5-5)','relu-lbfgs-adaptive (10-15-10)','relu-sgd-invscaling (10-5-5)','relu-adam-invscaling (5-15-5)','relu-adam-adaptive (15-5-5)']
        listAlgth = ['MLPClassifier','MLPClassifier','MLPClassifier','MLPClassifier','NuSVC','MLPClassifier','MLPClassifier','MLPClassifier','MLPClassifier','MLPClassifier','MLPClassifier']
        actualData = [0.823529411765,0.764705882353,0.764705882353,0.764705882353,0.705882352941,0.705882352941,0.705882352941,0.705882352941,0.705882352941,0.705882352941,0.705882352941]
        clf = []## NOTE: solo se trabajara con un maximo de 5 clasificadores...

        clf.append(MLPClassifier(hidden_layer_sizes=(5,5,5), activation='tanh', solver='sgd', learning_rate='invscaling'))
        clf.append(MLPClassifier(hidden_layer_sizes=(5,15,10), activation='tanh', solver='sgd', learning_rate='invscaling'))
        clf.append(MLPClassifier(hidden_layer_sizes=(10,10,15), activation='relu', solver='lbfgs', learning_rate='invscaling'))
        clf.append(MLPClassifier(hidden_layer_sizes=(5,15,5), activation='relu', solver='adam', learning_rate='constant'))
        clf.append(NuSVC(kernel='rbf', degree=3, gamma=10, probability=True))#Kernel
        clf.append(MLPClassifier(hidden_layer_sizes=(15,10,5), activation='logistic', solver='sgd', learning_rate='invscaling'))
        clf.append(MLPClassifier(hidden_layer_sizes=(5,5,5), activation='relu', solver='lbfgs', learning_rate='adaptive'))
        clf.append(MLPClassifier(hidden_layer_sizes=(10,15,10), activation='relu', solver='lbfgs', learning_rate='adaptive'))
        clf.append(MLPClassifier(hidden_layer_sizes=(10,5,5), activation='relu', solver='sgd', learning_rate='invscaling'))
        clf.append(MLPClassifier(hidden_layer_sizes=(5,15,5), activation='relu', solver='adam', learning_rate='invscaling'))
        clf.append(MLPClassifier(hidden_layer_sizes=(15,5,5), activation='relu', solver='adam', learning_rate='adaptive'))

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
