'''
script que permite hacer las ejecuciones correspondietes para el calculo de los estadisticos de interes en las distribuciones correspondientes
'''

from proyect.CCStatistic import makeStatisticDistribution
import sys

#recibimos los datos de entrada...
group = int(sys.argv[1])
pathOutput = sys.argv[2]
pathFile = sys.argv[3]

#hacemos la instancia...
statistic = makeStatisticDistribution.processStatisticDist(group, pathOutput, pathFile)
statistic.handlerStatistic()
