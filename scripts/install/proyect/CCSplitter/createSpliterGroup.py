'''
clase con la responsabilidad de recibir un set de datos y evaluar todas las posibles opciones de generar una subdivision por
medio de tecnicas de clustering que permitan indicar el numero de cluster a evaluar...
'''

from sklearn.cluster import KMeans, AgglomerativeClustering, AffinityPropagation, MeanShift, estimate_bandwidth
from sklearn.cluster import DBSCAN, Birch
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from proyect.CCProcesFile import document
from proyect.CCSplitter import modelGroup

class splitterGroup(object):

    def __init__(self, nameDataSet):

        self.nameDataSet = nameDataSet
        self.processDataSet()
        self.ListModel = []

    #tratamos el set de datos para hacerlo manejable...
    def processDataSet(self):

        self.dataSet = document.document(self.nameDataSet, 'sadsa').readMatrix()
        self.dataSet = self.dataSet[1:]

        #transformamos la data a float...
        for i in range (len(self.dataSet)):
            for j in range (len(self.dataSet[i])):
                self.dataSet[i][j] = float(self.dataSet[i][j])

    #metodo que permite aplicar k-means al set de datos...
    def applyKMeans(self):

        for algorithm in ['auto', 'full', 'elkan']:
            model = KMeans(n_clusters=2, random_state=1, algorithm=algorithm).fit(self.dataSet)
            self.ListModel.append(modelGroup.modelGroup(model, 'KMeans', algorithm))

    #metodo que permite aplicar bisrch clustering
    def aplicateBirch(self):

        model = Birch(threshold=0.2, branching_factor=50, n_clusters=2, compute_labels=True, copy=True).fit(self.dataSet)
        self.ListModel.append(modelGroup.modelGroup(model, 'Birch', 'Birch'))

    #metodo que permite aplicar cluster jerarquico
    def aplicateAlgomerativeClustering(self):

        for linkage in ['ward', 'complete', 'average']:
            for affinity in ['euclidean', 'l1', 'l2', 'manhattan', 'cosine', 'precomputed']:
                try:
                    model = AgglomerativeClustering(n_clusters=2, affinity=affinity, memory=None, connectivity=None, compute_full_tree='auto', linkage=linkage).fit(self.dataSet)
                    desc = "%s-%s" % (linkage, affinity)
                    self.ListModel.append(modelGroup.modelGroup(model, 'AgglomerativeClustering', desc))
                except:
                    pass
