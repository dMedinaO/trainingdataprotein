'''
script que permite la creacion de nuevos set de datos aleatorios con la misma cantidad de elementos
y los mismos grupos, con el fin de poder determinar si las performance obtenidas son valores cualquiera
o tienen algun significado por detras...
'''

from proyect.CCMakeGroups import makeRandomGroup
from proyect.CCProcesFile import procesFile
import pandas as pd
import sys
import subprocess

#las entradas son el csv con la informacion de los grupos, la matriz de datos, y el path de salida...
nameFileGroup = sys.argv[1]
pathOutput = sys.argv[2]
nameMatrix = sys.argv[3]
iterations = int(sys.argv[4])

#hacemos la lectura del archivo de grupos...
df = pd.read_csv(nameFileGroup, sep=',')

#creamos un diccionario con el csv...
dictGroup = {}
for i in range(len(df['grupo'])):
    dictGroup.update({df['grupo'][i]:df['integrantes'][i]})

#trabajamos con la matriz general y la procesamos...
process = procesFile.processDataSet(nameMatrix, pathOutput, ',')
process.processMatrixData()#procesamos la matriz...

for i in range(iterations):

    #creamos un directorio segun la iteracion...
    dirCreate=pathOutput+"iteration_%d/" % (i+1)
    command = "mkdir -p %s" % dirCreate
    subprocess.call(command, shell=True)
    groupRandom = makeRandomGroup.makeGroup(dictGroup, process.matrixData, process.header, dirCreate)
    
