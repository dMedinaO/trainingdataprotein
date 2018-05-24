from Modules.View import Main
import ConfigParser

class Launcher(object):
	
	def __init__(self, getGlade):
		
		self.nameFile = self.getConfiguration(getGlade)
		self.windows = Main.Handler(self.nameFile)
		
	#methon for get params for handler the file of building windows
	def getConfiguration(self, getGlade):

		Config = ConfigParser.ConfigParser()#instance of ConfigParser
		Config.read('/etc/DataDiabetes/configDB.cfg')

		#create dictionary for add information of connection
		nameFile = Config.get('FrontEnd', getGlade)

		return nameFile

def main ():
	
	launcher = Launcher('principal')

if __name__ == '__main__':
	main()
