'''
clase con la responsabilidad de recibir un set de datos que posee las clases y los grupos,
crea un directorio con la informacion y un archivo resumen, ademas genera la evaluacion grafica del coeficiente
de siluetas, y los directorios asociados a cada componente, ademas de normalizar los datos y entrenar los modelos...
'''

from proyect.CCClustering import graphicSilohuette#para crear el grafico de siluetas...
from proyect.CCProcesFile import document #para hacer la instancia a la clase de lectura y escritura de archivos...
from proyect.CCStatistic import normalize #para normalizar el set de datos...
#para hacer el entrenamiento de modelos...
from proyect.CCTraining import naiveBayes, adaBoost, knnAlgorithm, decisionTrees, gradientTreeBoost, nuSVC, SVC, randomForest, performanceScore, processPerformance
from proyect.CCTraining import resumeResult

import subprocess
import json

class createGroups(object):

    def __init__(self, dataSet, description, pathOutput, nameDir, splitter, model, header):

        self.header = header
        self.dataSet = dataSet
        self.description = description
        self.pathOutput = pathOutput
        self.splitter = splitter
        self.nameDir = self.pathOutput+nameDir
        self.model = model
        self.createDirForOutput(self.nameDir)#creamos el directorio...
        self.createJSONFile()#creamos el archivo de descripcion de los datos...
        try:
            self.createSilhouetteCoef(self.model)
        except:
            pass

        #creamos los directorios para los grupos...
        self.createDirForGroups()
        self.exportGroupsCSV()

    #metodo que permite hacer los directorios para los grupos...
    def createDirForGroups(self):

        numberCluster = list(set(self.model.labels))

        for numberK in numberCluster:
            command = "mkdir -p %s%d" % (self.nameDir, numberK)
            subprocess.call(command, shell=True)

    #metodo que permite agregar los elementos al set de datos del grupo y segun el exportarlo al csv...
    def exportGroupsCSV(self):

        numberCluster = list(set(self.model.labels))
        for number in numberCluster:
            nameFile= "group_%d.csv" % int(number)
            pathOutputForGroup = self.nameDir+str(number)+"/"
            matrixForGroup = []
            for element in self.dataSet:
                if element[-1] == number:
                    row = []
                    for i in range(15):
                        row.append(element[i])
                    row.append(element[-2])
                    matrixForGroup.append(row)
                    document.document(nameFile, pathOutputForGroup).createExportFileWithPandas(matrixForGroup, self.header)

                    #creamos el directorio para normalizar la informacion del grupo y poder entrenar el modelo...
                    pathNormaliced = self.nameDir+str(number)+"/Normaliced/"
                    self.createDirForOutput(pathNormaliced)
                    print "Normaliced group"
                    #hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
                    normalObject = normalize.NormalizeData(self.header, matrixForGroup, pathNormaliced)
                    normalObject.createMatrixNorm()

                    pathTraining = self.nameDir+str(number)+"/Training/"
                    #entrenamiento de modelos...
                    self.trainingDataSet(normalObject, pathTraining)
                    
    #metodo que permite hacer el entrenamiento del set de datos...
    def trainingDataSet(self, normalObject, pathDir):

        ListResultAlgorithm = []
        try:
            naiveBayesValue = naiveBayes.naiveBayes(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(naiveBayesValue)
        except:
            pass
        try:
            adaBoostValue = adaBoost.adaBoost(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(adaBoostValue)
        except:
            pass
        try:
            knnAlgorithmValue = knnAlgorithm.knnAlgorithm(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(knnAlgorithmValue)
        except:
            pass
        try:
            decisionTreesValue = decisionTrees.decisionTrees(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(decisionTreesValue)
        except:
            pass
        try:
            gradientTreeBoostValues = gradientTreeBoost.gradientTreeBoost(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(gradientTreeBoostValues)
        except:
            pass
        try:
            nuSVCValue = nuSVC.nuSVC(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(nuSVCValue)
        except:
            pass
        try:
            SVCValue = SVC.SVCObjet(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(SVCValue)
        except:
            pass
        try:
            randomForestValue = randomForest.randomForest(normalObject.matrixNormalized,2)
            ListResultAlgorithm.append(randomForestValue)
        except:
            pass
        try:
            #hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
            self.createDirForOutput(pathDir)
            #hacemos la instancia al objeto...
            resumen = resumeResult.resumePerformance(ListResultAlgorithm, pathDir)
        except:
            pass

    #metodo que permite hacer el grafico del coeficiente de siluetas....
    def createSilhouetteCoef(self, model):

        numberCluster = len(list(set(model.labels)))
        graphic = graphicSilohuette.groupGraphicSil(self.dataSet, model.labels, self.nameDir, numberCluster, model.model.cluster_centers_)
        graphic.createGraphic()

    #metodo que permite crear un directorio...
    def createDirForOutput(self, nameDirCreate):

        command = "mkdir -p %s" % nameDirCreate
        subprocess.call(command, shell=True)

    #metodo que permite crear un archivo en formato json con la informacion que posee sobre la generacion del grupo...
    def createJSONFile(self):

        nameFileOutput = self.nameDir+"descriptionCreateGroup.json"
        with open(nameFileOutput, "w") as outfile:
            json.dump(self.description, outfile)
