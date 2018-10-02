'''
clase con la responsabilidad de generar la ejecución de los mejores modelos obtenidos en la ejecucion full data y obtener
todos los posibles resultados para un clasificador
'''

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import NuSVC, SVC

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
        self.ListScore = ['accuracy', 'recall', 'precision', 'neg_log_loss', 'f1']
        self.ftwo_scorer = make_scorer(fbeta_score, beta=2)
        self.classAttribute = []
        self.dataWC = []
        self.prepareDataSet()

    #metodo que permite procesar los modelos, crea los clf y genera los resultados
    def processModels(self):

        # param_name = "alpha"
        # param_range = np.logspace(-6,1,5)
        # clf = NuSVC(kernel='linear', degree=3, gamma=10, probability=True)
        # self.createModel(clf, "NuSVC_linear/", 0.2, param_name, param_range, 'gamma', 'Validation curve with NuSVC', 0)

        param_name = "n_estimators"
        param_range = [10,20,50,100,150,200,250,500,750,1000,1500]

        clf= AdaBoostClassifier(n_estimators=20, algorithm='SAMME')
        self.createModel(clf, "AdaBoostClassifier_250/", 0.2, param_name, param_range, 'n_estimators', 'Validation curve with RandomForestClassifier', 1)

        # clf= KNeighborsClassifier(n_neighbors=3,metric='minkowski',algorithm='auto',weights='uniform', n_jobs=-1)
        # self.createModel(clf, "KNN_min_auto_3_uni/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 1)
        # #
        # clf= KNeighborsClassifier(n_neighbors=3,metric='euclidean',algorithm='auto',weights='uniform', n_jobs=-1)
        # self.createModel(clf, "KNN_euc_auto_3_uni/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 1)
        # #
        # clf= KNeighborsClassifier(n_neighbors=3,metric='minkowski',algorithm='auto',weights='distance', n_jobs=-1)
        # self.createModel(clf, "KNN_min_auto_3_dist/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 1)
        # #
        # clf= KNeighborsClassifier(n_neighbors=3,metric='euclidean',algorithm='auto',weights='distance', n_jobs=-1)
        # self.createModel(clf, "KNN_euc_auto_3_dist/", 0.2, param_name, param_range, 'n_neighbors', 'Validation curve with KNN', 1)

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
    def createModel(self, clf, pathName, size, param_name, param_range, xlabel, title, index):

        path = self.createPath(pathName)
        clfNull = clf
        clf = clf.fit(self.dataWC, self.classAttribute)

        print "Process summary score"
        self.crossValidateModel(clf, path)

        print "Process confusion matrix"
        nameMatrix = "%sConfusionMatrix.svg" % path
        self.createConfusionMatrix(self.dataWC, self.classAttribute, clf, nameMatrix)
        try:
            print "Process Precision and recall curve"
            fig1 = "%sprecision_recall_curve.svg" % path
            fig2 = "%sprecision_recall_curve_for_class.svg" % path
            self.plot_precision_and_recall_curve(clfNull, fig1, fig2)
        except:
            print "Not precision_recall_curve"
            pass

        try:
            print "Process ROC curve"
            namePicture = "%sroc_curve.svg" % path
            self.createCurveRoc(clfNull, namePicture)
        except:
            print "Not roc_curve"
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
            scores = cross_val_score(clf, self.dataWC, self.classAttribute, cv=5, scoring=element)
            meanScore = np.mean(scores)
            scoreData.append(meanScore)
        #aplicamos el scrore fbeta...
        scores = cross_val_score(clf, self.dataWC, self.classAttribute, cv=5, scoring=self.ftwo_scorer)
        meanScore = np.mean(scores)
        scoreData.append(meanScore)

        #exportamos la data...
        header = ["Metric", "Score"]
        matrixData = [['accuracy', scoreData[0]], ['recall', scoreData[1]], ['precision', scoreData[2]], ['neg_log_loss', scoreData[3]], ['f1', scoreData[4]]]
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

        self.predictions = cross_val_predict(clf, xTrain, yTrain, cv=5)
        matrix = confusion_matrix(yTrain, self.predictions)

        np.set_printoptions(precision=2)

        # Plot non-normalized confusion matrix
        plt.figure()
        self.plot_confusion_matrix(matrix, classes=['Clinical','No clinical'], title='Confusion matrix, without normalization')
        plt.savefig(nameFig)

    #metodo que permite crear una curva roc con la data...
    def createCurveRoc(self, clf, nameFig):

        #recibimos la data y la transformamos en
        X = np.array(self.dataWC)
        y = np.array(self.transformInt(self.classAttribute))

        cv = StratifiedKFold(n_splits=5)
        classifier = clf
        tprs = []
        aucs = []
        mean_fpr = np.linspace(0, 1, 100)
        plt.figure(figsize=(20,10))
        i = 0
        for train, test in cv.split(X, y):
            probas_ = classifier.fit(X[train], y[train]).predict_proba(X[test])
            # Compute ROC curve and area the curve
            fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
            tprs.append(interp(mean_fpr, fpr, tpr))
            tprs[-1][0] = 0.0
            roc_auc = auc(fpr, tpr)
            aucs.append(roc_auc)
            plt.plot(fpr, tpr, lw=1, alpha=0.3,
                     label='ROC fold %d (AUC = %0.2f)' % (i, roc_auc))

            i += 1
        plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
                 label='Luck', alpha=.8)

        mean_tpr = np.mean(tprs, axis=0)
        mean_tpr[-1] = 1.0
        mean_auc = auc(mean_fpr, mean_tpr)
        std_auc = np.std(aucs)
        plt.plot(mean_fpr, mean_tpr, color='b',
                 label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
                 lw=2, alpha=.8)

        std_tpr = np.std(tprs, axis=0)
        tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
        tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
        plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
                         label=r'$\pm$ 1 std. dev.')

        plt.xlim([-0.05, 1.05])
        plt.ylim([-0.05, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic example', fontsize=25)
        plt.legend(loc="lower right")
        plt.savefig(nameFig)

    #metodo que permite crear la curva de validacion
    def createCurveValidation(self, clf, nameFig, param_name, param_range, xlabel, title, option):

        X = np.array(self.dataWC)
        y = np.array(self.transformInt(self.classAttribute))

        train_scores, test_scores = validation_curve(clf, X, y, param_name=param_name, param_range=param_range,cv=5, scoring="accuracy", n_jobs=1)
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
        cv = ShuffleSplit(n_splits=100, test_size=size, random_state=0)
        self.plot_learning_curve(clf, title, X, y, cv, ylim=(0.01, 1.01), n_jobs=4)

        plt.savefig(nameFig)

    #metodo que permite aplicar las diversas curvas de precision vs recall
    def plot_precision_and_recall_curve(self, classifier, fig1, fig2):

        X = np.array(self.dataWC)
        y = np.array(self.transformInt(self.classAttribute))

        # Limit to the two first classes, and split into training and test
        X_train, X_test, y_train, y_test = train_test_split(X[y < 2], y[y < 2],test_size=.5)

        # Create a simple classifier
        classifier.fit(X_train, y_train)
        y_score = classifier.decision_function(X_test)
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
