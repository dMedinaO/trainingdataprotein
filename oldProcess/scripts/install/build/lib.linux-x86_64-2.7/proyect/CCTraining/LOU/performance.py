'''
clase que representa la lista de performance que posee un entrenamiento en particular...
'''
from sklearn.metrics import accuracy_score, precision_score, recall_score
class performanceTraining(object):

    def __init__(self):

        self.ListAccuracy = []
        self.ListRecall = []
        self.ListPrecision = []
        self.ListTN = []
        self.ListFP = []
        self.ListFN = []
        self.ListTP = []

    #metodo que permite calcular cada una de las performance y agregarla a la lista...
    def calculatePerformance(self, classTest, predictionValue):
        self.ListAccuracy.append(accuracy_score(classTest, predictionValue))
        self.ListRecall.append(recall_score(classTest, predictionValue, average='weighted'))
        self.ListPrecision.append(precision_score(classTest, predictionValue))
