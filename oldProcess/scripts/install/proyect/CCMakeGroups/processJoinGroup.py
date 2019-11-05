'''
clase que tiene la responsabilidad de recibir las listas de los grupos que deben ser agregadas
y las que no, trabaja con ellas y evalua las inserciones a los nuevos grupos.
'''

from proyect.CCMakeGroups import processGroupOptions

class processInsertElement(object):

    def __init__(self, groupsJoin, groupsValid):

        self.groupsJoin = groupsJoin
        self.groupsValid = groupsValid
        self.calcules = processGroupOptions.processOption()

    #metodo que permite procesar la distancia de un elemento a un grupo...
    def processDistanceElementToGroup(self, vectorA, group):

        distance = self.calcules.calculateDistanceVectors(vectorA, group.centroide)
        return distance

    #metodo que permite hacer el procesamiento de datos de distancia...
    def checkDistances(self):

        ListNotPossibleInsert = []
        for groupData in self.groupsJoin:
            print groupData
            print "Processed eelements in group: ", groupData.name

            for member in groupData.ListVector:#todos los vectores de un grupo...

                distancesToCentroidesGroup = {}#diccionario para las distancias...

                #calculamos la distancia con otros grupos que pueden unirse...
                for groupValid in self.groupsValid:
                    distancesToCentroidesGroup.update({groupValid.name: self.processDistanceElementToGroup(member, groupValid)})

                myDistanceOwnerCentroide = self.processDistanceElementToGroup(member, groupData)#calculamos la propia distancia a su centroide

                cont=0
                for data in distancesToCentroidesGroup:
                    if distancesToCentroidesGroup[data] <myDistanceOwnerCentroide:
                        cont+=1
                if cont==0:#no hay grupos para insertar...
                    ListNotPossibleInsert.append(member)
        print len(ListNotPossibleInsert)
