'''
script que permite realizar un conunto de analisis estadisticos a las variables de interes, generando un flujo de trabajo completo al set de datos recibido...
'''

from proyect.CCStatistic import boxPlotForDataSet, histogramesForFeature, pieChartForAttributes, createCorrelationMatrix
from proyect.CCStatistic import statisticalSummary

import sys
import subprocess

#recibimos las variables de entrada...
dataSet = sys.argv[1]
pathOutput = sys.argv[2]

print "process statisticalSummary"
statisticalSummary.statisticalSummary(dataSet, pathOutput).generateStatisticalSummary()

#creamos el directorio para el box plot...
print "process box plot"
command = "mkdir -p %sboxPlot" % pathOutput
subprocess.call(command, shell=True)

boxPlotO = boxPlotForDataSet.boxPlotDataSet(dataSet, pathOutput+"boxPlot")
boxPlotO.readDataSet()

print "process Histograme"
command = "mkdir -p %shistogram" % pathOutput
subprocess.call(command, shell=True)

histograms = histogramesForFeature.histogrameForDataSet(dataSet, pathOutput+"histogram/")
histograms.readDataSet()

print "process Pie Chart"
command = "mkdir -p %spiechart" % pathOutput
subprocess.call(command, shell=True)

pieCharts = pieChartForAttributes.pieChart(dataSet, pathOutput+"piechart/")
pieCharts.processInformation()

print "process Bar Chart"
command = "mkdir -p %sbarchart" % pathOutput
subprocess.call(command, shell=True)
pieCharts.processInformationBC(pathOutput+"barchart/")

print "process Correlation Matrix Data"
command = "mkdir -p %scorrelation" % pathOutput
subprocess.call(command, shell=True)
corr = createCorrelationMatrix.correlationMatrix(dataSet, pathOutput+"correlation/")
corr.createCorrelationMatrixData()
