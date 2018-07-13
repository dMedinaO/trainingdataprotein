'''
clase con la responsabilidad de generar un archivo PDB, este archivo permite generar n sectores, los cuales son pintados de diferentes colores
con respecto a las divisiones generadas, esto con el fin de poder visualizar la division generada, una ves formado el pdb y creado los colores,
se procede a almacenar la informacion de interes en una imagen y un archivo pdb
'''

#modulos a trabajar...
from proyect.CCModels import pdbFile

class createPDBFile(object):

    #constructor de la clase, recibimos el path de entrada y el de salida, ademas de la iteracion a la que corresponde...
    def __init__(self, pathInput, pathOutput, iterator, structPD, group):

        self.iterator = iterator
        self.pathInput = pathInput
        self.pathOutput = pathOutput
        self.structPDB = structPDB
        self.group = group

    #metodo que permite leer el set de datos generados en base a la iteracion
    def getResiduesFromDataSet(self):

        nameFile = "%sgroup_%d/matrixRandom.csv"
