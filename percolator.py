#muc: Jackson Kunde, Daniel Tan, Colin Skinnerf, William Akon, and Jasper Sand

from benchmark import *
from util import *

#for game tree

class Tree:
    def __init__(self, data, children = []):
        self.children = children
        self.data = data
        self.good = True #perhaps implement "good" list external to class for memory

    def isLeaf(self):
        return True if len(self.children) == 0 else False

# left = Tree("left")
# middle = Tree("middle")
# right = Tree("right")
# root = Tree("root", [left, middle, right])

class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == -1
    def ChooseVertexToColor(graph, player):
        return random.choice([v for v in graph.V if v.color == -1])

    def GetVertee(graph, i):
        for v in graph.V:
            if v.index == i:
                return v
        return None

    def IncidentEdges(graph, v):
        return [e for e in graph.E if (e.a == v or e.b == v)]

    def Percolate(graph, index):
        # Get attached edges to this vertex, remove them.
        v = PercolationPlayer.GetVertee(graph, index)
        for e in PercolationPlayer.IncidentEdges(graph, v):
            graph.E.remove(e)
        # Remove this vertex.
        graph.V.remove(v)
        # Remove all isolated vertices.
        to_remove = [iso for iso in graph.V if len(PercolationPlayer.IncidentEdges(graph, iso)) == 0]
        for item in to_remove:
            graph.V.remove(item)

        return graph

# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
# Should return a vertex `v` from graph.V where v.color == player
    def ChooseVertexToRemove(graph, player):

        #remove isolated vertices
        #connectedVertices = {v.index: v for v in graph.V if v.index not in [v.index for v in graph.V if len([e for e in graph.E if e.a == v or e.b == v]) == 0]}
        #connectedGraph = Graph(connectedVertices, graph.E)

        print("de")
        print(graph.V)
        print(graph.E)

        tree = PercolationPlayer.CreateGameTree(graph, player)
        max = -999
        index = None
        for node in tree.children:
            (h, i) = node.data
            if h > max:
                max = h
                index = i
        print("ok")
        print(index)
        ok = [v for v in graph.V if v.index == index and v.color == player]
        print(ok)
        return ok[0]

    #matt redmond heuristic
    def GetValue(graph, player):
        return len([v for v in graph.V if v.color == player]) - len([v for v in graph.V if v.color == 1-player])

    #frame with Tree implementation]
    def CreateGameTree(graph, player):
        #1 degree search in DFS
        tree = Tree([PercolationPlayer.GetValue(graph, player), None])
        print("validityCheck")
        print([v for v in graph.V if v.color == player])
        for index in [v.index for v in graph.V if v.color == player]:
            child_graph = copy.deepcopy(graph)
            child_graph = PercolationPlayer.Percolate(child_graph, index)
            tree.children.append(Tree([PercolationPlayer.GetValue(child_graph, player), index])) # change to diction ery : )
        return tree

    # def minimax(treenode, maxplayer):
    #     if treenode.isLeaf():
    #         return treenode.data[0]
    #     if maxplayer:
    #         min = -999
    #         for child in treenode.children:
    #             min = max(min, minimax(child, False))
    #         return min
    #     else:
    #         max = 999
    #         for child in treenode.children:
    #             max = min(max, minimax(child, True))
    #         return max

# Feel free to put any personal driver code here.
def main():
    p1 = RandomPlayer
    p2 = PercolationPlayer
    iters = 1
    wins = PlayBenchmark(p1, p2, iters)
    print(wins)
    print(
        "Player 1: {0} Player 2: {1}".format(
            1.0 * wins[0] / sum(wins), 1.0 * wins[1] / sum(wins)
        )
    )
    pass

if __name__ == "__main__":
    main()
