'''
script que permite testear los modelos asociados al grupo 01 de la division inducida por clustering recursivo, es una funcion
por modelo, cada funcion retorna 3 arreglos:
1. Los valores reales de la clasificacion
2. Los valores de prediccion de la clasificacion
3. Los valores de score asociados a la clasificacion generada
'''

from sklearn.neighbors import KNeighborsClassifier

class testingGrupo1CR(object):

    def __init__(self, dataSet, response):

        self.dataSet = dataSet
        self.response = response

    #metodo que permite aplicar todos los modelos seleccionados a la mejor accuracy obtenida...
    def applyModelsAccuracy(self):

        for i in range (1,3):
            for metric in ["euclidean", "minkowski"]:
                for algorithm in ["auto", "ball_tree"]:
                    for weight in ["uniform", "distance"]:
                        clf = KNeighborsClassifier(n_neighbors=i,metric=metric,algorithm=algorithm,weights=weight, n_jobs=-1)
                        clf = clf.fit(self.dataSet, self.response)

                        print clf.score(self.dataSet, self.response)
                        break
                    break
                break
            break
