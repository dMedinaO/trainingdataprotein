'''
clase que permite poder representar la performance obtenida por algun algoritmo
'''
from sklearn.model_selection import cross_validate, cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.metrics import accuracy_score, cohen_kappa_score, f1_score, precision_score, recall_score
import numpy as np

class performanceAlgoritmo(object):

    def __init__(self, algorithm, description, validation):

        self.ListScore = ['accuracy', 'recall', 'precision', 'neg_log_loss', 'f1']
        self.ftwo_scorer = make_scorer(fbeta_score, beta=2)

        self.algorithm = algorithm
        self.description = description
        self.validation = validation

    #funcion que permite estimar las metricas de control para el modelo generado... con validacion CV=10
    def estimatedMetricsPerformance(self, clf, dataInput, dataClass, valueCV):

        self.scoreData = []
        for element in self.ListScore:
            scores = cross_val_score(clf, dataInput, dataClass, cv=valueCV, scoring=element)
            meanScore = np.mean(scores)
            self.scoreData.append(meanScore)
        #aplicamos el scrore fbeta...
        scores = cross_val_score(clf, dataInput, dataClass, cv=valueCV, scoring=self.ftwo_scorer)
        meanScore = np.mean(scores)
        self.scoreData.append(meanScore)

        #generamos la matriz de confusion...
        predictions = cross_val_predict(clf, dataInput, dataClass, cv=valueCV)
        tn, fp, fn, tp = confusion_matrix(dataClass, predictions).ravel()
        #siempre con respecto a la clase de interes...
        self.scoreData.append(tn)
        self.scoreData.append(fp)
        self.scoreData.append(fn)
        self.scoreData.append(tp)
