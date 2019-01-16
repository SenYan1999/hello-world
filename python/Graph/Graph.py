class Graph:
    def __init__(self,graphList=None,V=None,E=None):
        '''
        Constructor
        '''
        self.V,self.E = V,E
        self.adj = [[] for i in range(V)]
        for i in range(0,len(graphList),2):
            self.addEdge(graphList[i],graphList[i+1])
    
    def getV(self):
        return self.V
    def getE(self):
        return self.E
    
    def addEdge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def getGraph(self):
        return self.adj

    def adj(self,v):
        return self.adj[v]
 
if __name__=='__main__':    
    data = []
    with open('/home/mike/Documents/tinyG.txt') as fileToRead:
        for line in fileToRead:
            for i in line.split():
                data.append(int(i))   
    dataList = data[2:]
    myGraph = Graph(data[0],data[1],dataList)
    print(dataList)
