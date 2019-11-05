'''
clase que permite la lectura y escritura de archivos,
tiene los metodos necesarios para efectuar estas operaciones...
'''

import pandas as pd
import subprocess

class document(object):
    def __init__(self, nameFile, pathOutput):
        self.nameFile = nameFile
        self.pathOutput = pathOutput

    #metodo que permite una lectura normal de documento...
    def readNormalDocument(self):

        #comenzamos con la lectura del archivo...
        fileOpen = open(self.nameFile, 'r')
        data = []
        line = fileOpen.readline()

        while line:
            line = line.replace("\n", "")
            data.append(line)
            line = fileOpen.readline()
        fileOpen.close()

        return data

    #metodo que permite leer un archivo de texto...
    def readDocument(self):

        fileOpen = open(self.nameFile, 'r')
        line = fileOpen.readline()
        matrixData = []

        while line:
            line = line.replace("\n", "")
            matrixData.append(line)
            line = fileOpen.readline()
        fileOpen.close()

        return matrixData

    #metodo que permite leer una matriz...
    def readMatrix(self):

        fileOpen = open(self.nameFile, 'r')
        line = fileOpen.readline()
        matrixData = []

        while line:
            line = line.replace("\n", "")
            row = line.split(',')
            matrixData.append(row)
            line = fileOpen.readline()
        fileOpen.close()

        return matrixData


    #metodo que permite poder generar el archivo de salida...
    def createExportFileWithPandas(self, matrixData, header):
        fileExport = self.pathOutput+self.nameFile
        #hacemos que el archivo se exporte en csv mediante pandas
        df = pd.DataFrame(matrixData)
        df.to_csv(fileExport, sep=',',header=header, index=False)

    #metodo que permite crear un directorio...
    def createDir(self, nameDir):

        command = "mkdir -p %s" % (nameDir)
        subprocess.call(command, shell=True)
