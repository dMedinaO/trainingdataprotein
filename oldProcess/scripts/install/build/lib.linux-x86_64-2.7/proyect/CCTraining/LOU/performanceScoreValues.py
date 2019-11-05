from proyect.CCTraining.LOU import performance

class performanceScoreValues(object):

    def __init__(self, algorithm, description, validation, performance):

        self.algorithm = algorithm
        self.description = description
        self.validation = validation
        self.performance = performance
