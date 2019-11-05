'''
script que permite adicionar la clase al set de datos generado mediante splitter clustering dirigido...
'''

from proyect.CCSplitter import addClassToGroup
import sys

dataSetG = sys.argv[2]
dataSetO = sys.argv[1]
pathOutput = sys.argv[3]
nameGroup = sys.argv[4]

addValues = addClassToGroup.addClass(dataSetO, dataSetG, pathOutput)
addValues.processDataInformation(nameGroup)
