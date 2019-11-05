'''
script que permite procesar las performance obtenidas por el proceso de entrenamiento...
'''

from proyect.CCTraining import processDistributionTraining
import sys
import subprocess

#get data
inputData = sys.argv[1]
pathOutput = sys.argv[2]
stdValue = float(sys.argv[3])

headerList = ['accuracy', 'recall', 'precision']

for header in headerList:

    print "process element ", header
    #creamos el path...
    command = "mkdir -p %s%s" % (pathOutput, header)
    subprocess.call(command, shell=True)

    #instance object
    process = processDistributionTraining.processPerformance(inputData, pathOutput+header+"/", header, stdValue)
    process.processInfo()
