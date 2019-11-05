'''
clase con la responsabilidad de evaluar los modelos generados de clustering...
'''
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from proyect.CCSplitter import modelGroup

class evaluatedClustering(object):

    def __init__(self, ListModel, dataSet, pathOutput):

        self.ListModel = ListModel
        self.dataSet = dataSet
        self.calinskiList = []
        self.siluetas = []
        self.pathOutput = pathOutput
        self.header = ['AAWt', 'AAMt', 'Sstruct', 'SaccW', 'ShbondsW', 'SaccM', 'ShbondsM', 'yDDG', 'Result', 'Positiontype', 'ProteinPropens',	'Positionaccept', 'MOSST', 'SectorSuperficie', 'Functionalrelevancefunction']

    #metodo que permite aplicar coeficiente de siluetas a toda la data del modelo...
    def checkSilohuetteCoeficient(self):

        for i in range (len(self.ListModel)):
            try:
                print "evaluated: ", self.ListModel[i].algorithm, " ", self.ListModel[i].description
                silohuette = metrics.silhouette_score(self.dataSet, self.ListModel[i].model.labels_, metric='euclidean')
                calinski = metrics.calinski_harabaz_score(self.dataSet, self.ListModel[i].model.labels_)
                self.ListModel[i].silohuette = silohuette
                self.ListModel[i].calinski = calinski
                self.calinskiList.append(calinski)
                self.siluetas.append(silohuette)
            except:
                pass

    #obtenemos el modelo con mayor calinski y con mayor coeficiente de siluetas...
    def getBestModel(self):

        maxCalinski = max(self.calinskiList)
        print maxCalinski
        bestModel = []

        #buscamos los modelos con los mejores valores...
        for model in self.ListModel:
            if model.calinski == maxCalinski:
                if model not in bestModel:
                    bestModel.append(model)

        return bestModel

    #metodo que evalua la proporcion de los elementos en las etiquetas...
    def evaluatedProportion(self, labels):

        cont1 = 0
        cont0 = 0

        for element in labels:
            if element == 0:
                cont0+=1
            else:
                cont1+=1

        return cont0, cont1

    #metodo que permite obtener las proporciones...
    def getProportion(self, cont0, cont1):

        proportion = []
        for i in range (len(cont1)):
            if cont1[i]>=cont0[i]:
                proportion.append(float(cont0[i])/float(cont1[i]))
            else:
                proportion.append(float(cont1[i])/float(cont0[i]))
        return proportion

    #obtenemos el mejor modelo segun la proporcion...
    def getProportionData(self, proportion):

        maxProportion = max(proportion)
        index = 0

        for i in range(len(proportion)):
            if proportion[i] == maxProportion:
                index = i
                break
        return index

    #metodo que permite chequear el segundo filtro de los grupos...
    def checkSecondCriterion(self):

        bestModel = self.getBestModel()#son los mejores modelos segun los criterios
        cont1List = []
        cont0List = []

        #evaluamos la distribucion de los grupos...
        for model in bestModel:
            cont0, cont1 = self.evaluatedProportion(model.model.labels_)
            cont0List.append(cont0)
            cont1List.append(cont1)

        proportion = self.getProportion(cont0List, cont1List)
        index = self.getProportionData(proportion)

        #con el modelo generamos los archivos de salida...
        bestModel[index].exportData(self.dataSet, self.header, self.pathOutput)
        bestModel[index].createSummary(self.pathOutput)
