'''
clase que permite poder ejecutar las diversas acciones asociadas al tratamiento de datos, el procesamiento de la
informacion, la generacion de estadisticas y los entrenamientos de modelos...
'''

from proyect.CCProcesFile import procesFile
import sys
import os

#recibimos los datos de entrada...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]

#hacemos la instancia al procesamiento de la informacion....
process = procesFile.processDataSet(nameFile, pathOutput, ',')
process.processMatrixData()
process.checkAttributesInMatrix()
