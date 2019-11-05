from proyect.CCProcessPDB import processPDB, calculateHBondsBestNetwork, parserDegreePhiPsi, calculateCovalentEnergy
from proyect.CCProcesFile import document
from proyect.CCProcessPDB import createGraph

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import collections
from networkx.drawing.nx_agraph import write_dot

from networkx.algorithms import approximation as approx
from networkx.algorithms import clique as clic
from networkx.algorithms import bipartite

class jobsGraph(object):

    def __init__(self, matrixData, pathOutput):

        self.matrixName = matrixData
        self.pathOutput = pathOutput
        self.grafo = nx.Graph(attr="residues")#representa al grafo a generar...

    #metodo que permite transformar a float...
    def transformFloat(self, array):

        for i in range(len(array)):
            array[i]=float(array[i])
        return array

    #metodo que permite leer el archivo con la matriz generada...
    def readMatrixData(self):

        self.MatrixData = []
        self.headerList = []
        fileOpen = open(self.matrixName, 'r')
        header = fileOpen.readline()

        self.headerList = header.replace("\n", "").split(",")

        line = fileOpen.readline()

        while line:

            self.MatrixData.append(self.transformFloat(line.replace("\n", "").split(",")))
            line = fileOpen.readline()
        fileOpen.close()

    #metodo que permite trabajar con el header, agregando los elementos al grafo en forma de nodos...
    def addNodesToGraph(self):
        #comenzamos a agregar nodos al grafo...
        for element in self.headerList:
            self.grafo.add_node(element,data=str(element))

    #metodo que permite trabajar con la matriz y el header y agregar los edge al grafo con sus respectivos pesos
    def addEdgeToGraph(self, matrixNorm):

        self.numberEdge =0

        for i in range (len(matrixNorm)):
            for j in range (len(matrixNorm[i])):
                if matrixNorm[i][j]!= 0:
                    self.grafo.add_edge(self.headerList[i], self.headerList[j], weight=matrixNorm[i][j], label=str(matrixNorm[i][j]))
                    self.numberEdge+=1

    #metodo que permite crear el grafo a partir de la matriz de adjacencia...
    def createGrphFromMatrix(self):
        #matrixNorm = preprocessing.normalize(self.MatrixData, norm='l2')

        self.addNodesToGraph()
        self.addEdgeToGraph(self.MatrixData)

    #metodo que permite aplicar diversos algoritmos al grafo generado...
    def searchSubGraphs(self):

        #responsePairs = approx.all_pairs_node_connectivity(self.grafo)
        self.grafo.remove_edges_from(self.grafo.selfloop_edges())
        k_components = approx.k_components(self.grafo)#una opcion haciendo k-means en el grafo!
        for key in k_components:
            print k_components[key]

        #maxCliquesData = approx.max_clique(self.grafo)
        #print maxCliquesData

        #averageCluster = approx.average_clustering(self.grafo, trials=1000)
        #print averageCluster
        #cliks = clic.enumerate_all_cliques(self.grafo)
        #cliks = clic.find_cliques(self.grafo)
        #for clique in cliks:
        #    print clique

        #comunities = list(nx.k_clique_communities(self.grafo, 3))
        #print comunities
