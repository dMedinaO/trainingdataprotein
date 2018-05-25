'''
clase que permite poder ejecutar las diversas acciones asociadas al tratamiento de datos, el procesamiento de la
informacion, la generacion de estadisticas y los entrenamientos de modelos...
'''

from proyect.CCProcesFile import procesFile
from proyect.CCStatistic import normalize
import sys
import os
import subprocess

#recibimos los datos de entrada...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]

pathOutputProcessFile = pathOutput+"inputFile/"
command = "mkdir -p %s" % pathOutputProcessFile
subprocess.call(command, shell=True)

#hacemos la instancia al procesamiento de la informacion....
process = procesFile.processDataSet(nameFile, pathOutputProcessFile, ',')
process.processMatrixData()
process.checkAttributesInMatrix()

#hacemos la instancia para la normalizacion de los datos, creamos un directorio previamente...
pathOuputNormaliced = "%sNormaliced/" % pathOutput
command = "mkdir -p %sNormaliced" % pathOutput
subprocess.call(command, shell=True)
normalize.NormalizeData(process.header, process.matrixData, pathOuputNormaliced).createMatrixNorm()
