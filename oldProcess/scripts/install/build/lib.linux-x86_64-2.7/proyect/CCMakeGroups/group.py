'''
clase que permite representar la informacion de un grupo, esta clase contiene informacion sobre sus atributos,
en forma de vectores, la atributo clase al cual pertenece, ademas de valores como el centroide, los maximos y minimos de
distancias dentro de su radio y a su vez la informacion correspondiente a la data de interes con respecto a distancias y variables
hacia otros grupos...
'''

from proyect.CCMakeGroups import processGroupOptions
from proyect.CCMakeGroups import descriptionDistanceGroups

class groupDescription(object):

    def __init__(self, name, ListVector, ListClass):

        #instancia al objeto de calculos...
        self.processOptionObject = processGroupOptions.processOption()
        self.name = name
        self.ListVector = ListVector
        self.ListClass = ListClass
        self.transformData()
        self.dataDistances = {}

    #metodo que permite mostrar las distancias de un grupo con el resto...
    def showDistancesForGroup(self):

        print "Distances for group: ", self.name
        for key in self.dataDistances:
            print "---------------------------------"
            print "distancia con grupo ", key
            print self.dataDistances[key].max_max
            print "---------------------------------"
    #metodo que permite hacer la transformacion de datos...
    def transformData(self):
        for i in range(len(self.ListVector)):
            for j in range(len(self.ListVector[i])):
                self.ListVector[i][j] = float(self.ListVector[i][j])
    #metodo que permite procesar las diversas opciones del grupo...
    def processAttributesGroup(self):

        self.centroide = self.processOptionObject.calculateCentroide(self.ListVector)#calculamos el centroide
        self.maxDist, self.minDist, indexMax, indexMin = self.processOptionObject.calculateMaxMinDistanceToCentroide(self.ListVector, self.centroide)#calculamos  las distancias al centroide

        self.vectorMax = self.ListVector[indexMax]
        self.vectorMin = self.ListVector[indexMin]
