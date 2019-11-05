'''
clase con la responsabilidad de generar la ejecución de los mejores modelos obtenidos en la ejecucion full data y obtener
todos los posibles resultados para un clasificador
'''

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import NuSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import LeaveOneOut

from sklearn.svm import NuSVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.ensemble import RandomForestClassifier

from scipy import interp
from itertools import cycle
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import validation_curve
from sklearn.model_selection import learning_curve
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier

from proyect.CCProcesFile import document
import matplotlib.pyplot as plt
import itertools

import numpy as np
import subprocess

class createBestModels(object):

    def __init__(self, dataSet, pathOutput):

        self.matrix = dataSet
        self.pathOutput = pathOutput
        self.ListScore = ['accuracy', 'recall', 'precision']
        self.ftwo_scorer = make_scorer(fbeta_score, beta=2)
        self.classAttribute = []
        self.dataWC = []
        self.prepareDataSet()

    #metodo que permite procesar los modelos, crea los clf y genera los resultados
    def processModels(self):

        param_name = "n_neighbors"
        param_range = [1,2,3,4,5,6]

        clf= KNeighborsClassifier(n_neighbors=4,metric='minkowski',algorithm='auto',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_min_auto/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 1,0)

        clf= KNeighborsClassifier(n_neighbors=4,metric='euclidean',algorithm='auto',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_euc_auto/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 1,0)

        clf= KNeighborsClassifier(n_neighbors=4,metric='minkowski',algorithm='ball_tree',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_min_ball/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 0,0)

        clf= KNeighborsClassifier(n_neighbors=4,metric='euclidean',algorithm='ball_tree',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_euc_ball/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 0,0)

        clf= KNeighborsClassifier(n_neighbors=4,metric='minkowski',algorithm='kd_tree',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_min_kd/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 0,0)

        clf= KNeighborsClassifier(n_neighbors=4,metric='minkowski',algorithm='kd_tree',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_euc_kd/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 0,0)

        clf= KNeighborsClassifier(n_neighbors=4,metric='euclidean',algorithm='brute',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_min_brute/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 0,0)

        clf= KNeighborsClassifier(n_neighbors=4,metric='minkowski',algorithm='brute',weights='uniform', n_jobs=-1)
        self.createModel(clf, "KNN_euc_brute/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 0,0)


    #metodo que permite crear un directorio...
    def createPath(self, namePath):

        namePath = self.pathOutput+namePath
        command = "mkdir -p %s" % namePath
        subprocess.call(command, shell=True)

        return namePath

    #metodo que permite hacer la lectura y la preparacion del set de datos...
    def prepareDataSet(self):

        for element in self.matrix:
            self.dataWC.append(element[:-1])
            self.classAttribute.append(element[-1])

    #crear el modelo para gradientes...
    def createModel(self, clf, pathName, size, param_name, param_range, xlabel, title, index, value):

        path = self.createPath(pathName)
        clfNull = clf
        clf = clf.fit(self.dataWC, self.classAttribute)

        print "Process summary score"
        self.crossValidateModel(clf, path)

        try:
            print "Process confusion matrix"
            nameMatrix = "%sConfusionMatrix.svg" % path
            self.createConfusionMatrix(self.dataWC, self.classAttribute, clf, nameMatrix)
        except:
            pass

        try:
            print "Process validation curve"
            namePicture = "%svalidation_curve.svg" % path
            self.createCurveValidation(clfNull, namePicture, param_name, param_range, xlabel, title, index)
        except:
            print "Not validation_curve"
            pass
        try:
            print "Process learning curve"
            namePicture = "%slearning_curve.svg" % path
            self.createLearningCurve(clfNull, namePicture, "Learning Curve For GradientBoostingClassifier", size)
        except:
            print "It is not possible create learning curve"
            pass

    def transformInt(self, listData):
        for i in range(len(listData)):
            listData[i] = int(listData[i])
        return listData

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

    #generamos la validacion del modelo...
    def crossValidateModel(self, clf, path):

        scoreData = []
        for element in self.ListScore:
            loocv = LeaveOneOut()
            scores = cross_val_score(clf, self.dataWC, self.classAttribute, cv=loocv, scoring=element)
            scoreData.append(scores.mean())

        #exportamos la data...
        header = ["Metric", "Score"]
        matrixData = [['accuracy', scoreData[0]], ['recall', scoreData[1]], ['precision', scoreData[2]]]
        document.document("summaryScore.csv", path).createExportFileWithPandas(matrixData, header)

    #desarrollo del plot de la matriz de confusion...
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

    #metodo que permite generar la matriz de confusion...
    def createConfusionMatrix(self, xTrain, yTrain, clf, nameFig):

        loocv = LeaveOneOut()
        self.predictions = cross_val_predict(clf, xTrain, yTrain, cv=loocv)
        matrix = confusion_matrix(yTrain, self.predictions)

        np.set_printoptions(precision=2)

        # Plot non-normalized confusion matrix
        plt.figure()
        self.plot_confusion_matrix(matrix, classes=['Clinical','No clinical'], title='Confusion matrix, without normalization')
        plt.savefig(nameFig)

    #metodo que permite crear la curva de validacion
    def createCurveValidation(self, clf, nameFig, param_name, param_range, xlabel, title, option):

        X = np.array(self.dataWC)
        y = np.array(self.transformInt(self.classAttribute))
        loocv = LeaveOneOut()
        train_scores, test_scores = validation_curve(clf, X, y, param_name=param_name, param_range=param_range,cv=loocv, scoring="accuracy", n_jobs=1)
        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)

        plt.figure()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel("Score")
        plt.ylim(0.0, 1.1)
        lw = 2
        #si grafica en forma de logaritmo o no...
        if option == 1:
            plt.plot(param_range, train_scores_mean, label="Training score",color="darkorange", lw=lw)
            plt.fill_between(param_range, train_scores_mean - train_scores_std,train_scores_mean + train_scores_std, alpha=0.2,color="darkorange", lw=lw)
            plt.plot(param_range, test_scores_mean, label="Cross-validation score",color="navy", lw=lw)
            plt.fill_between(param_range, test_scores_mean - test_scores_std,test_scores_mean + test_scores_std, alpha=0.2,color="navy", lw=lw)
        else:
            plt.semilogx(param_range, train_scores_mean, label="Training score",color="darkorange", lw=lw)
            plt.fill_between(param_range, train_scores_mean - train_scores_std,train_scores_mean + train_scores_std, alpha=0.2,color="darkorange", lw=lw)
            plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",color="navy", lw=lw)
            plt.fill_between(param_range, test_scores_mean - test_scores_std,test_scores_mean + test_scores_std, alpha=0.2,color="navy", lw=lw)
        plt.legend(loc="best")
        plt.savefig(nameFig)

    #metodo que permite crear la curva de aprendizaje...
    def plot_learning_curve(self, estimator, title, X, y, cv, ylim=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):
        plt.figure()
        plt.title(title)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.xlabel("Training examples")
        plt.ylabel("Score")
        train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)

        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)
        plt.grid()

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1, color="g")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")

        plt.legend(loc="best")
        return plt

    def createLearningCurve(self, clf, nameFig, title, size):

        X = np.array(self.dataWC)
        y = np.array(self.transformInt(self.classAttribute))

        # Cross validation with 100 iterations to get smoother mean test and train
        # score curves, each time with 20% data randomly selected as a validation set.
        cv = LeaveOneOut()
        self.plot_learning_curve(clf, title, X, y, cv, ylim=(0.01, 1.01), n_jobs=4)

        plt.savefig(nameFig)

    #metodo que permite aplicar las diversas curvas de precision vs recall
    def plot_precision_and_recall_curve(self, classifier, fig1, fig2, value):

        X = np.array(self.dataWC)
        y = np.array(self.transformInt(self.classAttribute))

        # Limit to the two first classes, and split into training and test
        X_train, X_test, y_train, y_test = train_test_split(X[y < 2], y[y < 2],test_size=.5)

        # Create a simple classifier
        classifier.fit(X_train, y_train)
        if value == 0:
            y_score = classifier.decision_function(X_test)
        else:
            y_score = classifier.decision_path(X_test)
        average_precision = average_precision_score(y_test, y_score)

        print('Average precision-recall score: {0:0.2f}'.format(average_precision))

        precision, recall, _ = precision_recall_curve(y_test, y_score)

        plt.figure()
        plt.step(recall, precision, color='b', alpha=0.2,where='post')
        plt.fill_between(recall, precision, step='post', alpha=0.2,color='b')

        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.ylim([0.0, 1.05])
        plt.xlim([0.0, 1.0])
        plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(average_precision))

        plt.savefig(fig1)
