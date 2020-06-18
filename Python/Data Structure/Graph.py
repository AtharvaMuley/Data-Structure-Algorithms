"""
Author: Atharva Muley
Date: Jan 30 2020
"""
class Graph:
    graph_dict = {}

    def addEdge(self, u, v):
        if u not in self.graph_dict:
            self.graph_dict.update({u:[v]})
        else:
            self.graph_dict[u].append(v)

    def showEdges(self):
        for node in self.graph_dict:
            for neighbours in self.graph_dict[node]:
                print(neighbours, end=" ")
        print()
if __name__ == "__main__":
    g = Graph()
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(3,2)
    g.addEdge(4,2)
    g.showEdges()
