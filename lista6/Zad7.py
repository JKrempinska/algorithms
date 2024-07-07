from Zad1_2_3_4_5 import Graph

class WaterJugProblem(Graph):

    def addState(self, state):
        state_key = str(state)
        if state_key not in self.vertList:
            newVertex = self.addVertex(state_key)
            return newVertex
        else:
            return self.vertList[state_key]

    def generateStates(self):
        for a in range(4):
            for b in range(5):
                state = (a, b)
                self.addState(state)

    def generateValidMoves(self):
        new_vertices = [] 

        for vertex in list(self.vertList.values()): 
            state = eval(vertex.getId())
            a, b = state[0], state[1]
            
            if self.isValidState((3, b)):
                new_vertex = self.addState((3, b))
                vertex.addNeighbor(new_vertex)

            if self.isValidState((a, 4)): 
                new_vertex = self.addState((a, 4))
                vertex.addNeighbor(new_vertex)

            if self.isValidState((0, b)):
                new_vertex = self.addState((0, b))
                vertex.addNeighbor(new_vertex)

            if self.isValidState((a, 0)):
                new_vertex = self.addState((a, 0))
                vertex.addNeighbor(new_vertex)

            pour_to_b = min(a, 4 - b)
            if self.isValidState((a - pour_to_b, b + pour_to_b)):
                new_vertex = self.addState((a - pour_to_b, b + pour_to_b))
                vertex.addNeighbor(new_vertex)

            pour_to_a = min(3 - a, b)
            if self.isValidState((a + pour_to_a, b - pour_to_a)):
                new_vertex = self.addState((a + pour_to_a, b - pour_to_a))
                vertex.addNeighbor(new_vertex)
            
            new_vertices.extend([(3, b), (a, 4), (0, b), (a, 0), (a - min(a, 4 - b), b + min(a, 4 - b)), (a + min(3 - a, b), b - min(3 - a, b))])

        for state in new_vertices:
            self.addState(state)

    def isValidState(self, state):
        a, b = state
        if 0 <= a <= 3 and 0 <= b <= 4:
            return True

    def solveWaterJugProblem(self):
        self.generateStates()
        self.generateValidMoves()

        start_state = (0, 0)
        end_state = (2, 0)

        start_vertex = self.getVertex(str(start_state))
        end_vertex = self.getVertex(str(end_state))
        if start_vertex and end_vertex:
            all_paths = self.shortestPath(str(start_state))
            result = all_paths[str(end_state)][1]
            return result

graph = WaterJugProblem()
print(graph.toDot())
solution = graph.solveWaterJugProblem()
print(solution)