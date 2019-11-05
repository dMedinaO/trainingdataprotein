'''
script que permite generar la validacion cruzada de los grupos con respecto a los valores de prediccion de los otros grupos de interes...
'''

from proyect.CCMakeModels import checkModelsGroup1, checkModelsGroup2, checkModelsGroup3, checkModelsGroup4, checkModelsGroup5, checkModelsGroup6, checkModelsGroup7
import sys

#recibimos la data de interes...
pathInput = sys.argv[1]
pathOutput = sys.argv[2]

#check1 = checkModelsGroupA.evaluacionCruzada(pathInput, pathOutput+"A_Attribute/training/crossValidation/")
#check1.processGroup()
#
#check2 = checkModelsGroup2.evaluacionCruzada(pathInput, pathOutput+"grupo2/training/crossValidation/")
#check2.processGroup()
#
#check3 = checkModelsGroup3.evaluacionCruzada(pathInput, pathOutput+"grupo3/training/crossValidation/")
#check3.processGroup()
#
#check4 = checkModelsGroup4.evaluacionCruzada(pathInput, pathOutput+"grupo4/training/crossValidation/")
#check4.processGroup()
#
#check5 = checkModelsGroup5.evaluacionCruzada(pathInput, pathOutput+"grupo5/training/crossValidation/")
#check5.processGroup()
#
#check6 = checkModelsGroup6.evaluacionCruzada(pathInput, pathOutput+"grupo6/training/crossValidation/")
#check6.processGroup()
#
check7 = checkModelsGroup7.evaluacionCruzada(pathInput, pathOutput+"grupo7/training/crossValidation/")
check7.processGroup()
