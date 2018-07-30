'''
clase con la responsabilidad de evaluar los modelos seleccionados para el grupo A y
compararlos con los del resto de los grupos, genera un archivo resumen por cada entrenamiento de grupo diferente...
'''
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

class evaluacionCruzada(object):

    def __init__(self, pathOutput, pathInput):

        self.pathOutput = pathOutput
        self.pathInput = pathInput
        self.listGroup = ['B_Attribute', 'C_Attribute', 'F_Attribute', 'H_Attribute', 'M_Attribute', 'N_Attribute', 'O_Attribute', 'P_Attribute', 'R_Attribute', 'T_Attribute', 'U_Attribute', 'Z_Attribute']

    #metodo que permite hacer la lectura del set de datos a evaluar...
    def readDataSet(self, group):

        matrixData = pd.read_csv(group)
        return matrixData

    #metodo que permite hacer la prediccion por grupo...
    def createPredictForGroup(self, group):

        #formamos el path...
        nameFile = self.pathInput+group+"/normaliced/dataSetNormaliced.csv"
        matrixData = self.readDataSet(nameFile)

        #logistic-sgd-invscaling (10-10-15)
        mlp = MLPClassifier(hidden_layer_sizes=(10,10,15), activation='logistic', solver='sgd', learning_rate='invscaling')

    #metodo que permite hacer el procesamiento de todos los grupos...
    def processGroup(self):

        for element in self.listGroup:
            print "Process group: ", element
            self.createPredictForGroup(element)
