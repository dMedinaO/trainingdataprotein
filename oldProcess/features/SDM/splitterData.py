'''
script que recibe un archivo y permite ir dividiendo con respecto a la data e ir probando de 20 en 20 residuos
'''

#funcion que permite escribir un archivo con algunas mutaciones correspondientes
def createFile(dataLine, nameOutput):

    openFile = open(nameOutput, 'w')
    for element in dataLine:
        openFile.write(element)
    openFile.close()

openFile = open('outputMutations.txt', 'r')

listLine = []

line = openFile.readline()

while line:
    listLine.append(line)
    line = openFile.readline()

openFile.close()

numberFile = len(listLine)/20
restSeq = len(listLine)%20

seqActual = 0

#comenzamos a generar los archivos
for data in range(numberFile):
    dataLine = []

    for i in range(seqActual, seqActual+20):
        dataLine.append(listLine[i])
    print dataLine
    nameOutput = "mutations/processFile"+str(data)+"txt"
    createFile(dataLine, nameOutput)
    seqActual+=20

#trabajamos con las ultimas dos mutaciones
dataLine = []
for i in range(len(listLine)-2, len(listLine)):
    dataLine.append(listLine[i])
print dataLine
nameOutput = "mutations/processFileResidue.txt"
createFile(dataLine, nameOutput)
