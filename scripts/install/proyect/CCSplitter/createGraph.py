'''
permite crear el arbol de decision segun la informacion generada por el proceso de division por clustering...
'''

from graphviz import Digraph

g = Digraph('G', filename='hello.gv')

g.edge('Hello', 'World')

g.view()
