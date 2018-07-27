'''
clase que genera la matriz de adyacencia...
'''

from Bio.PDB.PDBParser import PDBParser
from proyect.CCProcessPDB import createDistances
from proyect.CCProcesFile import document
import subprocess

class processMatrix(object):

    def __init__(self, codePDB, pathFile, namePDB, pathOutput, distMin, distMax):

        self.codePDB = codePDB
        self.pathFile = pathFile
        self.pathOutput = pathOutput
        self.namePDB = namePDB
        self.residuesValids = ['ALA', 'LYS', 'ARG', 'HIS', 'PHE', 'THR', 'PRO', 'MET', 'GLY', 'ASN', 'ASP', 'GLN', 'GLU', 'SER', 'TYR', 'TRP', 'VAL', 'ILE', 'LEU', 'CYS']
        self.ListResidues = []
        self.distMax = distMax
        self.distMin = distMin


    #metodo que permite poder obtener la informacion del archivi PDB, nota: trabajamos con todos los residuos...
    def getAllResiduesPDB(self):

        parser = PDBParser()#creamos un parse de pdb
        self.structure = parser.get_structure(self.codePDB, self.pathFile+"/"+self.namePDB)#trabajamos con la proteina cuyo archivo es 1AQ2.pdb
        self.residuesFull = self.structure.get_residues()

        for model in self.structure:
            for chain in model:
                for residue in chain:
                    if residue.resname in self.residuesValids:
                        self.ListResidues.append(residue)

    #metodo que permite crear el header de la matriz...
    def createHeader(self):

        self.header = []
        for element in self.ListResidues:#para cada residuo obtenemos el full name...
            fullID = element.get_full_id()
            nameResidue = "%s-%d-%s" % (element.resname, int(fullID[3][1]), fullID[2])
            self.header.append(nameResidue)

    #metodo que permite crear la matrix con solo 0...
    def generateMatrixOnes(self):

        matrixData = []
        self.createHeader()#creamos el header...

        #creamos los elementos de la matriz...
        for i in range(len(self.header)):
            row = []
            #completamos con 0....
            for j in range(len(self.ListResidues)):
                row.append(0)
            matrixData.append(row)
        return matrixData

    #metodo que permite generar la matriz de elementos...
    def createMatrixEnergyVoid(self):

        matrixData = self.generateMatrixOnes()
        self.names = []
        #exportamos el documento, crearemos diversos documentos con respecto a los calculos de energia...
        nameFile = "matrix_connectivity_pdb_%s.csv" % self.codePDB
        self.names.append(nameFile)
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)
        nameFile = "matrix_connectivity_Distances_pdb_%s.csv" % self.codePDB
        self.names.append(nameFile)
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)
        nameFile = "matrix_connectivity_Energy_pdb_%s.csv" % self.codePDB
        self.names.append(nameFile)
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)

    #metodo que permite crear los directorios...
    def createPath(self, nameDir):

        command = "mkdir -p %s" % nameDir
        subprocess.call(command, shell=True)

    #metodo que permite procesar las distancias...
    def processDistances(self):

        for i in range (len(self.names)-1):#para los criterios, no esta contando la matriz de energia...
            #creamos el path de salida...
            pathOutputMatrix = "%s%d_%d/" % (self.pathOutput, self.distMin, self.distMax)
            self.createPath(pathOutputMatrix)
            distancesO = createDistances.processDistance(self.names[i], self.pathOutput, self.distMin, self.distMax, i+1, pathOutputMatrix, self.header, self.structure)
            print "process ", self.names[i]
            distancesO.changeValueMatrix()
