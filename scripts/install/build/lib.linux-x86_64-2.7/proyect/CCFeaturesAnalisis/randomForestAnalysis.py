'''
clase con la responsabilidad de aplicar el algoritmo de random forest con el fin de ir evaluando cada una de las features existentes
y determinar la importancia que estas poseen para la generacion del clasificador, genera un conjunto de resultados que son de interes
a la hora de evaluar cada uno de los componentes...

Recibe como entrada el set de datos normalizado y el path donde se dispondra de los resultados...
'''
from sklearn.ensemble import RandomForestClassifier
from proyect.CCProcesFile import document

class featureImportance(object):

    def __init__(self, dataSet, pathOutput):

        self.dataSet = dataSet
        self.pathOutput = pathOutput

        #criterion for config exec algorithm
        self.criterionList = ['gini', 'entropy']
        self.n_estimatorsList = [10, 20, 50, 100, 150, 200, 250, 500, 750, 1000, 1500]

    #metodo que permite hacer la lectura de la matriz normalizada...
    def getDataSet(self):

        doc = document.document(self.dataSet, self.pathOutput)
        self.data = doc.readMatrix()[1:]#remove header

    #metodo que recibe una lista y la transforma a flotante...
    def transformFloat(self, listData):

        for i in range(len(listData)):
            listData[i] = float(listData[i])
        return listData

    #metodo que permite separar los atributos, dejando en un array las clases y en otro los valores...
    def getClassAndAttributes(self):

        self.dataWC = []
        self.classAttribute = []

        for element in self.data:
            self.dataWC.append(self.transformFloat(element[:-1]))
            self.classAttribute.append(element[-1])

    #metodo que permite aplicar el algoritmo y hacer las evaluaciones correspondientes...
    def checkFeatures(self):

        for criterion in self.criterionList:
            for n_estimators in self.n_estimatorsList:

                print "RandomForest, criterion: %s n_estimators: %d" % (criterion, n_estimators)
                clf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=n_estimators, n_jobs=-1, criterion=criterion)
                clf = clf.fit(self.dataWC, self.classAttribute)

                
