'''
clase con la responsabilidad de generar distintas matrices de adyacencia asociadas a la data de los ejemplos,
recibe la data normalizada y genera los calculos, emplea distintas metricas de distancia para cada sujeto y genera
diversas matrices asociadas a cada metrica...
'''

from scipy.spatial import distance
import scipy as sp
import pandas as pd

from proyect.CCProcesFile import document

class distanceSamples(object):

    def __init__(self, matrixData, header, pathOutput):

        self.matrixData = matrixData
        self.header = header
        self.pathOutput = pathOutput
        self.df = pd.DataFrame(data=self.matrixData)
        self.covmx = self.df.cov()
        self.invcovmx = sp.linalg.inv(self.covmx)
        self.header = header

    #metodo que permite calcular la distancia entre diferentes sujetos, con respecto a distintas metricas...
    def estimatedDistance(self, sample1, sample2, metric):

        if metric==0:#euclidean
            return distance.euclidean(sample1, sample2)
        elif metric == 1:#cosine
            return distance.cosine(sample1, sample2)
        elif metric == 2:#mahalanobis
            return distance.mahalanobis(sample1, sample2, self.invcovmx)
        elif metric == 3:#canberra
            return distance.canberra(sample1, sample2)
        elif metric == 4:#minkowski orden 1
            return distance.minkowski(sample1, sample2, 1)
        elif metric == 5:#minkowski orden 2
            return distance.minkowski(sample1, sample2, 2)
        else:#minkowski orden 3
            return distance.minkowski(sample1, sample2, 3)


    #metodo que permite generar la matriz de adjacencia...
    def createAdjacenceMatrix(self):

        listMetrics = ['euclidean', 'cosine', 'mahalanobis', 'canberra', 'minkowski 1', 'minkowski 2', 'minkowski 3']

        for i in range(len(listMetrics)):
            print "Process distance matrix for: ", listMetrics[i]

            matrixAdj = []
            for element in self.matrixData:
                rowDistance = []
                for element2 in self.matrixData:
                    rowDistance.append(self.estimatedDistance(element, element2, i))
                matrixAdj.append(rowDistance)

            #exportamos el documento...
            nameFile = self.pathOutput+listMetrics[i]+".csv"
            df = pd.DataFrame(matrixAdj)
            df.to_csv(nameFile, sep=',',header=self.header, index=False)
