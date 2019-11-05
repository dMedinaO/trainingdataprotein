'''
permite procesar el archivo PDB, generar las matrices y evaluar diversas caracteristicas...
'''

from proyect.CCProcessPDB import processPDB, calculateHBondsBestNetwork, parserDegreePhiPsi, calculateCovalentEnergy
from proyect.CCProcessPDB import joinMatrixEnergy

import sys
import subprocess

#recibimos los datos de entrada para generar el objeto de interes...
# NOTE: el archivo pdb a trabajar debe estar protonado...
pathFile = sys.argv[1]
namePDB = sys.argv[2]
pathOutput = sys.argv[3]
responseWhatIf = sys.argv[4]
degreeFile = sys.argv[5]

data = namePDB.split('.')
codePDB = data[0]

#creamos el directorio asociado al archivo PDB...
command = "mkdir -p %s%s/" % (pathOutput, codePDB)
subprocess.call(command, shell=True)

pathOutput = pathOutput+codePDB+"/"
#instanciamos al objeto...
print "Process PDB"
processPDBObject = processPDB.processPDB(codePDB, pathFile, namePDB, pathOutput)
processPDBObject.getAllResiduesPDB()

#hacemos el procesamiento de la informacion con los datos
print "Create Energy Matrix for HBonds optim hBondsNetwork"
nameMatrix = "matrix_energy_H_Bonds_Network_pdb_%s.csv" % codePDB
hBondsNetworkValue = calculateHBondsBestNetwork.hBondsNetwork(processPDBObject, responseWhatIf, nameMatrix, pathOutput)
hBondsNetworkValue.processResponseWI()
hBondsNetworkValue.createDictValues()
hBondsNetworkValue.processHBondsSearch()
hBondsNetworkValue.exportDocument()

#hacemos el procesamiento de las energias covalentes...
print "Process degreee values for protein"
nameMatrix = "matrix_energy_Covalent_pdb_%s.csv" % codePDB
parserDegree = parserDegreePhiPsi.degreeValues(degreeFile, pathOutput)
covalenteValues = calculateCovalentEnergy.covalenteEnergyProcess(processPDBObject, parserDegree, nameMatrix, pathOutput)
covalenteValues.processELOC1()
covalenteValues.processELOC2()
covalenteValues.processELOC3()

print covalenteValues.processPDBObject.header
covalenteValues.exportMatrix()

print "Join Matrix Full"
nameMatrix = "matrix_energy_full_pdb_%s.csv" % codePDB
joinMatrix = joinMatrixEnergy.fullMatrixEnergy(processPDBObject, hBondsNetworkValue, covalenteValues, nameMatrix, pathOutput, codePDB)
joinMatrix.createFullMatrix()
joinMatrix.createMatrixRemoveCol()
joinMatrix.createGraphData()
