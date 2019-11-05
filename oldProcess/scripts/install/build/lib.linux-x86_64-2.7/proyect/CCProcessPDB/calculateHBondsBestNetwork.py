'''
clase que tiene la responsabilidad de procesar la informacion con respecto a la data del valor de los elementos
de salida de whatif dado el resultado de la estimacion de puentes de hidrogeno a traves de campos de fuerza
Recibe la lista de residuos y retorna el archivo de la matriz con la informacion procesada...
'''

from proyect.CCProcessPDB import processPDB
from proyect.CCProcesFile import document

class hBondsNetwork(object):

    def __init__(self, processPDBObject, responseWhatIf, nameMatrixFile, pathOutput):

        self.processPDBObject = processPDBObject
        self.responseWhatIf = responseWhatIf
        self.matrixData = self.processPDBObject.generateMatrixOnes()
        self.pathOutput = pathOutput
        self.nameMatrixFile = nameMatrixFile
        print self.matrixData

    #metodo que permite hacer la busqueda del index de la columna...
    def searchIndex(self, res, header):

        index = -1

        for i in range(len(header)):
            if header[i] == res:
                index= i+1
        return index

    #metodo que permite hacer la busqueda de valores en el diccionario, la key permite evaluar si busco aceptor o donor...
    def searchHBondsForResidue(self, residue, dictResponseFull, key):

        listResiduesInHBond = []
        for element in dictResponseFull:
            if element[key] == residue:
                listResiduesInHBond.append(element)
        return listResiduesInHBond

    #metodo que permite obtener la informacion del whatif
    def processResponseWI(self):
        dataResponse = document.document(self.responseWhatIf, '').readNormalDocument()

        self.HBondsWhitOutH2O = []#lista que contendra todos los elementos que no consideren enlaces de hidrogeno con residuos de agua...

        for element in dataResponse:
            splitElement = element.split(" ")
            dataSinSpace = []
            for value in splitElement:
                if value != '':
                    dataSinSpace.append(value)
            #quitamos los atomos de agua...
            if 'HOH' not in element:
                self.HBondsWhitOutH2O.append(dataSinSpace)

    #metodo que permite generar el diccionario con la informacion...
    def createDictValues(self):

        self.dictResponseFull = []

        for element in self.HBondsWhitOutH2O:
            dictValue = {}
            nameA = "%s-%s-%s" % (element[1], element[3], element[4][1])
            nameD = "%s-%s-%s" % (element[8], element[10], element[11][1])
            vscore = float(element[16])
            DA = float(element[18])
            DHA = float(element[20])

            dictValue.update({'nameA': nameA})
            dictValue.update({'nameD': nameD})
            dictValue.update({'vscore': vscore})
            dictValue.update({'DA': DA})
            dictValue.update({'DHA': DHA})
            self.dictResponseFull.append(dictValue)

    #procesamiento de los puentes de hidrogeno...
    def processHBondsSearch(self):

        for element in self.processPDBObject.header[1:]:
            listA = self.searchHBondsForResidue(element, self.dictResponseFull, 'nameA')
            listD = self.searchHBondsForResidue(element, self.dictResponseFull, 'nameD')
            if len(listA) >0:
                #obtenemos los valores asociados a los elementos encontrados...
                for res in listA:
                    nameRes = res['nameD']
                    valueData = res['vscore']
                    print valueData
                    indexPos = self.searchIndex(nameRes, self.processPDBObject.header[1:])
                    indexRow = self.searchIndex(element, self.processPDBObject.header[1:]) -1
                    if indexPos != -1 and indexRow != -1:
                        self.matrixData[indexRow][indexPos] += valueData
            if len(listD) >0:
                #obtenemos los valores asociados a los elementos encontrados...
                for res in listD:
                    nameRes = res['nameA']
                    valueData = res['vscore']
                    print valueData
                    indexPos = self.searchIndex(nameRes, self.processPDBObject.header[1:])
                    indexRow = self.searchIndex(element, self.processPDBObject.header[1:])-1
                    if indexPos != -1 and indexRow != -1:
                        self.matrixData[indexRow][indexPos] += valueData

    #exportamos el documento...
    def exportDocument(self):

        document.document(self.nameMatrixFile, self.pathOutput).createExportFileWithPandas(self.matrixData, self.processPDBObject.header)
