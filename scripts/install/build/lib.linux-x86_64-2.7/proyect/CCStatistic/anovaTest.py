'''
clase que permite ejecutar el test de anova para dos grupos y asi evaluar si estos son distintos o no,
mediante un criterio estadistico, esto facilita el trabajo de la comparacion de elementos, ademas para casos
posteriores, permite la evaluacion de la insercion de un elemento a un grupo...
'''
from sklearn import preprocessing
import rpy2.robjects as robjects
import scipy.stats as stats
import numpy as np

class anovaTest(object):

    def __init__(self, matrixObjetive):

        self.matrixObjetive = matrixObjetive
        self.matrixObjetive = preprocessing.normalize(self.matrixObjetive, norm='l2')
    #metodo que permite estimar el valor de anova para los grupos obtenidos...
    def anovaTestValue(self):

        self.processMeanAttribute()
        self.nValue = len(self.matrixObjetive)*len(self.matrixObjetive[0])
        self.meanGeneral = np.mean(self.ListMeanAttribute)
        self.calculateSumaCuadradosTotales()
        self.calculateSumaCuadradosTratamientos()
        self.calculateSumaCuadradosError()
        self.cmt=self.sct/(self.nValue-1)
        self.cmtr = self.sctr/(len(self.matrixObjetive[0])-1)
        self.cme = self.sce/(self.nValue - len(self.matrixObjetive[0]))

        self.valueF = self.cmtr/self.cme

        print "Fisher: ", self.valueF
        print "NL Numerador: ", len(self.matrixObjetive[0])-1
        print "NL Denominador: ", self.nValue - len(self.matrixObjetive[0])

        self.evaluateFValue(len(self.matrixObjetive[0])-1, self.nValue - len(self.matrixObjetive[0]))
        print self.isAccepted
    #metodo que permite evaluar si el valor F es significativo...
    def evaluateFValue(self, gl1, gl2):

        data = robjects.r["qf"](0.01, gl1, gl2)
        print "Valor Tabla: ", data[0]
        if self.valueF < data:
            self.isAccepted=True
        else:
            self.isAccepted=False

    #metodo que permite calcular las medias de los atributos...
    def processMeanAttribute(self):

        self.ListMeanAttribute = []
        for i in range(len(self.matrixObjetive[0])):
            rowAttribute = []
            for j in range (len(self.matrixObjetive)):
                rowAttribute.append(self.matrixObjetive[j][i])

            self.ListMeanAttribute.append(np.mean(rowAttribute))

    #metodo que permite sumar de cuadrados de error...
    def calculateSumaCuadradosError(self):

        self.sce=0

        for i in range(len(self.matrixObjetive[0])):
            for j in range(len(self.matrixObjetive)):
                dif = (self.matrixObjetive[j][i] - self.ListMeanAttribute[i])**2
                self.sce+=dif

    #metodo que permite calcular la suma de cuadrados de tratamientos
    def calculateSumaCuadradosTratamientos(self):
        self.sctr =0

        for element in self.ListMeanAttribute:
            value = (element-self.meanGeneral)**2
            self.sctr+=value

    #metodo que permite calcular las sumas de cuadrados totales
    def calculateSumaCuadradosTotales(self):

        self.sct=0
        for i in range(len(self.matrixObjetive)):
            for j in range(len(self.matrixObjetive[i])):
                value = (self.matrixObjetive[i][j]-self.meanGeneral)**2
                self.sct+=value
