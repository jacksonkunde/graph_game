#ok
from benchmark import *
from util import *

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

    def Percolate(graph, v):
        for e in PercolationPlayer.GetE(graph, v):
            graph.E.remove(e)
        graph.V.remove(v)
        to_remove = {u for u in graph.V if len(IncidentEdges(graph, u)) == 0}
        graph.V.difference_update(to_remove)

    def RedmondHeuristic(graph, player):
        return len([v for v in graph.V if v.color == player]) - len([u for u in graph.V if u.color != player])

    def VDegSumHeuristic(graph, player):
        oursum = 0
        opposum = 0
        for v in graph.V:
            degree = len(IncidentEdges(graph,v))
            if v.color == player:
                oursum += degree
            else:
                opposum += degree
        return (oursum + opposum, oursum - opposum)

    def combineHeuristics(graph, player):
        normalizedRedmondHeuristic = 0.0
        if len(graph.V) != 0:
            normalizedRedmondHeuristic = PercolationPlayer.RedmondHeuristic(graph, player)/len(graph.V)

        normalizedVDegHeuristic = 0.0
        te = PercolationPlayer.VDegSumHeuristic(graph, player)
        if te[0] != 0:
            normalizedVDegHeuristic = te[1]/te[0]

        #arbitrary weighting, weight or no weight will pull 70% win split
        return normalizedRedmondHeuristic + normalizedVDegHeuristic

    #at one degree
    def Children(graph, player):
        children = []
        for v in graph.V:
            if v.color == player:
                temp = copy.deepcopy(graph)
                copiedV = PercolationPlayer.GetV(temp, v.index)
                PercolationPlayer.Percolate(temp, copiedV)
                children.append((v, PercolationPlayer.combineHeuristics(temp, player)))
        return children

    def ChooseVertexToRemove(graph, player):
        maxHeur = -999
        chosen = None
        for item in PercolationPlayer.Children(graph, player):
            if item[1] > maxHeur:
                maxHeur = item[1]
                chosen = item[0]
        return chosen

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
