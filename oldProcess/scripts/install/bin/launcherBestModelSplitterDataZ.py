'''
script que permite hacer la ejecucion de los multiples modelos que fueron seleccionados como mejores
segun su valor obtenido en la distribucion de modelos...
'''

from proyect.CCMakeModels import createBestModelSummaryWithLOUZ
from proyect.CCProcesFile import document
import sys

#recibimos la data de entrada...
matrixData = sys.argv[1]
pathOutput = sys.argv[2]

#hacemos la lectura de la matriz...
matrixInput = document.document(matrixData, pathOutput).readMatrix()
matrixInput = matrixInput[1:]

#hacemos el parse a float e int...
for i in range(len(matrixInput)):
    for j in range (len(matrixInput[i])):
        if j < len(matrixInput[i])-1:
            matrixInput[i][j] = float(matrixInput[i][j])
        else:
            matrixInput[i][j] = int(matrixInput[i][j])

models = createBestModelSummaryWithLOUZ.createBestModels(matrixInput, pathOutput)
models.processModels()
