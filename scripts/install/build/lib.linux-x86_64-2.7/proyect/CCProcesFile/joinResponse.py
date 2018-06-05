'''
script que permite generar la union de archivos en formato csv dentro de un conjunto de directorios...
'''

import subprocess
import sys

#recibimos las variables
pathDir = sys.argv[1]
nameAll = sys.argv[2]
iterator = int(sys.argv[3])

for i in range(1, iterator+1):

    for j in range(1, 14):#son 13 grupos
        command = "cat %s%d%s/%d/training/*.csv > %s%d%s/%d/training/fullJoin.csv" % (pathDir, i, nameAll, j, pathDir, i, nameAll, j)
        print command
        subprocess.call(command, shell=True)
