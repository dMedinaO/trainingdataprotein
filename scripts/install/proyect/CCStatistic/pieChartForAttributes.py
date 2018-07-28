'''
clase con la responsabilidad de generar los pie charts para los atributos con distribucion discreta, por cada uno de los atributos,
genera un pie chart...
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class pieChart(object):

    def __init__(self, dataSet, pathOutput):

        self.dataSet = dataSet
        self.pathOutput = pathOutput
        self.ListFeatures = ['AAWt','AAMt', 'Sstruct', 'ShbondsW', 'ShbondsM', 'Result', 'Positiontype', 'Clinical']

    #hacemos el procesamiento de la informacion...
    def processInformation(self):

        dataInput = pd.read_csv(self.dataSet)

        for key in self.ListFeatures:
            plt.figure()
            title = "Pie Chart for attribute %s" % key
            nameFig = "%spieChart_%s.svg" % (self.pathOutput, key)
            print "process pie chart to feature: ", key
            datas = self.getValuesCountFeature(dataInput[key])
            df = pd.DataFrame(datas[1], index=datas[0], columns=[key])
            plotData = df.plot(kind='pie', subplots=True, figsize=(10, 10), legend=False, style='ticks', colormap='Paired')
            plt.title(title, fontsize=18)
            plt.savefig(nameFig)

    #hacemos el procesamiento de la informacion para generar los barchart...
    def processInformationBC(self, pathValues):

        dataInput = pd.read_csv(self.dataSet)

        for key in self.ListFeatures:
            plt.figure()
            title = "Bar Chart for attribute %s" % key
            nameFig = "%sbarChart_%s.svg" % (pathValues, key)
            print "process barchart chart to feature: ", key
            datas = self.getValuesCountFeature(dataInput[key])
            df = pd.DataFrame(datas[1], index=datas[0], columns=[key])
            plotData = df.plot(kind='bar', subplots=True, figsize=(10, 10), legend=False, style='default', colormap='Paired', grid=False,rot=45)
            plt.title(title, fontsize=18)
            plt.savefig(nameFig)

    #obtenemos los valores de los atributos en forma de conteo...
    def getValuesCountFeature(self, listFeature):

        listUnique = list(set(listFeature))
        index = listUnique
        counts = []

        for i in range(len(index)):
            cont=0
            for values in listFeature:
                if index[i] == values:
                    cont+=1
            counts.append(cont)

        print index
        print counts
        return index, counts
