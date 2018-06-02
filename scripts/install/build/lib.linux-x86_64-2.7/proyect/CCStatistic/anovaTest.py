'''
clase que permite ejecutar el test de anova para dos grupos y asi evaluar si estos son distintos o no,
mediante un criterio estadistico, esto facilita el trabajo de la comparacion de elementos, ademas para casos
posteriores, permite la evaluacion de la insercion de un elemento a un grupo...
'''

import scipy.stats as stats

class anovaTest(object):

    def __init__(self, matrixObjetive):

        self.matrixObjetive = matrixObjetive

    #metodo que permite estimar el valor de anova para los grupos obtenidos...
    def anovaTestValue(self):
        print self.matrixObjetive
        data = stats.f_oneway(self.matrixObjetive)
        print data
