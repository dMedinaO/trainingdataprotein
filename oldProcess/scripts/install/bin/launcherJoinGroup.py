'''
script que tiene la responsabilidad de trabajar con los grupos y preparar la data
para hacer la union de los elementos con respecto a diversas caracteristicas...
'''

from proyect.CCMakeGroups import processGroup
from proyect.CCMakeGroups import processJoinGroup

import sys

#recibimos la informacion desde la terminal...
nameFile = sys.argv[1]
pathOutput = sys.argv[2]
splitter = sys.argv[3]

processGroupObject = processGroup.groupList(nameFile, pathOutput, splitter)
processGroupObject.processDistancesObject()
processGroupObject.exportDistancesToMatrix()
processGroupObject.applySilohuetteCoeficient()
processGroupObject.processAnovaTest()

#obtenemos los grupos que deben separarse...
processGroupObject.evaluateGroupJoin()

#procesamos los grupos para formar las uniones...
processJoinGroupObject = processJoinGroup.processInsertElement(processGroupObject.ListJoin, processGroupObject.ListValidGroup)
processJoinGroupObject.checkDistances()
