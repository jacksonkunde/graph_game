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

    def Get(graph, i):
        for v in graph.V:
            if v.index == i:
                return v
        return None

    def ChooseVertexToRemove(graph, player):
        return PercolationPlayer.Get(graph, random.choice([v.index for v in graph.V if v.color == player]))



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
