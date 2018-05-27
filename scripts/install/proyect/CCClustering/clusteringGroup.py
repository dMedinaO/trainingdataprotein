'''
clase que permite crear grupos de elementos con respecto a un clustering generado,
el objetivo general, es generar nuevos set de datos, con respecto a la data que estos poseen
y en base a su valor de coeficiente de siluetas.

Se aplicaran diversos algoritmos y se seleccionaran aquellos en los cuales se cumplan las siguientes condiciones:

1. El valor de coeficiente de siluetas debe ser mayor a 0
2. El numero de integrantes por grupo, para cada grupo, debe ser mayor a 30
3. Las clases deben ser distribuidas equitativamente en razones de 50/50, 40/60, 30/70
'''

from proyect.CCProcesFile import document #para hacer la instancia a la clase de lectura y escritura de archivos...
from proyect.CCProcesFile import procesFile#para hacer el procesamiento completo...
from proyect.CCClustering import processClustering#para ejecutar diversos clustering
from proyect.CCClustering import evaluateClustering#para hacer la evaluacion del clustering...
from proyect.CCClustering import createNewClusterGroup#para hacer los grupos...

class clusteringDataSet(object):

    def __init__(self, nameFile, pathOutput, splitter):#constructor de la clase...
        self.nameFile = nameFile
        self.pathOutput = pathOutput
        self.splitter = splitter
        self.processObject = procesFile.processDataSet(self.nameFile, self.pathOutput, self.splitter)
        self.prepareDataSet()
        self.getMatrixWhitOutClass()
        print self.matrixWithOutClass[0]

        self.processClusteringObject = processClustering.aplicateClustering(self.matrixWithOutClass)

    #metodo que permite crear el set de datos, la idea es que el set de datos no posea las clases...
    def prepareDataSet(self):

        self.processObject.processMatrixData()
        self.processObject.checkAttributesInMatrixNotExport()
        self.classValues = []

        #obtenemos las clases...
        for element in self.processObject.matrixData:
            self.classValues.append(element[-1])

    #transformamos  a float cada atributo...
    def transformFloat(self):
        for i in range(len(self.matrixWithOutClass)):
            for j in range(len(self.matrixWithOutClass[i])):
                self.matrixWithOutClass[i][j] = float(self.matrixWithOutClass[i][j])

    #metodo que permite obtener la matriz sin el atributo clase...
    def getMatrixWhitOutClass(self):

        self.matrixWithOutClass = []

        for element in self.processObject.matrixData:
            self.matrixWithOutClass.append(element[:-1])

        self.transformFloat()

    #metodo que permite aplicar diversas metodologias de clustering...
    def applyClusteringOptions(self):

        #aplicamos AffinityPropagation
        print "Aplicando AffinityPropagation"
        self.processClusteringObject.aplicateAffinityPropagation()
        evaluateData = evaluateClustering.checkGroups(self.processClusteringObject.model, self.processClusteringObject.labels, self.matrixWithOutClass, 20, self.classValues)

        #preguntamos por el valor de las condiciones...
        if evaluateData.isValid == True:
            descripcion = {'method': 'AffinityPropagation', 'coeficiente_siluetas': evaluateData.performance}
            groupCreate = createNewClusterGroup.createGroups(self.matrixWithOutClass, descripcion, self.pathOutput, "AffinityPropagation/", ',', self.processClusteringObject, self.processObject.header)

        #aplicamos clustering k means...
        for i in range(2,10):
            print "Aplicando KMeans con %d vecinos" % i
            self.processClusteringObject.aplicateKMeans(i)
            evaluateData = evaluateClustering.checkGroups(self.processClusteringObject.model, self.processClusteringObject.labels, self.matrixWithOutClass, 20, self.classValues)

            if evaluateData.isValid == True:
                descripcion = {'method': 'KMeans', 'coeficiente_siluetas': evaluateData.performance}
                nameDir = 'KMeans%d/' % i
                groupCreate = createNewClusterGroup.createGroups(self.matrixWithOutClass, descripcion, self.pathOutput, nameDir, ',', self.processClusteringObject, self.processObject.header)

        #aplicamos clustering aglomerativo...
        for linkage in ['ward', 'complete', 'average']:
            for affinity in ['euclidean', 'l1', 'l2', 'manhattan', 'cosine']:
                for i in range (2, 10):
                    print "Aplicando AgglomerativeClustering con %d vecinos, %s linkage y %s affinity" % (i, linkage, affinity)
                    self.processClusteringObject.aplicateAlgomerativeClustering(linkage, affinity, i)
                    evaluateData = evaluateClustering.checkGroups(self.processClusteringObject.model, self.processClusteringObject.labels, self.matrixWithOutClass, 20, self.classValues)
                    if evaluateData.isValid == True:
                        descripcion = {'method': 'AgglomerativeClustering', 'coeficiente_siluetas': evaluateData.performance, 'linkage':linkage, 'affinity':affinity, 'numberK':i}
                        nameDir = 'AgglomerativeClustering_%s_%s_%d/' % (linkage, affinity, i)
                        groupCreate = createNewClusterGroup.createGroups(self.matrixWithOutClass, descripcion, self.pathOutput, nameDir, ',', self.processClusteringObject, self.processObject.header)
