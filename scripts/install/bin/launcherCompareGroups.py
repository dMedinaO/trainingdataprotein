'''
script que permite generar una matriz de comparacion de grupos para evaluar la significancia estadistica
de estos...
'''

import sys
from proyect.CCStatistic import compareMultipleGroups

pathInput = sys.argv[1]
compare = compareMultipleGroups.compareGroups(pathInput)
compare.readDataSet()
compare.compareGroupsMWT()
