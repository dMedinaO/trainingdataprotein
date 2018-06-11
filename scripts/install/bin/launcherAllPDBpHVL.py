'''
script que permite parsear todos los posibles pdbs de la familia pVHL, generando el archivo para trabajar el grafo,
los parser de los degree, los elementos de los calculos de matrices de energia, los datos de estos y otros archivos
que se me ocurran durante el proceso XD...
'''

import sys
import subprocess

ListpVHL = ['1lm8', '1lqb', '3ec1', '3zrc', '3zrf', '3ztc', '3ztd', '3zun', '4ajy', '4awj', '4b9k', '4b95', '4bks', '4bkt', '4w9c', '4w9d', '4w9e', '4w9f', '4w9g', '4w9h', '4w9i', '4w9j', '4w9k', '4w9l', '4wqo', '5lli', '5n4w', '5nvv', '5nvw', '5nvx', '5nvy', '5nvz', '5nw0', '5nw1', '5nw2', '5t35', '6fmi', '6fmj', '6fmk']

#recibimos los parametros por consola...
pathFile = sys.argv[1]
pathOutput = sys.argv[2]
responseWhatIf = sys.argv[3]
degreePath = sys.argv[4]

for element in ListpVHL:

    try:
        command = "python launcherPDBProcess.py %s %s.pdb %s %s%s_HBonds.txt %s%s_DegreeValues.txt" % (pathFile, element, pathOutput, responseWhatIf, element, degreePath, element)
        subprocess.call(command, shell=True)
    except:
        print "pleas check %s pdb" % element
