from proyect.CCProcessPDB import processMatrix

import sys
import subprocess

#data desde la terminal...
codePDB = sys.argv[1]
pathFile = sys.argv[2]
namePDB = sys.argv[3]
pathOutput = sys.argv[4]+codePDB+"/"

command = "mkdir -p %s" % pathOutput
subprocess.call(command, shell=True)
process = processMatrix.processMatrix(codePDB, pathFile, namePDB, pathOutput, 7,8)
process.getAllResiduesPDB()
process.createMatrixEnergyVoid()
process.processDistances()
