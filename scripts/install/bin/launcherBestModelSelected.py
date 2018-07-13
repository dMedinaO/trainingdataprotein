'''
script que permite ejecutar la busqueda de los mejores modelos y sus parametros con respecto a la distribucion y los outliers extremos que estos poseen
'''

from proyect.CCModels import getBestModelsForDistribution
import sys

#recibimos la data de entrada...
pathResponse = sys.argv[1]
group = int(sys.argv[2])
pathRoot = sys.argv[3]
pathOutput = sys.argv[4]

searching = getBestModelsForDistribution.bestModel(pathResponse, group, pathRoot, pathOutput)
searching.getBestPerformanceDist()
print searching.dictOutliers
searching.searchParamForOutlier()
searching.exportDocument()
