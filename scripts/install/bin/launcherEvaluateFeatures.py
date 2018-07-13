'''
script con la responsabilidad de evaluar las caracteristicas en base al analisis generado a traves de randomForest con deformacion
del espacio de los atributos...
'''

#importamos los modulos
import sys
from proyect.CCFeaturesAnalisis import randomForestAnalysis

dataSet = sys.argv[1]
pathOutput = sys.argv[2]

randomF = randomForestAnalysis.featureImportance(dataSet, pathOutput)
randomF.getDataSet()
randomF.getClassAndAttributes()
print randomF.dataWC[0]
