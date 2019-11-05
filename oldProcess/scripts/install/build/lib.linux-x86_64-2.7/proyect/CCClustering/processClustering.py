'''
clase que tiene la responsabilidad de aplicar diversos tipos de clustering para un set de datos determinado
recibe como entrada un array con el set de datos a procesar
'''

from sklearn.cluster import KMeans, AgglomerativeClustering, AffinityPropagation, MeanShift, estimate_bandwidth
from sklearn.cluster import DBSCAN, Birch
from sklearn import metrics
from sklearn.metrics import pairwise_distances

class aplicateClustering(object):

    def __init__(self, dataSet):
        self.dataSet = dataSet

    #metodo que permite aplicar k-means, genera diversos set de datos con respecto a las divisiones que se emplean...
    def aplicateKMeans(self, numberK):

        self.model = KMeans(n_clusters=numberK, random_state=1).fit(self.dataSet)
        self.labels = self.model.labels_

    #metodo que permite aplicar bisrch clustering
    def aplicateBirch(self, numberK):

        self.model = Birch(threshold=0.2, branching_factor=50, n_clusters=numberK, compute_labels=True, copy=True).fit(self.dataSet)
        self.labels = self.model.labels_

    #metodo que permite aplicar cluster jerarquico
    def aplicateAlgomerativeClustering(self, linkage, affinity, numberK):

        #linkageList = ['ward', 'complete', 'average']
        #affinitList = ['euclidean', 'l1', 'l2', 'manhattan', 'cosine']
        try:
            self.model = AgglomerativeClustering(n_clusters=numberK, affinity=affinity, memory=None, connectivity=None, compute_full_tree='auto', linkage=linkage).fit(self.dataSet)
            self.labels = self.model.labels_
        except:
            pass

    #metodo que permite aplicar AffinityPropagation, con diversos parametros...
    def aplicateAffinityPropagation(self):

        self.model = AffinityPropagation().fit(self.dataSet)
        self.labels = self.model.labels_

    #metodo que permite aplicar DBSCAN
    def aplicateDBSCAN(self):

        self.model = DBSCAN(eps=0.3, min_samples=10).fit(self.dataSet)
        self.labels = self.model.labels_

    #metodo que permite aplicar MeanShift clustering...
    def aplicateMeanShift(self):

        bandwidth = estimate_bandwidth(self.dataSet, quantile=0.2)
        self.model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        self.model = self.model.fit(self.dataSet)
        self.labels = self.model.labels_
