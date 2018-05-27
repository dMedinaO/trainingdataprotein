'''
clase que permite crear grupos de elementos con respecto a un clustering generado,
el objetivo general, es generar nuevos set de datos, con respecto a la data que estos poseen
y en base a su valor de coeficiente de siluetas.

Se aplicaran diversos algoritmos y se seleccionaran aquellos en los cuales se cumplan las siguientes condiciones:

1. El valor de coeficiente de siluetas debe ser mayor a 0
2. El numero de integrantes por grupo, para cada grupo, debe ser mayor a 30
'''

from proyect.CCProcesFile import document #para hacer la instancia a la clase de lectura y escritura de archivos...

class clusteringDataSet(object):

    def __init__(self, nameFile, pathOuput):#constructor de la clase...
        self.nameFile = nameFile
        self.pathOuput = pathOuput
