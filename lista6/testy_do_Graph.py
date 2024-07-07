from Zad1_2_3_4_5 import Graph

graph1=Graph()
graph1.addVertex('A')
graph1.addVertex('B')
graph1.addVertex('C')
graph1.addVertex('D')
graph1.addVertex('E')
graph1.addVertex('F')
graph1.addEdge('A','B')
graph1.addEdge('B','C')
graph1.addEdge('B','F')
graph1.addEdge('C','D')
graph1.addEdge('C','E')

print(graph1.toDot())
print(graph1.bfs('A'))
print(graph1.dfs('A'))
print(graph1.topologicalSort())
print(graph1.shortestPath('A'))
'''
graph2=Graph()
graph2.addVertex('A')
graph2.addVertex('B')
graph2.addVertex('C')
graph2.addVertex('D')
graph2.addVertex('E')
graph2.addVertex('F')
graph2.addVertex('H')
graph2.addEdge('A','B')
graph2.addEdge('C','B')
graph2.addEdge('A','D')
graph2.addEdge('B','D')
graph2.addEdge('D','E')
graph2.addEdge('D','H')
graph2.addEdge('E','F')
graph2.addEdge('F','H')

graph3=Graph()
graph3.addVertex('A')
graph3.addVertex('B')
graph3.addVertex('C')
graph3.addVertex('D')
graph3.addVertex('E')
graph3.addVertex('F')
graph3.addEdge('A','B')
graph3.addEdge('B','D')
graph3.addEdge('A','D')
graph3.addEdge('D','E')
graph3.addEdge('E','B')
graph3.addEdge('B','C')
graph3.addEdge('E','F')
graph3.addEdge('F','C')
'''