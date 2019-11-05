'''
clase que tiene la responsabilidad de trabajar con la matriz de adyasencia y generar el correspondiente grafo,
a partir de la matriz permite la agregacion de los nodos, las aristas y los pesos correspondientes.

La matriz a trabajar sera normalizada para que no existan datos demasiado desproporcionados...
'''
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import collections
from networkx.drawing.nx_agraph import write_dot

from networkx.algorithms import approximation as apxa
from networkx.algorithms import bipartite

class createGraph(object):

    def __init__(self, matrixData, header, pathOutput, codePDB):

        self.matrixData = matrixData
        self.codePDB = codePDB
        self.header = header[1:]
        self.pathOutput = pathOutput
        self.grafo = nx.Graph(attr="Aminoacidos")#representa al grafo a generar...

    #metodo que permite crear el grafo a partir de la matriz de adjacencia...
    def createGrphFromMatrix(self):
        matrixRemove = self.removeFirstCol()
        matrixRemove = preprocessing.normalize(matrixRemove, norm='l2')
        self.grafo = nx.from_numpy_matrix(np.array(matrixRemove))

    #metodo que permite trabajar con el header, agregando los elementos al grafo en forma de nodos...
    def addNodesToGraph(self):
        self.header = self.header[1:]#le quitamos el -

        #comenzamos a agregar nodos al grafo...
        for element in self.header:
            self.grafo.add_node(element,data=str(element))

    #metodo que permite trabajar con la matriz quitando la primera columna...
    def removeFirstCol(self):
        matrixRemove = []
        for element in self.matrixData:
            matrixRemove.append(element[1:])
        return matrixRemove

    #metodo que permite trabajar con la matriz y el header y agregar los edge al grafo con sus respectivos pesos
    def addEdgeToGraph(self):

        matrixRemove = self.removeFirstCol()
        #scaler = StandardScaler()
        #scaler.fit(matrixRemove)
        #matrixRemove = scaler.transform(matrixRemove)
        self.numberEdge =0
        #matrixRemove = preprocessing.normalize(matrixRemove, norm='l2')
        for i in range (len(matrixRemove)):
            for j in range (len(matrixRemove[i])):
                if matrixRemove[i][j]!= 0:
                    self.grafo.add_edge(self.header[i], self.header[j], weight=matrixRemove[i][j], label=str(matrixRemove[i][j]))
                    self.numberEdge+=1

    #metodo que permite visualizar el grafo...
    def showGraph(self):

        posD = nx.spectral_layout(self.grafo)
        nx.draw(self.grafo,posD,node_color='#A0CBE2', node_size=50, width=0.1,edge_cmap=plt.cm.Blues,with_labels=False)
        plt.show()

    #funcion que permite buscar los sub grupos dentro del grafo generado...
    def searchSubGrafos(self):

        print  nx.all_pairs_node_connectivity(self.grafo)

    #metodo que permite crear el archivo de salida...
    def createFileData(self, nodeList, linksList):

        nameFile = self.pathOutput+self.codePDB+"_graph.js"
        fileWrite = open(nameFile, 'w')
        fileWrite.write('var graph = {\n\n')

        #comenzamos a escribir la seccion de los nodos...
        fileWrite.write('nodes:[\n')

        for element in nodeList:
            for key in element:
                data = "{%s:'%s'}, " % (key, element[key])
            fileWrite.write(data)
        fileWrite.write("\n")
        fileWrite.write('],\n\n')

        #comenzamos a escribir la seccion de los links...
        fileWrite.write('links:[\n')

        for element in linksList:
            for key in element:
                value = key.split('-')
                data = "{source:%d, target:%d, value:%f}," %(int(value[0]), int(value[1]), float(element[key]))
                fileWrite.write(data)
        fileWrite.write('\n]\n\n')

        fileWrite.write('};')
        fileWrite.close()
    #metodo que permite crear el archivo para su visualizacion...
    def createGraphExportJS(self):

        matrixRemove = self.removeFirstCol()
        matrixRemove = preprocessing.normalize(matrixRemove, norm='l2')
        #creamos un arrego que posea la informacion de los nodos...
        nodes=[]
        for element in self.header:
            dictValue = {'aminoA':element}
            nodes.append(dictValue)

        #agregamos los edges...
        linksList = []
        for i in range (len(matrixRemove)):
            for j in range (len(matrixRemove[i])):
                if matrixRemove[i][j]!= 0:
                    value = "%d-%d" % (i,j)
                    dictValue = {value:matrixRemove[i][j]}
                    linksList.append(dictValue)

        #exportamos el archivo...
        self.createFileData(nodes, linksList)
