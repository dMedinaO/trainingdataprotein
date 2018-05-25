'''
clase con la responsabilidad de generar un diccionario con los resultados entregados en la lista de performance
para el algoritmo aplicado...
'''

from proyect.CCTraining import performanceScore

class processPerformance(object):

    def __init__(self, listPerfomance):

        self.listPerfomance = listPerfomance
        self.dictValue = []

    #metodo que permite obtener la informacion de la performance, crear un diccionario y agregarla a la lista...
    def getValuesPerformance(self):

        for performance in self.listPerfomance:
            dictResponse = {}
            dictResponse.update({'algoritmo': performance.algorithm})
            dictResponse.update({'description': performance.description})
            dictResponse.update({'validation': performance.validation})
            #agregamos los valores de las performance
            dictResponse.update({'accuracy': performance.scoreData[0]})
            dictResponse.update({'recall': performance.scoreData[1]})
            dictResponse.update({'precision': performance.scoreData[2]})
            dictResponse.update({'neg_log_loss': performance.scoreData[3]})
            dictResponse.update({'f1': performance.scoreData[4]})
            dictResponse.update({'ftwo_scorer': performance.scoreData[5]})

            self.dictValue.append(dictResponse)
