'''
clase con la responsabilidad de recibir un archivo pdb, leerlo y obtener la informacion de interes...
'''

from Bio.PDB.PDBParser import PDBParser

class pdbFile(object):

    def __init__(self, codePDB, pathInput):

        self.codePDB = codePDB
        self.pathInput = pathInput
        self.namePDB = self.codePDB+".pdb"

    #metodo que genera la lectura del archivo pdb...
    def readPDBFile(self):

        parser = PDBParser()#creamos un parse de pdb
        self.structure = parser.get_structure(self.codePDB, self.pathInput+"/"+self.namePDB)#trabajamos con la proteina cuyo archivo es 1AQ2.pdb
        
