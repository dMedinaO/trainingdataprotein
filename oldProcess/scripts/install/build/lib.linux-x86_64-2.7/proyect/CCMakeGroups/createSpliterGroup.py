'''
clase con la responsabilidad de recibir un set de datos y evaluar todas las posibles opciones de generar una subdivision por
medio de tecnicas de clustering que permitan indicar el numero de cluster a evaluar...
'''

from sklearn.cluster import KMeans, AgglomerativeClustering, AffinityPropagation, MeanShift, estimate_bandwidth
from sklearn.cluster import DBSCAN, Birch
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from proyect.CCProcesFile import document

class splitterGroup(object):

    def __init__(self, nameDataSet):

        self.nameDataSet = nameDataSet
        self.processDataSet()

    #tratamos el set de datos para hacerlo manejable...
    def processDataSet(self):

        self.dataSet = document.document(self.nameDataSet, 'sadsa').readMatrix()
        self.dataSet = self.dataSet[1:]

        #removemos las clases...
        for i in range (len(self.dataSet)):
            self.dataSet[i] = self.dataSet[i][:-1]

        #transformamos la data a float...
        for i in range (len(self.dataSet)):
            for j in range (len(self.dataSet[i])):
                self.dataSet[i][j] = float(self.dataSet[i][j])

    #metodo que permite aplicar k-means al set de datos...
    def applyKMeans(self):

        model = KMeans(n_clusters=2, random_state=1).fit(self.dataSet)
        print model.labels_
