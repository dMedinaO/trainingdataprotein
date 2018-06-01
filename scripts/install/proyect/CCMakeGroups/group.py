'''
clase que permite representar la informacion de un grupo, esta clase contiene informacion sobre sus atributos,
en forma de vectores, la atributo clase al cual pertenece, ademas de valores como el centroide, los maximos y minimos de
distancias dentro de su radio y a su vez la informacion correspondiente a la data de interes con respecto a distancias y variables
hacia otros grupos...
'''

from proyect.CCMakeGroups import processGroupOptions

class groupDescription(object):

    def __init__(self, name, ListVector, ListClass):

        #instancia al objeto de calculos...
        self.processOptionObject = processGroupOptions.processOption()
        self.name = name
        self.ListVector = ListVector
        self.ListClass = ListClass

    #metodo que permite procesar las diversas opciones del grupo...
    def processAttributesGroup(self):

        self.centroide = self.processOptionObject.calculateCentroide(self.ListVector)#calculamos el centroide
        self.maxDist, self.minDist = self.processOptionObject.calculateMaxMinDistanceToCentroide(self.ListVector, self.centroide)#calculamos  las distancias al centroide
