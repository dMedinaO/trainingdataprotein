'''
script que permite generar la ejecucion del procesamiento de datos para el histograma de elementos
aleatorios...
'''

from proyect.CCStatistic import processHistogramRandomFull
import sys

#recibimos los argumentos de entrada...
pathInput = sys.argv[1]
pathOutput = sys.argv[2]
iteration  = int(sys.argv[3])
groupsNumber = int(sys.argv[4])
splitter = sys.argv[5]

#hacemos la instancia...
histDataRandom = processHistogramRandomFull.processHistogramRandom(pathInput, pathOutput, iteration, groupsNumber, splitter)
histDataRandom.processData()#procesamos la data...
histDataRandom.processHistogramGeneration()#generamos los histogramas...
