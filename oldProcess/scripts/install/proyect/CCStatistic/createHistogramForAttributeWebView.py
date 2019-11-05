'''
clase con la responsabilidad de recibir una lista y generar el archivo js para crear el histograma...
Nota: el js que se genera, solo contiene las variables...
'''

class createHistograma(object):

    def __init__(self, dataExport, nameFileExport, title):

        self.dataExport = dataExport
        self.nameFileExport = nameFileExport
        self.title = title

    #metodo que permite pasar la lista a una cadena de texto...
    def transformDataExport(self):

        self.dataLine = "var data = ["

        for element in self.dataExport:
            self.dataLine= "%s%f," % (self.dataLine, float(element))

        self.dataLine=self.dataLine[:-1]
        self.dataLine=self.dataLine+"];"

    #metodo que permite crea el archivo de salida...
    def createFile(self):

        self.transformDataExport()
        titleData = "var title = '%s';" % self.title
        fileOpen = open(self.nameFileExport, 'w')

        fileOpen.write(self.dataLine+"\n")
        fileOpen.write(titleData+"\n")
        fileOpen.close()
