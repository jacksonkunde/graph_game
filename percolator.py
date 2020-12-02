#muc: Jackson Kunde, Daniel Tan, Colin Skinnerf, William Akon, and Jasper Sand

from benchmark import *
from util import *



class PercolationPlayer:
	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
    # Should return a vertex `v` from graph.V where v.color == -1
    def ChooseVertexToColor(graph, player):
        return random.choice([v for v in graph.V if v.color == -1])

# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
# Should return a vertex `v` from graph.V where v.color == player
    def ChooseVertexToRemove(graph, player):
        return random.choice([v for v in graph.V if v.color == player])

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
