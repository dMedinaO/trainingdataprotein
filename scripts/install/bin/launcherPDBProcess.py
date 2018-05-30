'''
permite procesar el archivo PDB, generar las matrices y evaluar diversas caracteristicas...
'''

from proyect.CCProcessPDB import processPDB
import sys
import subprocess

#recibimos los datos de entrada para generar el objeto de interes...
# NOTE: el archivo pdb a trabajar debe estar protonado...
pathFile = sys.argv[1]
namePDB = sys.argv[2]
pathOutput = sys.argv[3]
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

print "Create Energy Matrix Void"
processPDBObject.createMatrixEnergyVoid()
