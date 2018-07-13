'''
clase que permite representar a un modelo, con sus parametros, descripcion, grupo al que pertenece y otros atributos de interes...
'''

class modelData(object):

    def __init__(self, algorithm, description, validation, accuracy, group, iterator):

        self.algorithm = algorithm
        self.description = description
        self.validation = validation
        self.accuracy = accuracy
        self.group = group
        self.iterator = iterator
