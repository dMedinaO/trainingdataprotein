'''
clase que permite poder graficar el coeficiente de siluetas para un grupo, crea la imagen y la exporta al directorio
que recibe...
'''

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class groupGraphicSil(object):

    def __init__(self, dataSet, labels, namePath, numberCluster, centers):

        self.dataSet = dataSet
        self.labels = labels
        self.namePath= namePath
        self.numberCluster = numberCluster
        self.centers = centers

    def createGraphic(self):

        # Create a subplot with 1 row and 1 columns
        fig, ax1  = plt.subplots(1, 1)
        fig.set_size_inches(18, 7)
        ax1.set_xlim([-0.1, 1])
        ax1.set_ylim([0, len(self.dataSet) + (self.numberCluster + 1) * 10])
        silhouette_avg = silhouette_score(self.dataSet, self.labels)
        sample_silhouette_values = silhouette_samples(self.dataSet, self.labels)

        y_lower = 10

        for i in range(self.numberCluster):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[self.labels == i]
            ith_cluster_silhouette_values.sort()
            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.spectral(float(i) / self.numberCluster)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                      "with n_clusters = %d" % self.numberCluster),
                     fontsize=14, fontweight='bold')
        nameFile = self.namePath+"silhouetteGraphic.png"
        plt.savefig(nameFile)
