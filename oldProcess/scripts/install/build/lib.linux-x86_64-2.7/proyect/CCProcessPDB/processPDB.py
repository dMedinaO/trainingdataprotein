'''
clase con la responsabilidad de parsear el archivo pdb y almacenar la informacion del mismo en forma de objeto
con el fin de poder utilizarla en posteriores procesos...
Recibe como entrada un codigo PDB, ademas del path donde se encuentra el mismo...
'''
from Bio.PDB.PDBParser import PDBParser
from proyect.CCProcesFile import document

class processPDB(object):

    def __init__(self, codePDB, pathFile, namePDB, pathOutput):

        self.codePDB = codePDB
        self.pathFile = pathFile
        self.pathOutput = pathOutput
        self.namePDB = namePDB
        self.residuesValids = ['ALA', 'LYS', 'ARG', 'HIS', 'PHE', 'THR', 'PRO', 'MET', 'GLY', 'ASN', 'ASP', 'GLN', 'GLU', 'SER', 'TYR', 'TRP', 'VAL', 'ILE', 'LEU', 'CYS']
        self.ListResidues = []

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
        self.header.append('-')
        for element in self.ListResidues:#para cada residuo obtenemos el full name...
            fullID = element.get_full_id()
            nameResidue = "%s-%d-%s" % (element.resname, int(fullID[3][1]), fullID[2])
            self.header.append(nameResidue)

    #metodo que permite crear la matrix con solo 0...
    def generateMatrixOnes(self):

        matrixData = []
        self.createHeader()#creamos el header...

        #creamos los elementos de la matriz...
        for i in range(1, len(self.header)):
            row = []
            row.append(self.header[i])

            #completamos con 0....
            for j in range(len(self.ListResidues)):
                row.append(0)
            matrixData.append(row)
        return matrixData

    #metodo que permite generar la matriz de elementos...
    def createMatrixEnergyVoid(self):

        matrixData = self.generateMatrixOnes()

        #exportamos el documento, crearemos diversos documentos con respecto a los calculos de energia...
        nameFile = "matrix_energy_H_Bonds_Network_pdb_%s.csv" % self.codePDB
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)
        nameFile = "matrix_energy_H_Bonds_All_pdb_%s.csv" % self.codePDB
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)
        nameFile = "matrix_energy_Covalent_pdb_%s.csv" % self.codePDB
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)
        nameFile = "matrix_energy_SideChain_pdb_%s.csv" % self.codePDB
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)
        nameFile = "matrix_energy_Esteric_pdb_%s.csv" % self.codePDB
        document.document(nameFile, self.pathOutput).createExportFileWithPandas(matrixData, self.header)
