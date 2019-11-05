'''
clase con la responsabilidad de generar los calculos de energia de enlace covalente entre los residuos...
las formulas son obtenidas desde paper en bibliografia, se hace la lectura de los enlaces phi y psi mediante
el archivo json creado previamente, y crea la matriz con la informacion, en general la data estara asociada
a las diagonales existentes...
'''

from Bio.PDB.PDBParser import PDBParser
import json
import Bio.PDB
import numpy as np
import math
from proyect.CCProcessPDB import parserDegreePhiPsi
from proyect.CCProcessPDB import rangeTableForELOC3
from proyect.CCProcesFile import document

class covalenteEnergyProcess(object):

    def __init__(self, processPDBObject, parserDegreePhiPsiValues, nameMatrixFile, pathOutput):

        self.processPDBObject = processPDBObject#objeto!!!
        self.parserDegreePhiPsiValues = parserDegreePhiPsiValues#objeto!!!
        self.nameMatrixFile = nameMatrixFile
        self.pathOutput = pathOutput
        self.matrixData = self.processPDBObject.generateMatrixOnes()#generamos la matriz de 0...
        self.dictELOC={}#diccionario para las energias que se obtienen en el primer componente...
        self.createTableEloc3()

    #metodo que permite crear la tabla de los valores para el eloc3...
    def createTableEloc3(self):

        self.elocTableValue = []
        #row1
        self.elocTableValue.append(rangeTableForELOC3.elocTable('SER', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('CYS', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('THR', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('VAL', 'I', 'X1', 0.6, 3))
        #row 2
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ILE', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ILE', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('LEU', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('LEU', 'I', 'X2', 0.6, 3))
        #row3
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ASP', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ASP', 'IV', 'X2', -0.4, 2))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ASN', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ASN', 'IV', 'X2', -0.4, 2))
        #row4
        self.elocTableValue.append(rangeTableForELOC3.elocTable('HIS', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('HIS', 'III', 'X2', 0.4, 2))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('PHE', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('PHE', 'III', 'X2', 0.4, 2))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('TYR', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('TYR', 'III', 'X2', 0.4, 2))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('TRP', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('TRP', 'III', 'X2', 0.4, 2))
        #row5
        self.elocTableValue.append(rangeTableForELOC3.elocTable('MET', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('MET', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('MET', 'II', 'X3', 0.3, 3))
        #row6
        self.elocTableValue.append(rangeTableForELOC3.elocTable('GLU', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('GLU', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('GLU', 'IV', 'X3', -0.4, 2))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('GLN', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('GLN', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('GLN', 'IV', 'X3', -0.4, 2))
        #row7
        self.elocTableValue.append(rangeTableForELOC3.elocTable('LYS', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('LYS', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('LYS', 'I', 'X3', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('LYS', 'I', 'X4', 0.6, 3))
        #row8
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ARG', 'I', 'X1', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ARG', 'I', 'X2', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ARG', 'I', 'X3', 0.6, 3))
        self.elocTableValue.append(rangeTableForELOC3.elocTable('ARG', 'III', 'X4', 0.4, 3))

    #metodo que permite agregar a la lista los atomos que son de interes para los calculos...
    def selectedAtom(self, atomList):
        atomSelected = []

        for element in atomList:
            if 'H' in element.name:
                atomSelected.append(element)
            if element.name in ['CA', 'CB', 'N', 'O']:
                atomSelected.append(element)
        return atomSelected

    #metodo que permite obtener el valor de la carga del atomo...
    def getValueCharge(self, atom):

        if 'C' in atom.name or 'O' in atom.name:
            return 0.42
        else:
            if 'N' in atom.name or 'H' in atom.name:
                return 0.20
            else:#por si fuera otro atomo..., es solo del back bone...
                return 0

    #funcion que permite calcular las distancias de los atomos en los residuos...
    def getDistanceAtomsResidues(self, atomResidueA, atomResidueB, componenteA, componentB):

        cont=0
        sumData=0
        for atom in atomResidueA:
            for atomB in atomResidueB:
                if componenteA in atom.name and componentB in atomB.name:
                    cont+=1
                    sumData+=(atom-atomB)

        return sumData/cont

    #funcion que permite poder obtener los atomos de un residuo...
    def getAtomResidue(self, residue):

        atomResidue = []
        for atom in residue:
            atomResidue.append(atom)
        return atomResidue

    #funcion que permite evaluar el valor de la funcion mu
    def evaluatedMUi(self, residueA, residueB):

        #obtenemos los atomos de cada residuo...
        atomResidueA = self.getAtomResidue(residueA)
        atomResidueB = self.getAtomResidue(residueB)

        ListComponent = []
        ListComponent.append(self.getDistanceAtomsResidues(atomResidueA, atomResidueB, 'H', 'N'))
        ListComponent.append(self.getDistanceAtomsResidues(atomResidueA, atomResidueB, 'N', 'H'))
        thirdComponent= self.getDistanceAtomsResidues(atomResidueA, atomResidueB, 'H', 'H')
        return min(ListComponent)-thirdComponent

    #funcion que permite evaluar el valor de la funcion nu...
    def evaluatedNu(self, residueA, residueB):

        #obtenemos los atomos de cada residuo...
        atomResidueA = self.getAtomResidue(residueA)
        atomResidueB = self.getAtomResidue(residueB)

        ListComponent = []
        ListComponent.append(self.getDistanceAtomsResidues(atomResidueA, atomResidueB, 'O', 'C'))
        ListComponent.append(self.getDistanceAtomsResidues(atomResidueA, atomResidueB, 'C', 'O'))
        thirdComponent= self.getDistanceAtomsResidues(atomResidueA, atomResidueB, 'O', 'O')
        return min(ListComponent)-thirdComponent

    #funcion que permite evaluar la funcion F
    def evaluateFFunction(self, component):

        ListData = [0, np.tanh(component)]
        return min(ListData)

    #funcion que permite evaluar el calculo de los cosenos de la gly...
    def processValuesPhiPsi(self, elementValue):

        #obtenemos los valores del elemento
        value = self.getFullID(elementValue.get_full_id(), elementValue)
        dataElement = value.split("-")#Res, Pos, Chain
        psiDegree = 0
        valueForm = 0
        #buscamos en el diccionario la informacion...
        for data in self.parserDegreePhiPsiValues.dictResponse:

            if data['residue'] == dataElement[0]:
                if data['chain'] == dataElement[2]:
                    if data['idResidue'] == dataElement[1]:
                        psiDegree = data['psiDegree']
                        break
        valueForm = math.cos(psiDegree) + 2*math.cos(2*psiDegree)
        return valueForm

    #funcion que permite calcular el valor de ELOC(1), el cual tiene que ver con el primer termino de la componente de energia...
    def calculateELOCA(self, residuesInBond):

        #nota, en la lista, siempre el residuo de interes estara en la primera posicion del array...
        sumValueData = 0
        for residue in residuesInBond:
            atomList = []
            for atom in residue:
                atomList.append(atom)
            atomSelected = self.selectedAtom(atomList)
            for atom in atomSelected:
                for atomV in atomSelected:
                    if atom != atomV:
                        qi = self.getValueCharge(atom)
                        qj = self.getValueCharge(atomV)
                        if qj==0 or qi==0:
                            pass
                        else:
                            data = (qi*qj) / (atom-atomV)
                            sumValueData +=data
        return sumValueData

    #funcion que permite calcular el valor de ELOC2...
    def calculateELOCB(self, residueA, residueB):

        total = 0
        euValue = 0
        if 'GLY' not in residueA.resname:
            if 'GLY' not in residueB.resname:
                valueFMu = self.evaluateFFunction(self.evaluatedMUi(residueA, residueB))
                valueFNu = self.evaluateFFunction(self.evaluatedNu(residueA, residueB))
                total = valueFMu+valueFNu
                euValue = 1.2
            else:
                gly1 = self.processValuesPhiPsi(residueA)
                gly2 = self.processValuesPhiPsi(residueB)
                total = gly1+gly2
                euValue = -0.15
        else:
            gly1 = self.processValuesPhiPsi(residueA)
            gly2 = self.processValuesPhiPsi(residueB)
            glyTotal = -0.15*(gly1+gly2)
            total = gly1+gly2
            euValue = -0.15

        return total, euValue

    #funcion que permite evaluar los valores de ELOC3 para un residuo...
    def calculateELOCC(self, residueKey):

        total = 0

        for element in self.elocTableValue:
            if element.residue in residueKey:
                value = element.eloc*math.cos(element.ni)
                total+=value
        return total

    #metodo que permite trabajar con el full id...
    def getFullID(self, data, element):

        nameResidue = "%s-%d-%s" % (element.resname, int(data[3][1]), data[2])
        return nameResidue

    #metodo que permite hacer el procesamiento de los calculos para ELOC1...
    def processELOC1(self):

        for i in range(len(self.processPDBObject.ListResidues)-1):
            nameA = self.getFullID(self.processPDBObject.ListResidues[i].get_full_id(), self.processPDBObject.ListResidues[i])
            nameB = self.getFullID(self.processPDBObject.ListResidues[i+1].get_full_id(), self.processPDBObject.ListResidues[i+1])
            key = "%s:%s" % (nameA, nameB)
            valueEloc1 = self.calculateELOCA([self.processPDBObject.ListResidues[i], self.processPDBObject.ListResidues[i+1]])
            self.dictELOC.update({key:valueEloc1})
            print "%s : %f" % (key, valueEloc1)

    #metodo que permite hacer el procesamiento de los calculos para ELOC2...
    def processELOC2(self):

        #caso 1... el primer y segundo residuo...
        nameA = self.getFullID(self.processPDBObject.ListResidues[0].get_full_id(), self.processPDBObject.ListResidues[0])
        nameB = self.getFullID(self.processPDBObject.ListResidues[1].get_full_id(), self.processPDBObject.ListResidues[1])
        key = "%s:%s" % (nameA, nameB)

        #calculamos las funciones U y V...
        total, euValue = self.calculateELOCB(self.processPDBObject.ListResidues[2], self.processPDBObject.ListResidues[3])
        self.dictELOC[key] = self.dictELOC[key]+(total*euValue)

        #caso 2... el segundo y el tercer residuo...
        nameA = self.getFullID(self.processPDBObject.ListResidues[1].get_full_id(), self.processPDBObject.ListResidues[1])
        nameB = self.getFullID(self.processPDBObject.ListResidues[2].get_full_id(), self.processPDBObject.ListResidues[2])
        key = "%s:%s" % (nameA, nameB)

        #calculamos las funciones U y V...
        total, euValue = self.calculateELOCB(self.processPDBObject.ListResidues[3], self.processPDBObject.ListResidues[4])
        self.dictELOC[key] = self.dictELOC[key]+(total*euValue)

        #la opcion del ultimo peptido...
        nameA = self.getFullID(self.processPDBObject.ListResidues[-2].get_full_id(), self.processPDBObject.ListResidues[-2])
        nameB = self.getFullID(self.processPDBObject.ListResidues[-1].get_full_id(), self.processPDBObject.ListResidues[-1])
        key = "%s:%s" % (nameA, nameB)

        #calculamos las funciones U y V...
        total, euValue = self.calculateELOCB(self.processPDBObject.ListResidues[-4], self.processPDBObject.ListResidues[-3])
        self.dictELOC[key] = self.dictELOC[key]+(total*euValue)

        #las opciones del penultimo peptido...
        nameA = self.getFullID(self.processPDBObject.ListResidues[-3].get_full_id(), self.processPDBObject.ListResidues[-3])
        nameB = self.getFullID(self.processPDBObject.ListResidues[-2].get_full_id(), self.processPDBObject.ListResidues[-2])
        key = "%s:%s" % (nameA, nameB)

        #calculamos las funciones U y V...
        total, euValue = self.calculateELOCB(self.processPDBObject.ListResidues[-5], self.processPDBObject.ListResidues[-4])
        self.dictELOC[key] = self.dictELOC[key]+(total*euValue)

        #hacemos el resto de procesamiento de datos...
        for i in range(3,len(self.processPDBObject.ListResidues)-3):

            nameA = self.getFullID(self.processPDBObject.ListResidues[i].get_full_id(), self.processPDBObject.ListResidues[i])
            nameB = self.getFullID(self.processPDBObject.ListResidues[i+1].get_full_id(), self.processPDBObject.ListResidues[i+1])
            key = "%s:%s" % (nameA, nameB)

            #calculamos las funciones U y V...
            total, euValue = self.calculateELOCB(self.processPDBObject.ListResidues[i+2], self.processPDBObject.ListResidues[i+3])
            self.dictELOC[key] = self.dictELOC[key]+(total*euValue)

        for element in self.dictELOC:
            print element, ": ", self.dictELOC[element]

    #metodo que permite procesar los calculos de ELOC3...
    def processELOC3(self):

        for key in self.dictELOC:
            residues = key.split(":")#procesamos la key para obtener los dos residuos...
            totalA = self.calculateELOCC(residues[0])
            totalB = self.calculateELOCC(residues[1])
            total = totalA+totalB
            self.dictELOC[key]+=total
        for element in self.dictELOC:
            print element, ": ", self.dictELOC[element]

    #metodo que permite hacer la busqueda del index de la columna...
    def searchIndex(self, res, header):

        index = -1
        for i in range(len(header)):
            if header[i] == res:
                index= i
        return index

    #metodo que permite exportar el diccionario a la matriz...
    def exportMatrix(self):

        for key in self.dictELOC:
            print key
            residues = key.split(":")

            indexA = self.searchIndex(residues[0], self.processPDBObject.header[1:])
            indexB = self.searchIndex(residues[1], self.processPDBObject.header[1:])

            self.matrixData[indexA][indexB+1] = self.dictELOC[key]#completamos las filas
            self.matrixData[indexA+1][indexB] = self.dictELOC[key]#completamos las columnas
        document.document(self.nameMatrixFile, self.pathOutput).createExportFileWithPandas(self.matrixData, self.processPDBObject.header)
