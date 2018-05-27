'''
clase con los metodos necesarios para hacer la evaluacion del clustering y que cumpla con las condiciones impuestas previamente.
Si cumple con las condiciones, el atributo isValid posee un valor de 0, en caso contrario, posse un valor de 1.
'''

from sklearn import metrics
from sklearn.metrics import pairwise_distances

class checkGroups(object):

    def __init__(self, model, labels, dataSet, minValue,classData):#constructor de la clase

        self.model = model
        self.labels = labels
        self.groupIndex = list(set(self.labels))#obtenemos los elementos unicos de cada clase...
        self.dataSet = dataSet
        self.addClassAndGroupToDataSet(classData)
        self.evaluateCoeficientSilohuette()
        self.checkMembersGroup()
        self.isValid=False
        self.checkConditions(minValue,classData)
        self.evaluateConditions()

    #metodo que permite aplicar la performance...
    def evaluateCoeficientSilohuette(self):

        self.performance = metrics.silhouette_score(self.dataSet, self.labels, metric='euclidean')
        print self.performance

    #metodo que permite evaluar la cantidad de integrantes por grupo...
    def checkMembersGroup(self):

        groupLabel = list(set(self.labels))
        self.dictCountMembers = {}

        for element in groupLabel:
            cont=0
            for label in self.labels:
                if label == element:
                    cont+=1
            self.dictCountMembers.update({element:cont})
        print self.dictCountMembers

    #metodo que permite poder evaluar si la division seleccionada cumple con las condiciones generadas...
    def checkConditions(self, minValue,classData):

        self.conditionOptions = []

        if self.performance >=0.4:#condicion de performance
            self.conditionOptions.append(True)
        else:
            self.conditionOptions.append(False)

        self.conditionOptions.append(self.checkMembersNumber(minValue))#condicion de numero de miembros...

        self.conditionOptions.append(self.checkClassRate(classData))
    #metodo que permite evaluar la cantidad de integrantes por grupo...
    def checkMembersNumber(self, minValue):

        cont=0

        for element in self.dictCountMembers:
            if self.dictCountMembers[element] < minValue:
                cont=1
                break
        if cont==0:
            return True
        else:
            return False

    #metodo que permite agregar la clase y el grupo al set de datos...
    def addClassAndGroupToDataSet(self, classData):

        self.matrixDataValues = []
        for element in self.dataSet:
            self.matrixDataValues.append(element)

        for i in range (len(self.matrixDataValues)):
            self.matrixDataValues[i].append(classData[i])
            self.matrixDataValues[i].append(self.labels[i])

    #metodo que evalua la taza correspondiente...
    def evaluateRate(self, dictCount):

        total = 0
        values = []
        for data in dictCount:
            total+=dictCount[data]
            values.append(dictCount[data])
        if len(values) == 2:#son dos clases
            minValue = min(values)
            maxValue = max(values)

            rate = float(minValue)/float(maxValue)
            if rate >=0.5:
                return True
            else:
                return False
        else:
            return False

    #metodo que permite evaluar la razon entre las clases...
    def checkClassRate(self, classData):

        #obtenemos las clases unicas...
        uniqueClass = list(set(classData))
        groupRate=[]
        for element in self.groupIndex:#trabajabamos con el grupo...
            dictClassRate = {}
            #actualizamos el diccionario...
            for value in uniqueClass:#trabajabamos con las clases...
                cont=0
                for example in self.matrixDataValues:
                    if example[-1] == element:#es del grupo...
                        if example[-2] == value:#es de la clase...
                            cont+=1
                dictClassRate.update({value:cont})
            groupRate.append(self.evaluateRate(dictClassRate))

        #buscamos si existe uno false...
        cont=True
        for element in groupRate:
            if element == False:
                cont=False
                break
        return cont

    #metodo que permite evaluar los valores de las condiciones modificando el valor del parametro isValid
    def evaluateConditions(self):

        cont=0
        for condition in self.conditionOptions:
            if condition ==True:
                cont+=1
        if cont==3:
            self.isValid=True
