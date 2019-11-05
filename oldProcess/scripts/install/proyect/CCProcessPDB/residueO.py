'''
clase que tiene la responsabilidad de almacenar la informacion de interes de un residuo,
ademas del manejo de la informacion de este con el fin de poder utilizarla para hacer los
calculos correspondientes y generar matrices de adjacencia de interes....
'''

class residue(object):

    def __init__(self, resname, chain, pos, listAtom):

        self.resname = resname
        self.chain = chain
        self.pos = pos
        self.listAtom = listAtom
