from Zad1_2_3_4_5 import Graph

class MissionariesAndCannibalsGraph(Graph):

    def addState(self, state):
        state_key = str(state)
        if state_key not in self.vertList:
            newVertex = self.addVertex(state_key)
            return newVertex
        else:
            return self.vertList[state_key]

    def generateStates(self):
        for m in range(4):
            for k in range(4):
                for boat in ['L', 'R']:
                    state = (m, k, boat)
                    self.addState(state)

    def generateValidMoves(self):
        for vertex in self.vertList.values():
            state = eval(vertex.getId())

            if state[2] == 'L':
                for m in range(3):
                    for k in range(3):
                        if 0 < m + k <= 2: 
                            new_state = (3-state[0] + m, 3-state[1] + k, 'R')
                            if self.isValidState(new_state):
                                new_vertex = self.addState(new_state)
                                vertex.addNeighbor(new_vertex)

            elif state[2] == 'R':
                for m in range(3):
                    for k in range(3):
                        if 0 < m + k <= 2:
                            new_state = (3-state[0] + m, 3-state[1] + k, 'L')
                            if self.isValidState(new_state):
                                new_vertex = self.addState(new_state)
                                vertex.addNeighbor(new_vertex)

    def isValidState(self, state):
        m, k, _ = state
        if 0 <= m <= 3 and 0 <= k <= 3 and (m == 0 or m >= k) and (3 - m == 0 or (3 - m) >= (3 - k)):
            return True

    def solveMissionariesAndCannibals(self):
        self.generateStates()
        self.generateValidMoves()

        start_state = (3, 3, 'L')
        end_state = (3, 3, 'R')

        start_vertex = self.getVertex(str(start_state))
        end_vertex = self.getVertex(str(end_state))
        if start_vertex and end_vertex:
            all_paths = self.shortestPath(str(start_state))
            result = all_paths[str(end_state)][1]
            for i in range(len(result)):
                if result[i][-3] == 'L':
                    print(f"krok {i+1}: {result[i]}, ({3-int(result[i][1])}, {3-int(result[i][4])}, 'R')")
                elif result[i][-3] == 'R':
                    print(f"krok {i+1}: ({3-int(result[i][1])}, {3-int(result[i][4])}, 'L'), {result[i]}")
        else:
            return []

graph = MissionariesAndCannibalsGraph()
solution_path = graph.solveMissionariesAndCannibals()