'''
clase que permite poder ejecutar las diversas acciones asociadas al tratamiento de datos, el procesamiento de la
informacion, la generacion de estadisticas y los entrenamientos de modelos...
'''

from proyect.CCClustering import checkSplitterBySector

import sys
import os
import subprocess

#recibimos los datos de entrada...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]

pathOutputProcessFile = pathOutput+"evaluated/"
command = "mkdir -p %s" % pathOutputProcessFile
subprocess.call(command, shell=True)

#hacemos la instancia al procesamiento de la informacion....
checkGroup = checkSplitterBySector.evaluateSplitSectorSuperfice(nameFile, pathOutputProcessFile, ',', 13)
