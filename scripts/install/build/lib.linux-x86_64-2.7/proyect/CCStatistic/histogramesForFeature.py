'''
clase que tiene la responsabilidad de generar el box plot cada el set de datos, solo considera los atributos con valores continuos,
aquellos atributos con valores discretos, se realiza piechart y barchart.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class histogrameForDataSet(object):

    def __init__(self, dataSet, pathOutput):

        self.dataSet = dataSet
        self.pathOutput = pathOutput
        self.keys = ['SaccW', 'SaccM', 'yDDG', 'ProteinPropens', 'Positionaccept', 'MOSST', 'Functionalrelevancefunction']#keys con valores continuos...

    def getValuesToDF(self, key, df):

        values = []
        for element in df[key]:
            values.append(element)
        return values

    #metodo que permite leer el set de datos y almacenarlo como diccionario segun las caracteristicas de los mismos valores...
    def readDataSet(self):

        dataInput = pd.read_csv(self.dataSet)

        for key in self.keys:
            print "Process feature: ", key
            nameExport = "%shistogram_%s.svg" % (self.pathOutput, key)
            title = "Histograme for Feature %s" % key
            self.createHistogram(dataInput[key], nameExport, key, title)

    #metodo que permite generar el histograma...
    def createHistogram(self, listData, nameExport, label, title):
        plt.figure()
        sns.set(color_codes=True)
        sns.set(style="ticks")
        sns_plot = sns.distplot( listData , color="red", label=label, kde=False, rug=True)
        sns.plt.legend()
        sns.plt.title(title)
        sns_plot.figure.savefig(nameExport)
