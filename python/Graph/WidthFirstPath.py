from Graph import Graph
from queue import Queue

class WidthFirstSearch:
    def __init__(self,graph,s):
        self.s = s
        self.myQueue = Queue()
        self.marked = [False for i in range(graph.getV())]
        self.edgeTo = [None for i in range(graph.getV())]

    def bfs(self,graph,v):
        self.marked[v] = True
        self.myQueue.put(v)
        
        while myQueue.empty() == False:
            v = self.myQueue.get()
            for x in graph.adj(v):
                if self.marked[x]  == False:
                    self.marked[x] = True
                    self.edgeTo[x] = v
                    self.myQueue.put(x)

    def getPath(self,v):
        x = v
        path = Queue()
        while self.edgeTo[x] != None:
            path.put(x)
            x = self.edgeTo[x]
        path.put(self.s)
        return path

if __name__=='__main__':    
    data = []
    with open('/home/mike/Documents/tinyG.txt') as fileToRead:
        for line in fileToRead:
            for i in line.split():
                data.append(int(i))   
    dataList = data[2:]
    myGraph = Graph(data[0],data[1],dataList)

    myPath = WidthFirstSearch(myGraph,0)
    a = myPath.getPath(6)
    while a.empty == False:
        print(a.get())
