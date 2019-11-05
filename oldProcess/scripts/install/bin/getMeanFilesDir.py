'''
script que recibe un directorio, lee archivo por archivo y procesa el promedio de cada directorio...
'''

import sys
import numpy as np
import os

#recibimos los argumentos
nameFile = sys.argv[1]
namePath = sys.argv[2]

#hacemos el comando de lectura de los archivos...
fileOpen = open(nameFile, 'r')
listFiles = []

line = fileOpen.readline()
while line:
    listFiles.append(line.replace("\n", ""))
    line = fileOpen.readline()

fileOpen.close()

#por cada archivo, lo leemos, y sacamos el promedio...
for element in listFiles:
    try:
        print element,
        nameDocument = "%s%s" % (namePath, element)
        fileOpen = open(nameDocument, 'r')
        line = fileOpen.readline()
        line = fileOpen.readline()

        dataValues = []
        while line:
            dataValues.append(float(line.replace("\n", "")))
            line = fileOpen.readline()

        print "%f" % (np.mean(dataValues))
        fileOpen.close()
    except:
        pass
