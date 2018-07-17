'''
script que permite generar los line chart para cada distribucion con respecto a la informacion generada por los clasificadores y las medidas
de desempeno que se han generado.
'''

from proyect.CCStatistic import createMultipleLineChartForGSS
import sys

pathOutput = sys.argv[1]
pathInput = sys.argv[2]
numberGroups = int(sys.argv[3])

createMultipleLineChartForGSS.multipleLineChart(pathOutput, pathInput, numberGroups).makeGraphs()
