'''
permite crear el arbol de decision segun la informacion generada por el proceso de division por clustering...
'''

from graphviz import Digraph

g = Digraph('G', filename='grafo.gv')

g.edge('256', '203')
g.edge('256', '53')
g.edge('203', '82')
g.edge('203', '121')
g.edge('53', '12')
g.edge('53', '41')
g.edge('121', '95')
g.edge('121', '26')
g.edge('41', '13')
g.edge('41', '28')
g.edge('95', '33')
g.edge('95', '62')
g.view()
