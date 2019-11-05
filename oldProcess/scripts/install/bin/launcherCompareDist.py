'''
script que permite hacer la comparacion de las muestras y evaluar si son significativas para un grupo...
'''

from proyect.CCStatistic import compareDistributionGroups
import sys

pathInput = sys.argv[1]
pathOutput = sys.argv[2]
numberGroup = int(sys.argv[3])

compareValues = compareDistributionGroups.compareDist(pathInput, pathOutput, numberGroup)
compareValues.handlerCompareProcess()
