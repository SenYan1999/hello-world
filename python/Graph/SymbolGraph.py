from Graph import Graph
import sys

class SymbolGraph:
    def __init__(self,fileName,delim):
        

    def contains(self,key):

    def index(self,key):

    def name(self,v):

    def G(self)

if __name__ == '__main__':
    fileName = sys.argv[1]
    delim = sys.argv[1]

    sg = SymbolGraph(fileName,delim)
    G = sg.G()

    while True:
        source = input("Please input the index's name:")
        for w in G.adj(sg.index(source)):
            print('    ',sg.name(w))
