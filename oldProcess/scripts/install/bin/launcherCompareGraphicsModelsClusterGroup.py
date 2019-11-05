'''
script que permite hacer la comparacion de los modelos de manera grafica, permite hacer graficos por cada modelo y la comparacion de estos con respecto a los restantes grupos de interes...
'''

import sys
from proyect.CCModels import createBarChartModelsCompareClusterRec

pathInput = sys.argv[1]
groups = ['grupo7']
#groups = ['1', '2', '3', '4', '5', '6', '7', '8']

#formamos el objeto...
for group in groups:
    #formamos el path...
    print "Create bar charts to grpup ", group
    pathData = "%s%s/training/crossValidation/tn/" % (pathInput, group)
    barCharts = createBarChartModelsCompareClusterRec.barChartModels(pathData, pathData, group)
    barCharts.readDocuments()
    barCharts.makeGraphsByModel()
