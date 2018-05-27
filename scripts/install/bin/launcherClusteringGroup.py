'''
launcher para la ejecucion de la generacion de nuevos grupos con respecto a la division por clustering
que se aplica...
'''

from proyect.CCClustering import clusteringGroup

import sys
import os
import subprocess

#recibimos los datos de entrada...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]

clusterGroup = clusteringGroup.clusteringDataSet(nameFile, pathOutput, ',')
clusterGroup.getMatrixWhitOutClass()
clusterGroup.applyClusteringOptions()
