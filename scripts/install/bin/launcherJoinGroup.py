'''
script que tiene la responsabilidad de trabajar con los grupos y preparar la data
para hacer la union de los elementos con respecto a diversas caracteristicas...
'''

from proyect.CCMakeGroups import generateSplitterGroup
import sys

#recibimos la informacion desde la terminal...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]
splitter = sys.argv[3]

splitterObject = generateSplitterGroup.createGroupSplitter(nameFile, pathOutput, splitter)
splitterObject.processData()
