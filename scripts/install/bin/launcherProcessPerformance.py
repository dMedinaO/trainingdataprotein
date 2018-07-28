'''
script que permite procesar las performance obtenidas por el proceso de entrenamiento...
'''

from proyect.CCTraining import processDistributionTraining
import sys

#get data
inputData = sys.argv[1]
pathOutput = sys.argv[2]

#instance object
process = processDistributionTraining.processPerformance(inputData, pathOutput)
process.processInfo()
