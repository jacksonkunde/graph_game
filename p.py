#ok
from benchmark import *
from util import *

class Tree:
    def __init__(self, data, children = []):
        self.children = children
        self.data = data #ideally tuple

class PercolationPlayer:
    def ChooseVertexToColor(graph, player):
        return random.choice([v for v in graph.V if v.color == -1])

    def GetV(graph, i):
        for v in graph.V:
            if v.index == i:
                return v
        return None

    def GetE(graph, v):
        return [e for e in graph.E if (e.a == v or e.b == v)]

    def Percolate(graph, i):
        v = PercolationPlayer.GetV(graph, i)
        for e in PercolationPlayer.GetE(graph, v):
            graph.E.remove(e)
        graph.V.remove(v)
        to_remove = {u for u in graph.V if len(IncidentEdges(graph, u)) == 0}
        graph.V.difference_update(to_remove)

    def ChooseVertexToRemove(graph, player):
        it = copy.deepcopy(graph)
        #print(PercolationPlayer.GetE(graph, PercolationPlayer.GetV(graph, random.choice([v.index for  v in graph.V if v.color == player]))))
        return PercolationPlayer.GetV(it, random.choice([v.index for v in it.V if v.color == player]))



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
