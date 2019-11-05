#modulos asociados a la conexion y procesamiento de informacion a la base de datos
from Modules.CCConnectDB import ConnectDataBase
from Modules.CCCRUD import CrudDataBase

import sys

fileOpen = open(sys.argv[1], 'r')

line = fileOpen.readline()
Data = []

while line:

	line = line.replace("\n", "")
	Data.append(line)
	line = fileOpen.readline()

Connect = ConnectDataBase.ConnectDataBase()#instance to object ConnectDataBase
CrudDataBase = CrudDataBase.HandlerQuery()#instance to object CrudDataBase for handeler data base

i = 1
Connect.initConnectionDB()
for element in Data:

	dataSplit = element.split(",")
	
	query = "insert into conteoYemaIdeal values (%d, '%s', '%s', '%s', '%s', '%s', %d, %d, %d)" % (i, dataSplit[0], dataSplit[1], dataSplit[2], dataSplit[3], dataSplit[4], int(dataSplit[5]), int(sys.argv[2]), int(sys.argv[3]))

	print query 

	CrudDataBase.insertToTable(query, Connect)
	i+=1
Connect.closeConnectionDB()
