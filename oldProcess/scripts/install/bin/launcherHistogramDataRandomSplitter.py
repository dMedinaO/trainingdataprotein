'''
script que permite generar la ejecucion del procesamiento de datos para el histograma de elementos
aleatorios...
'''

from proyect.CCStatistic import processHistogramRandomSplitter
import sys

#recibimos los argumentos de entrada...
pathInput = sys.argv[1]
pathOutput = sys.argv[2]
iteration  = int(sys.argv[3])
splitter = sys.argv[4]

#hacemos la instancia...
histDataRandom = processHistogramRandomSplitter.processHistogramRandomSplitter(pathInput, pathOutput, iteration, splitter)
histDataRandom.processData()#procesamos la data...
histDataRandom.processHistogramGeneration()#generamos los histogramas...
