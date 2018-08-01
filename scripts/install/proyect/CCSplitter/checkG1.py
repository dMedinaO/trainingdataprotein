'''
clase con la responsabilidad de evaluar los modelos seleccionados para el grupo A y
compararlos con los del resto de los grupos, genera un archivo resumen por cada entrenamiento de grupo diferente...
'''
import pandas as pd
import numpy as np

from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from proyect.CCProcesFile import document

class evaluacionCruzada(object):

    def __init__(self, pathInput, pathOutput):

        self.pathOutput = pathOutput
        self.pathInput = pathInput
        self.listGroup = ['2', '3', '4', '5', '6', '7', '8']
        nameFile = self.pathInput+"1/1.csv"
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

        listDesc = ['tanh-lbfgs-constant (5-10-15)', 'tanh-lbfgs-adaptive (15-10-5)', 'relu-lbfgs-adaptive (10-5-15)', 'relu-sgd-invscaling (15-5-5)']
        listAlgth = 'MLPClassifier'
        actualData = 0.682926829268

        clf = []## NOTE: solo se trabajara con un maximo de 10 clasificadores...
        clf.append(MLPClassifier(hidden_layer_sizes=(5,10,15), activation='tanh', solver='lbfgs', learning_rate='constant'))#logistic-sgd-invscaling (10-10-15)
        clf.append(MLPClassifier(hidden_layer_sizes=(15,10,5), activation='tanh', solver='lbfgs', learning_rate='adaptive'))#identity-sgd-invscaling (5-5-10)
        clf.append(MLPClassifier(hidden_layer_sizes=(10,5,15), activation='relu', solver='lbfgs', learning_rate='adaptive'))#logistic-sgd-invscaling (5-15-15)
        clf.append(MLPClassifier(hidden_layer_sizes=(15,5,5), activation='relu', solver='sgd', learning_rate='invscaling'))#tanh-sgd-invscaling (10-5-15)

        matrixResult = []

        for i in range (len(clf)):
            clf[i] = clf[i].fit(self.dataSetTraining, self.classLearning)
            predict = clf[i].predict(dataSet)
            scoredata = clf[i].score(dataSet, classList)
            row = [listAlgth, listDesc[i], actualData, scoredata]
            matrixResult.append(row)

        #exportamos el resultado...
        nameDoc = "exportResultPredict_%s.csv" % group
        document.document(nameDoc, self.pathOutput).createExportFileWithPandas(matrixResult, ["algorithm", "desc", "actualScore", "new score"])

    #metodo que permite hacer el procesamiento de todos los grupos...
    def processGroup(self):

        for element in self.listGroup:
            print "Process group: ", element
            self.createPredictForGroup(element)
