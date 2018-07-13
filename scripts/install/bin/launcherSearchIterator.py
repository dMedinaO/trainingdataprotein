
#script que permite hacer la busqueda de las cantidades de apariciones de los algoritmos y los valores que se generan,

import sys
from proyect.CCModels import algorithmDist
#recibimos los atributos de entrada
pathRoot = sys.argv[1]
groups = int(sys.argv[2])
pathOutput = sys.argv[3]

#hacemos la instancia a los objetos...
algorithm = algorithmDist.searchAlgorithm(pathRoot, groups, pathOutput)
algorithm.searchBestAlgorithm()
algorithm.searchCountValues()
algorithm.createPieChart()
