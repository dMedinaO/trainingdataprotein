'''
clase que permite representar un componente de performance para un grupo cualquiera...
'''

class performanceGroup(object):

    def __init__(self, groupNumber, accuracy, r_call, precission):

        self.groupNumber = groupNumber
        self.accuracy = accuracy
        self.r_call = r_call
        self.precission = precission
