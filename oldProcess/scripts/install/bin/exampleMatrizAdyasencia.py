# Licence GPL 3+
# Copyright: Jesus Mager, 2017

import graphviz as gv
import numpy as np


class GraphClass:
    def __init__(self):
        pass

    def random(self, s=100):
        a = np.random.uniform(size=s)
        b = np.random.uniform(size=s)
        self.M = np.asmatrix([a,b])
        self.M = np.transpose(self.M)

    def d(self, X, Y):
        return np.linalg.norm(X-Y)

    def distances(self):
        self.distM = np.zeros((len(self.M), len(self.M)))
        i = 0
        j = 0
        for e in self.M:
            j = 0
            for comp in self.M:
                self.distM[j][i] = self.d(e, comp)
                j += 1
            i += 1

    def threshold(self, t = .3):
        print(self.distM)
        self.distM[self.distM > t] = 2
        self.distM[self.distM <= t] = 1
        self.distM[self.distM == 2] = 0
        np.fill_diagonal(self.distM, 0)
        print(self.distM)

    def draw(self):
        used=[]
        g = gv.Graph(format="svg")
        for i in range(len(self.distM)):
            g.node(str(self.M[i]))
            for j in range(len(self.distM[i])):
                if self.distM[j][i]:
                    if not str(self.M[i])+str(self.M[j]) in used:
                        used.append(str(self.M[i])+str(self.M[j]))
                        used.append(str(self.M[j])+str(self.M[i]))
                        g.edge(str(self.M[i]), str(self.M[j]))
        g.render(view=True)


if __name__  == "__main__":
    g = GraphClass()
    g.random()
    g.distances()
    g.threshold()
    g.draw()
