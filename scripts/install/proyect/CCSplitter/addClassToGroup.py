'''
clase con la responsabilidad de agregar el atributo clase al set de datos de interes...
'''

from proyect.CCProcesFile import document

class addClass(object):

    def __init__(self, dataSetName, groupProcess, pathOutput):

        self.dataSetName = dataSetName
        self.groupProcess = groupProcess
        self.pathOutput = pathOutput


    #metodo que permite hacer la lectura del set de datos y retorna el array con la informacion...
    def readDataSet(self, nameFile):

        dataValues = []
        fileOpen = open(nameFile, 'r')
        line = fileOpen.readline()

        while line:
            dataValues.append(line.replace("\n", ""))
            line = fileOpen.readline()
        fileOpen.close()

        return dataValues

    #metodo que permite procesar la informacion
    def processDataInformation(self, nameGroup):

        print "read data set objects"
        dataSetO = self.readDataSet(self.dataSetName)
        dataSetG = self.readDataSet(self.groupProcess)
        #trabajamos con el header...
        header = dataSetO[0].split(',')
        dataSetG = dataSetG[1:]
        dataSetO = dataSetO[1:]

        matrixData = []

        #por cada ejemplo en el set de datos del grupo lo buscamos en el original y obtenemos la clase...
        for example in dataSetG:
            row = []
            classData = -1
            for exampleO in dataSetO:
                if example in exampleO:
                    classData = exampleO.split(',')[-1]
                    break
            exampleList = example.split(',')
            for value in exampleList:
                row.append(float(value))
            row.append(int(classData))
            matrixData.append(row)

        #exportamos la matriz...
        document.document(nameGroup, self.pathOutput).createExportFileWithPandas(matrixData, header)
