'''
script que permite generar la validacion cruzada de los grupos con respecto a los valores de prediccion de los otros grupos de interes...
'''

from proyect.CCMakeModels import checkModelsGroupA, checkModelsGroupB, checkModelsGroupC, checkModelsGroupF, checkModelsGroupH, checkModelsGroupM, checkModelsGroupN, checkModelsGroupO, checkModelsGroupP, checkModelsGroupR, checkModelsGroupT, checkModelsGroupU, checkModelsGroupZ
import sys

#recibimos la data de interes...
pathInput = sys.argv[1]
pathOutput = sys.argv[2]

# checkA = checkModelsGroupA.evaluacionCruzada(pathInput, pathOutput+"A_Attribute/training/crossValidation/")
# checkA.processGroup()
#
# checkB = checkModelsGroupB.evaluacionCruzada(pathInput, pathOutput+"B_Attribute/training/crossValidation/")
# checkB.processGroup()
#
# checkC = checkModelsGroupC.evaluacionCruzada(pathInput, pathOutput+"C_Attribute/training/crossValidation/")
# checkC.processGroup()
#
# checkF = checkModelsGroupF.evaluacionCruzada(pathInput, pathOutput+"F_Attribute/training/crossValidation/")
# checkF.processGroup()
#
# checkH = checkModelsGroupH.evaluacionCruzada(pathInput, pathOutput+"H_Attribute/training/crossValidation/")
# checkH.processGroup()
#
# checkM = checkModelsGroupM.evaluacionCruzada(pathInput, pathOutput+"M_Attribute/training/crossValidation/")
# checkM.processGroup()
#
# checkN = checkModelsGroupN.evaluacionCruzada(pathInput, pathOutput+"N_Attribute/training/crossValidation/")
# checkN.processGroup()
#
# checkO = checkModelsGroupO.evaluacionCruzada(pathInput, pathOutput+"O_Attribute/training/crossValidation/")
# checkO.processGroup()
#
# checkP = checkModelsGroupP.evaluacionCruzada(pathInput, pathOutput+"P_Attribute/training/crossValidation/")
# checkP.processGroup()

checkR = checkModelsGroupR.evaluacionCruzada(pathInput, pathOutput+"R_Attribute/training/crossValidation/")
checkR.processGroup()

#checkT = checkModelsGroupT.evaluacionCruzada(pathInput, pathOutput+"T_Attribute/training/crossValidation/")
#checkT.processGroup()

#checkU = checkModelsGroupU.evaluacionCruzada(pathInput, pathOutput+"U_Attribute/training/crossValidation/")
#checkU.processGroup()

checkZ = checkModelsGroupZ.evaluacionCruzada(pathInput, pathOutput+"Z_Attribute/training/crossValidation/")
checkZ.processGroup()
