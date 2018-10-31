'''
script que permite evaluar todas las particiones obtenidas mediante Clustering recursivo,
recibe el directorio donde se almancenan los inputs de cada set de datos...
'''

import sys
import pandas as pd

from modulesServiceVHL.CCTestingCR import testingGrup1CR

#testeamos el primer grupo...
dataSet = pd.read_csv(sys.argv[1])
pathOutput = sys.argv[2]

#obtenemos los valores de la clase...
classData = []

for i in range(len(dataSet)):
    classData.append(dataSet['Clinical'][i])

dataSet = dataSet.drop('Clinical', 1)#removemos la clase...
testingC1 = testingGrup1CR.testingGrupo1CR(dataSet, classData)

testingC1.applyModelsAccuracy()
