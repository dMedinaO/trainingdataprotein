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
            packages=['modulesServiceVHL', 'modulesServiceVHL.CCTestingCR', 'modulesServiceVHL.CCTestingIPP'],)

def main():

    setup = SetupConfiguration()
    return 0

if __name__ == '__main__':
    main()
