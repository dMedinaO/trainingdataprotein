'''
script que permite hacer la division de un set de datos con respecto al uso inteligente de tecnicas de clustering...
'''

import sys
from proyect.CCSplitter import createSpliterGroup, evaluatedModels

dataSet = sys.argv[1]
pathOutput = sys.argv[2]

splitter = createSpliterGroup.splitterGroup(dataSet)

#aplicamos todos los modelos posibles...
try:
    splitter.applyKMeans()
except:
    pass
try:
    splitter.aplicateBirch()
except:
    pass
try:
    splitter.aplicateAlgomerativeClustering()
except:
    pass

#hacemos la evaluacion de los modelos...
evaluation = evaluatedModels.evaluatedClustering(splitter.ListModel, splitter.dataSet, pathOutput)
evaluation.checkSilohuetteCoeficient()
evaluation.checkSecondCriterion()
