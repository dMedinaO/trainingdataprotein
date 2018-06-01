'''
clase que permite representar la distancia entre los grupos...
'''

from proyect.CCMakeGroups import processGroupOptions

class distGroupData(object):

    def __init__(self, groupObjective, groupCompare):

        self.groupObjective = groupObjective
        self.groupCompare = groupCompare
        self.processOptionObject = processGroupOptions.processOption()

    def calculateDistData(self):

        #con respecto al centro...
        self.center_center = self.processOptionObject.calculateDistanceVectors(self.groupObjective.centroide, self.groupCompare.centroide)
        self.center_max = self.processOptionObject.calculateDistanceVectors(self.groupObjective.centroide, self.groupCompare.vectorMax)
        self.center_min = self.processOptionObject.calculateDistanceVectors(self.groupObjective.centroide, self.groupCompare.vectorMin)

        #con respecto al maximo...
        self.max_center = self.processOptionObject.calculateDistanceVectors(self.groupObjective.vectorMax, self.groupCompare.centroide)
        self.max_max = self.processOptionObject.calculateDistanceVectors(self.groupObjective.vectorMax, self.groupCompare.vectorMax)
        self.max_min = self.processOptionObject.calculateDistanceVectors(self.groupObjective.vectorMax, self.groupCompare.vectorMin)

        #con respector al minimo...
        self.min_center = self.processOptionObject.calculateDistanceVectors(self.groupObjective.vectorMin, self.groupCompare.centroide)
        self.min_max = self.processOptionObject.calculateDistanceVectors(self.groupObjective.vectorMin, self.groupCompare.vectorMax)
        self.min_min = self.processOptionObject.calculateDistanceVectors(self.groupObjective.vectorMin, self.groupCompare.vectorMin)
