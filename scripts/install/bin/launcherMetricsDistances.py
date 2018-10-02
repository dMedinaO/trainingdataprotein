'''
script que permite hacer el calculo de distancias para la evaluacion de comunidades mediante tecnicas de grafos
'''

from proyect.CCMakeGroups import createAdyacenciaMatrix
from proyect.CCProcesFile import document
from sklearn.preprocessing import normalize
import sys

#recibimos los datos de entrada...
matrixData = sys.argv[1]
pathOutput = sys.argv[2]

#hacemos la lectura y parseamos la data para obtener solo flotantes sin la clase...
matrix = document.document(matrixData, pathOutput).readMatrix()
#matrix = matrix[1:]#removemos el header...

#obtenemos los demas datos sin la columna asociada a la clase...
matrixRemove = []

for element in matrix:
    row = []
    for i in range(len(element)):
        row.append(float(element[i]))
    matrixRemove.append(row)

matrixRemove = normalize(matrixRemove, axis=0, norm='max')

#formamos el header...
header = []
for i in range (1, len(matrixRemove)+1):

    header.append(str(i))

madj = createAdyacenciaMatrix.distanceSamples(matrixRemove, header, pathOutput)
madj.createAdjacenceMatrix()
