'''
script que permite manejar las iteraciones de la generacion de grupos aleatorios...
'''

from proyect.CCMakeGroups import generateRandomGroupValues
from proyect.CCProcesFile import procesFile
import pandas as pd
import sys
import subprocess

nameFile = sys.argv[1]#el archivo original...
pathOutput = sys.argv[2]#el directorio de salida...
groups = int(sys.argv[3])#la cantidad de grupos a generar
iterator = int(sys.argv[4])#la cantidad de iteraciones a generar...

#creamos el directorio a almacenar la informacion...
pathOutputGroups = "%s%d_groupsRandom/" % (pathOutput, groups)
command = "mkdir -p %s" % pathOutputGroups
subprocess.call(command, shell=True)

process = procesFile.processDataSet(nameFile, pathOutput, ',')
process.processMatrixData()#procesamos la matriz...

#instanciamos al objeto generator...
process.header.pop(13)
generator = generateRandomGroupValues.groupRandomGenerator(groups, pathOutputGroups, process.matrixData, process.header, iterator)
generator.createProcess()
