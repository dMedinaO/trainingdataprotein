'''
clase que tiene la responsabilidad de generar el box plot cada el set de datos, solo considera los atributos con valores continuos,
aquellos atributos con valores discretos, se realiza piechart y barchart.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class boxPlotDataSet(object):

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
        #por cada key, formamos un data frame...
        index=0
        feature1 = pd.DataFrame({ 'Features' : np.repeat('SaccW',len(dataInput['SaccW'])), 'value': self.getValuesToDF('SaccW', dataInput) })
        feature2 = pd.DataFrame({ 'Features' : np.repeat('SaccM',len(dataInput['SaccM'])), 'value': self.getValuesToDF('SaccM', dataInput) })
        feature3 = pd.DataFrame({ 'Features' : np.repeat('yDDG',len(dataInput['yDDG'])), 'value': self.getValuesToDF('yDDG', dataInput) })
        feature4 = pd.DataFrame({ 'Features' : np.repeat('ProteinPropens',len(dataInput['ProteinPropens'])), 'value': self.getValuesToDF('ProteinPropens', dataInput) })
        feature5 = pd.DataFrame({ 'Features' : np.repeat('Positionaccept',len(dataInput['Positionaccept'])), 'value': self.getValuesToDF('Positionaccept', dataInput) })
        feature6 = pd.DataFrame({ 'Features' : np.repeat('MOSST',len(dataInput['MOSST'])), 'value': self.getValuesToDF('MOSST', dataInput) })
        feature7 = pd.DataFrame({ 'Features' : np.repeat('Functionalrelevancefunction',len(dataInput['Functionalrelevancefunction'])), 'value': self.getValuesToDF('Functionalrelevancefunction', dataInput) })

        df = feature1.append(feature2).append(feature3).append(feature4).append(feature5).append(feature6).append(feature7)

        #creamos el box plot...
        plt.figure(figsize=(15,15))
        sns.set(color_codes=True)
        sns.set(style="ticks")
        sns.plt.title('boxPlot for features with Normaliced Values', fontsize=18)
        sns_plot = sns.boxplot(x='Features', y='value', data=df)
        plt.xticks(rotation=45)
        exportFile = self.pathOutput+"/boxPlot.svg"
        sns_plot.figure.savefig(exportFile)
