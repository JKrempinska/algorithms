from collections import deque

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {} 
        self.id = key
        self.connectedTo = {}
        self.dist = 0   
        self.pred = None        
        self.disc = 0              
        self.fin = 0 

    def addNeighbor(self,nbr,weight=1):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def getNeighbors(self, vert_key):
        vertex = self.getVertex(vert_key)
        if vertex:
            return [neighbor.getId() for neighbor in vertex.getConnections()]
        else:
            return None
    
    def dfs(self, start_key, visited=None):
        if visited is None:
            visited = set()
        result = []
        start_vertex = self.getVertex(start_key)
        def dfs_recursive(vertex):
            if vertex.getId() not in visited:
                visited.add(vertex.getId())
                result.append(vertex.getId())
                for neighbor in vertex.getConnections():
                    dfs_recursive(neighbor)
        dfs_recursive(start_vertex)
        return result
    
    def bfs(self, start_key):
        visited = set()
        result = []
        start_vertex = self.getVertex(start_key)
        if not start_vertex:
            return result

        queue = deque([start_vertex])
        while queue:
            current_vertex = queue.popleft()
            if current_vertex.getId() not in visited:
                visited.add(current_vertex.getId())
                result.append(current_vertex.getId())
                for neighbor in current_vertex.getConnections():
                    queue.append(neighbor)
        return result
    
    def toDot(self):
        dot_representation = "digraph G {\n"
        for vertex in self.vertList.values():
            dot_representation += f'  "{str(vertex.getId())}" [label="{vertex.getId()}"];\n'
            for neighbor in vertex.getConnections():
                dot_representation += f'  "{str(vertex.getId())}" -> "{neighbor.getId()}"'
                dot_representation += f' [label="{vertex.getWeight(neighbor)}"];\n'
        dot_representation += "}\n"
        return dot_representation
    
    def topologicalSort(self):
        visited = set()
        stack = []

        def dfs_topological(vertex):
            visited.add(vertex.getId())
            for neighbor in vertex.getConnections():
                if neighbor.getId() not in visited:
                    dfs_topological(neighbor)
            stack.append(vertex.getId())

        for vertex in self.vertList.values():
            if vertex.getId() not in visited:
                dfs_topological(vertex)

        return stack[::-1]

    def shortestPath(self, start_key):

        start_vertex = self.getVertex(start_key)

        if not start_vertex:
            return {}

        distances = {vertex.getId(): float('inf') for vertex in self.vertList.values()}
        distances[start_key] = 0

        paths = {vertex.getId(): [] for vertex in self.vertList.values()}
        paths[start_key] = [start_key]

        queue = deque([(start_vertex, [start_key])])

        while queue:
            current_vertex, current_path = queue.popleft()

            for neighbor in current_vertex.getConnections():
                neighbor_key = neighbor.getId()

                if distances[neighbor_key] == float('inf'):
                    distances[neighbor_key] = distances[current_vertex.getId()] + 1
                    paths[neighbor_key] = current_path + [neighbor_key]
                    queue.append((neighbor, current_path + [neighbor_key]))

        result = {key: (distances[key], paths[key]) for key in distances}
        return result

graph=Graph()
print()