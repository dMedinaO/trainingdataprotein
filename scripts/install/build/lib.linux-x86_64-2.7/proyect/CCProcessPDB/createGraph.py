'''
clase que tiene la responsabilidad de trabajar con la matriz de adyasencia y generar el correspondiente grafo,
a partir de la matriz permite la agregacion de los nodos, las aristas y los pesos correspondientes.

La matriz a trabajar sera normalizada para que no existan datos demasiado desproporcionados...
'''
import networkx as nx
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

class createGraph(object):

    def __init__(self, matrixData, header, pathOutput):

        self.matrixData = matrixData
        self.header = header
        self.pathOutput = pathOutput
        self.grafo = nx.MultiGraph()#representa al grafo a generar...

    #metodo que permite trabajar con el header, agregando los elementos al grafo en forma de nodos...
    def addNodesToGraph(self):
        self.header = self.header[1:]#le quitamos el -

        #comenzamos a agregar nodos al grafo...
        for element in self.header:
            self.grafo.add_node(element)

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

        matrixRemove = preprocessing.normalize(matrixRemove, norm='l2')
        for i in range (len(matrixRemove)):
            for j in range (len(matrixRemove[i])):
                if matrixRemove[i][j]!= 0:
                    print "--------------"
                    print matrixRemove[i][j]
                    print self.header[i]
                    print self.header[j]
                    print "-------------"
                    #agregamos el edge...
                    self.grafo.add_edge(self.header[i], self.header[j], weight=matrixRemove[i][j])

    #metodo que permite visualizar el grafo...
    def showGraph(self):

        nx.draw_spectral(self.grafo, node_color='blue', node_size=120, line_color='grey', linewidths=0, width=0.2)
        plt.show()
