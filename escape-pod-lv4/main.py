from collections import defaultdict

class Graph: 

    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 

    def BFS(self,s, t, parent):
        """ Breadth first search that returns true

        Args:
            s ([int]): [source node]
            t ([int]): [sink node]
            parent ([type]): [description]

        Returns:
            [bool]: [returns true if there is a path from sink to source]
        """
        visited =[False]*self.ROW 
        queue = [s] 
        visited[s] = True

        while queue: 
            u = queue.pop(0) 

            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 

        return bool(visited[t])
        
    
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 

        parent = [-1]*self.ROW 

        max_flow = 0 
        while self.BFS(source, sink, parent) : 

            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 

            max_flow +=  path_flow 

            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 

        return max_flow 

def def_value():
    return 0

def solution(entrances, exits, path):
    n = len(path) + 2
    # calculate the flows for the super sink
    sinkdict = defaultdict(def_value)
    for i in exits:
        for j in path:
            sinkdict[i+1] += j[i]
            
    sourcedict = defaultdict(def_value)
    for i in entrances:
        sourcedict[i+1] = sum(path[i])
        
    # insert a 0 at the beginning and end of each path list
    for item in path:
        item.append(0)
        item.insert(0, 0)
    
    # make super source
    path.insert(0, [0]*n)
    
    # make super sink
    path.append([0]*n)
    
    # fill out super source
    for i in entrances:
        path[0][i+1] = sourcedict[i+1]
        
    # fill out super sink
    for i in exits:
        path[i+1][n-1] = sinkdict[i+1]
    
    g = Graph(path)
    return g.FordFulkerson(0,n-1)
    
    
if __name__ == '__main__':
    print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))