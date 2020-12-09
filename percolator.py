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

# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
# Should return a vertex `v` from graph.V where v.color == player

    def ChooseVertexToRemove(graph, player):

        #remove isolated vertices
        connectedVertices = {v.index: v for v in graph.V if v.index not in [v.index for v in graph.V if len([e for e in graph.E if e.a == v or e.b == v]) == 0]}
        connectedGraph = Graph(connectedVertices, graph.E)

        tree = PercolationPlayer.CreateGameTree(graph, player)
        g = [(node.data[0], node.data[1]) for node in tree.children]
        min = -999
        storage = Vertex(-999, -999)
        for item in g:
            if item[0] > min:
                min = item[0]
                storage = Vertex(item[1], player)
        return storage

    #matt redmond heuristic
    def GetValue(graph, player):
        return len([v for v in graph.V if v.color == player]) - len([v for v in graph.V if v.color == 1 - player])

    #frame with Tree implementation]
    def CreateGameTree(graph, player):
        #1 degree search in DFS
        tree = Tree("root")
        for index in [v.index for v in graph.V if v.color == player]:
            result = Graph({ve.index: ve for ve in graph.V if ve.index != index}.values(), [edge for edge in graph.E if (edge.a != index or ed.b != index)])
            tree.children.append(Tree((PercolationPlayer.GetValue(result, player), index)))
        return tree


    def minimax(treenode, maxplayer):
        if treenode.isLeaf():
            return treenode.data[0]
        if maxplayer:
            min = -999
            for child in treenode.children:
                min = max(min, minimax(child, False))
            return min
        else:
            max = 999
            for child in treenode.children:
                max = min(max, minimax(child, True))
            return max

# Feel free to put any personal driver code here.
def main():
    p1 = RandomPlayer
    p2 = PercolationPlayer
    iters = 200
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
