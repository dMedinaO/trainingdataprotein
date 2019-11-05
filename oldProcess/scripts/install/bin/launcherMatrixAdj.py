from proyect.CCProcessPDB import processMatrix

import sys
import subprocess

#data desde la terminal...
codePDB = sys.argv[1]
pathFile = sys.argv[2]
namePDB = sys.argv[3]
pathOutput = sys.argv[4]+codePDB+"/"
distance = int(sys.argv[5])


command = "mkdir -p %s" % pathOutput
subprocess.call(command, shell=True)
process = processMatrix.processMatrix(codePDB, pathFile, namePDB, pathOutput,distance)
process.getAllResiduesPDB()
process.createMatrixEnergyVoid()

process.processDistances()
