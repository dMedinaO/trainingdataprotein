'''
clase con la responsabilidad de parsear la informacion del archivo de grados phi y psi,
permite la lectura del archivo, procesamiento y obtencion de la informacion del mismo.
exporta el documento en formato json para su posterior ocupacion...
'''

from proyect.CCProcesFile import document
import json

class degreeValues(object):

    def __init__(self, nameInput, pathOutput):#constructor de la clase...
        self.nameInput = nameInput
        self.pathOutput = pathOutput
        self.data = document.document(nameInput, '').readNormalDocument()
        self.data = self.data[2:]

        self.processDegreeValues()
        self.exportDocumentProcess()

    #metodo que permite obtener el valor de los angulos phi y psi...
    def getValueDegrees(self, arraySplit):

        arrayData = []
        for element in arraySplit:
            if element != '':
                arrayData.append(element)
        return float(arrayData[5]), float(arrayData[6])
    #metodo que permite obtener el valor del id del residuo...
    def getIDResidue(self, arraySplit):

        arrayData = []
        for element in arraySplit:
            if element != '':
                arrayData.append(element)
        return int(arrayData[3])

    #metodo que permite obtener el valor del residuo...
    def getResidueValue(self, arraySplit):

        arrayData = []
        for element in arraySplit:
            if element != '':
                arrayData.append(element)
        return arrayData[1]
    #metodo que permite obtener el valor de la cadena...
    def getChainValue(self, arraySplit):
        chainValue = ""
        for element in arraySplit:
            if ')' in element:
                chainValue = element[1]
                break
        return chainValue

    #metodo que permite hacer el procesamiento de los angulos
    def processDegreeValues(self):

        self.dictResponse = []

        for dataElement in self.data:

            dictResidue = {}
            splitData = dataElement.split(" ")
            idResidue = self.getIDResidue(splitData)
            phiDegree, psiDegree = self.getValueDegrees(splitData)

            dictResidue.update({'chain': self.getChainValue(splitData)})
            dictResidue.update({'residue': self.getResidueValue(splitData)})
            dictResidue.update({'idResidue': self.getIDResidue(splitData)})
            dictResidue.update({'phiDegree': phiDegree})
            dictResidue.update({'psiDegree': psiDegree})

            self.dictResponse.append(dictResidue)

    #metodo que permite exportar el resultado...
    def exportDocumentProcess(self):

        nameOuput = "%soutputDegrees.json" % self.pathOutput
        with open(nameOuput, 'w') as outfile:
            json.dump(self.dictResponse, outfile)
