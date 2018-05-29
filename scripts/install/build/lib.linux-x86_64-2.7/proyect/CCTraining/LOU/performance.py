'''
clase que representa la lista de performance que posee un entrenamiento en particular...
'''
from sklearn.metrics import accuracy_score, cohen_kappa_score, f1_score, precision_score, recall_score, log_loss, hamming_loss
class performanceTraining(object):

    def __init__(self):

        self.ListAccuracy = []
        self.ListRecall = []
        self.ListPrecision = []
        self.ListHamming = []
        self.ListF = []
        self.ListCohen = []

    #metodo que permite calcular cada una de las performance y agregarla a la lista...
    def calculatePerformance(self, classTest, predictionValue):
        self.ListAccuracy.append(accuracy_score(classTest, predictionValue))
        self.ListRecall.append(recall_score(classTest, predictionValue, average='weighted'))
        self.ListPrecision.append(precision_score(classTest, predictionValue))
        self.ListHamming.append(hamming_loss(classTest, predictionValue))
        self.ListF.append(f1_score(classTest, predictionValue))
        self.ListCohen.append(cohen_kappa_score(classTest, predictionValue))
