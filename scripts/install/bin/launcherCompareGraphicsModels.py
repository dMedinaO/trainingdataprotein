'''
script que permite hacer la comparacion de los modelos de manera grafica, permite hacer graficos por cada modelo y la comparacion de estos con respecto a los restantes grupos de interes...
'''

import sys
from proyect.CCModels import createBarChartModelsCompare

pathInput = sys.argv[1]
groups = ['A', 'B', 'C', 'F', 'H', 'M', 'N', 'O', 'P', 'T', 'U']
#groups = ['1', '2', '3', '4', '5', '6', '7', '8']

#formamos el objeto...
for group in groups:
    #formamos el path...
    print "Create bar charts to grpup ", group
    pathData = "%s%s_Attribute/training/crossValidation/" % (pathInput, group)
    barCharts = createBarChartModelsCompare.barChartModels(pathData, pathData, group)
    barCharts.readDocuments()
    barCharts.makeGraphsByModel()
