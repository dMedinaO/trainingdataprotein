'''
clase con la responsabilidad de aplicar el algoritmo de random forest con el fin de ir evaluando cada una de las features existentes
y determinar la importancia que estas poseen para la generacion del clasificador, genera un conjunto de resultados que son de interes
a la hora de evaluar cada uno de los componentes...

Recibe como entrada el set de datos normalizado y el path donde se dispondra de los resultados...
'''
from sklearn.ensemble import RandomForestClassifier
from proyect.CCProcesFile import document
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve

import itertools

import subprocess
import numpy as np
import pandas as pd
from  matplotlib import pyplot

class featureImportance(object):

    def __init__(self, dataSet, pathOutput):

        self.dataSet = dataSet
        self.pathOutput = pathOutput

        #criterion for config exec algorithm
        self.criterionList = ['gini', 'entropy']
        self.n_estimatorsList = [10, 20, 50, 100, 150, 200, 250, 500, 750, 1000, 1500]

    #metodo que permite hacer la lectura de la matriz normalizada...
    def getDataSet(self):

        doc = document.document(self.dataSet, self.pathOutput)
        self.data = doc.readMatrix()
        self.header = self.data[0]
        self.data = self.data[1:]
        self.header = self.header[:-1]
        print self.header
    #metodo que recibe una lista y la transforma a flotante...
    def transformFloat(self, listData):

        for i in range(len(listData)):
            listData[i] = float(listData[i])
        return listData

    def transformInt(self, listData):
        for i in range(len(listData)):
            listData[i] = float(listData[i])
        return listData

    #metodo que permite separar los atributos, dejando en un array las clases y en otro los valores...
    def getClassAndAttributes(self):

        self.dataWC = []
        self.classAttribute = []

        for element in self.data:
            self.dataWC.append(self.transformFloat(element[:-1]))
            self.classAttribute.append(element[-1])

    #metodo que permite generar el archivo de descripcion y de resultados para cada procedimiento...
    def createDataSummary(self, description, scores, nameFile):

        fileData = open(nameFile, 'w')
        description = "Description: %s" % description
        fileData.write(description+"\n")
        meandData = "Mean: %f" % scores.mean()
        stdData = "Standard Deviation: %f" % scores.std()
        fileData.write(meandData+"\n")
        fileData.write(stdData+"\n")
        fileData.close()

    def plot_confusion_matrix(self, cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Oranges):

        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                     horizontalalignment="center",
                     color="black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    #creamos el directorio para cada evaluacion...
    def createDir(self, namePath):

        command = "mkdir -p %s" % namePath
        subprocess.call(command, shell=True)

    #metodo que permite generar la matriz de confusion...
    def createConfusionMatrix(self, xTrain, yTrain, random_forest, nameFig):

        self.predictions = cross_val_predict(random_forest, xTrain, yTrain, cv=10)
        matrix = confusion_matrix(yTrain, self.predictions)

        np.set_printoptions(precision=2)

        # Plot non-normalized confusion matrix
        plt.figure()
        self.plot_confusion_matrix(matrix, classes=['Clinical','No clinical'],
                              title='Confusion matrix, without normalization')
        plt.savefig(nameFig)

    def plot_precision_and_recall(self, random_forest, name):
        y_scores = random_forest.predict_proba(self.dataWC)
        y_scores = y_scores[:,1]
        self.y_scores = y_scores

        precision, recall, threshold = precision_recall_curve(self.transformInt(self.classAttribute), y_scores)
        plt.figure()
        plt.plot(threshold, precision[:-1], "r-", label="precision", linewidth=5)
        plt.plot(threshold, recall[:-1], "b", label="recall", linewidth=5)
        plt.xlabel("threshold", fontsize=19)
        plt.legend(loc="upper right", fontsize=19)
        plt.ylim([0, 1])
        plt.savefig(name)

    #metodo para evaluar la curva roc...
    def evaluatedError(self, nameFig, label=None):

        false_positive_rate, true_positive_rate, thresholds = roc_curve(self.classAttribute, self.y_scores)
        plt.figure()
        plt.plot(false_positive_rate, true_positive_rate, linewidth=2, label=label)
        plt.plot([0, 1], [0, 1], 'r', linewidth=4)
        plt.axis([0, 1, 0, 1])
        plt.xlabel('False Positive Rate (FPR)', fontsize=16)
        plt.ylabel('True Positive Rate (TPR)', fontsize=16)
        plt.savefig(nameFig)

    #metodo que permite aplicar el algoritmo y hacer las evaluaciones correspondientes...
    def checkFeatures(self):

        for criterion in self.criterionList:
            for n_estimators in self.n_estimatorsList:

                print "RandomForest, criterion: %s n_estimators: %d" % (criterion, n_estimators)
                random_forest = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=n_estimators, n_jobs=-1, criterion=criterion)
                random_forest = random_forest.fit(self.dataWC, self.classAttribute)
                scores = cross_val_score(random_forest, self.dataWC, self.classAttribute, cv=10, scoring='accuracy')
                print("Scores:", scores)
                print("Mean:", scores.mean())
                print("Standard Deviation:", scores.std())
                importances = pd.DataFrame({'feature':self.header,'importance':np.round(random_forest.feature_importances_,3)})
                importances = importances.sort_values('importance',ascending=False).set_index('feature')

                #create path...
                namePath = "%s%s_%d/" % (self.pathOutput, criterion, n_estimators)
                self.createDir(namePath)

                #create description...
                desc = "%s, %d"  % (criterion, n_estimators)
                nameFileExport = "%sDescriptionFile.txt" % namePath
                self.createDataSummary(desc, scores, nameFileExport)

                #export el pandas y el plot...
                nameCSV = "%sImportances.csv" % namePath
                importances.to_csv(nameCSV)
                importances.plot.bar()
                namePicture = "%sImportances.svg" % namePath
                pyplot.savefig(namePicture)

                #process confusion matrix
                nameMatrix = "%sConfusionMatrix.svg" % namePath
                self.createConfusionMatrix(self.dataWC, self.classAttribute, random_forest, nameMatrix)
                namePicture = "%sprecision_recall_curve.svg" % namePath
                self.plot_precision_and_recall(random_forest, namePicture)
                namePicture = "%sroc_curve.svg" % namePath
                self.evaluatedError(namePicture)
                
