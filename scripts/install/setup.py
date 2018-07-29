from distutils.core import setup
import ConfigParser
import os

class SetupConfiguration:

    def __init__(self):

        self.setupInstall()

    def setupInstall(self):

        setup(name='proyectDataTraining',
            version='alpha',
            description='Proyect Data Training and its scripts for manipulation data sets',
            author='david medina',
            author_email='david.medina@cebib.cl',
            license='Open GPL 3',
            packages=['proyect', 'proyect.CCConnectDB', 'proyect.CCCRUD', 'proyect.CCClustering', 'proyect.CCFeaturesAnalisis',  'proyect.CCProcesFile',  'proyect.CCStatistic', 'proyect.CCTraining', 'proyect.CCTraining.LOU', 'proyect.CCMakeGroups', 'proyect.CCProcessPDB', 'proyect.CCModels', 'proyect.CCMakeModels' ],)

def main():

    setup = SetupConfiguration()
    return 0

if __name__ == '__main__':
    main()
