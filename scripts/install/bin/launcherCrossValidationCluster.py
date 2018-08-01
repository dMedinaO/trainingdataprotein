'''
script que permite generar la validacion cruzada de los grupos con respecto a los valores de prediccion de los otros grupos de interes...
'''

from proyect.CCSplitter import checkG1, checkG2, checkG3, checkG4, checkG5, checkG6, checkG7, checkG8
import sys

#recibimos la data de interes...
pathInput = sys.argv[1]

#check1 = checkG1.evaluacionCruzada(pathInput, pathInput+"1/training/crossValidation/")
#check1.processGroup()

#check2 = checkG2.evaluacionCruzada(pathInput, pathInput+"2/training/crossValidation/")
#check2.processGroup()

#check3 = checkG3.evaluacionCruzada(pathInput, pathInput+"3/training/crossValidation/")
#check3.processGroup()

#check4 = checkG4.evaluacionCruzada(pathInput, pathInput+"4/training/crossValidation/")
#check4.processGroup()

#check5 = checkG5.evaluacionCruzada(pathInput, pathInput+"5/training/crossValidation/")
#check5.processGroup()

#check6 = checkG6.evaluacionCruzada(pathInput, pathInput+"6/training/crossValidation/")
#check6.processGroup()

#check7 = checkG7.evaluacionCruzada(pathInput, pathInput+"7/training/crossValidation/")
#check7.processGroup()

check8 = checkG8.evaluacionCruzada(pathInput, pathInput+"8/training/crossValidation/")
check8.processGroup()
