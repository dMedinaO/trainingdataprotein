'''
script que permite leer un archivo PDB, obtener la secuencia y las cadenas y generar una lista para evaluar
las posibles mutaciones y los efectos que estos tendran con respecto al software SDM.
'''

import sys
from Bio.PDB.PDBParser import PDBParser

namePDB = sys.argv[1]
codePDB = sys.argv[2]

resValues = ['ALA', 'LYS', 'ARG', 'HIS', 'PHE', 'THR', 'PRO', 'MET', 'GLY', 'ASN', 'ASP', 'GLN', 'GLU', 'SER', 'TYR', 'TRP', 'VAL', 'ILE', 'LEU', 'CYS']
dictValuesRes = {'ALA': 'A', 'LYS': 'K', 'ARG': 'R', 'HIS':'H', 'PHE':'F', 'THR':'T', 'PRO':'P', 'MET':'M', 'GLY':'G', 'ASN':'N', 'ASP':'D', 'GLN':'Q', 'GLU':'E', 'SER':'S', 'TYR':'Y', 'TRP':'W', 'VAL':'V', 'ILE':'I', 'LEU':'L', 'CYS':'C'}

parser = PDBParser()#creamos un parse de pdb
structure = parser.get_structure(codePDB, namePDB)#trabajamos con la proteina cuyo archivo es 1AQ2.pdb

arrayMutations = []

for model in structure:
    for chain in model:
        for residue in chain:
            if residue.resname in resValues:

                #formamos todas las posibles mutaciones...
                for mutation in resValues:
                    if mutation != residue.resname:
                        line = "%s %s%d%s" % (chain.id, dictValuesRes[residue.resname], residue.id[1], dictValuesRes[mutation])
                        arrayMutations.append(line)

#generamos el archivo con la salida correspondiente
fileOpen = open("outputMutations.txt" , 'w')
for line in arrayMutations:
    fileOpen.write(line+"\n")
fileOpen.close()
