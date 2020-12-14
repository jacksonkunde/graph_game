#okok
from benchmark import *
from util import *

class PercolationPlayer:
    def GetE(graph, v):
        return [e for e in graph.E if (e.a == v or e.b == v)]

    def GetV(graph, i):
        for v in graph.V:
            if v.index == i:
                return v
        return None

    def ChooseVertexToColor(graph, player):
        currMax = -999
        chosen = None
        for i in [v for v in graph.V if v.color == -1]:
            if len(PercolationPlayer.GetE(graph, i)) > currMax:
                currMax = len(PercolationPlayer.GetE(graph, i))
                chosen = i
        return PercolationPlayer.GetV(graph, chosen.index)

    def Percolate(graph, v):
        for e in PercolationPlayer.GetE(graph, v):
            graph.E.remove(e)
        graph.V.remove(v)
        to_remove = {u for u in graph.V if len(PercolationPlayer.GetE(graph, u)) == 0}
        graph.V.difference_update(to_remove)

    def RedmondHeuristic(graph, player):
        return len([v for v in graph.V if v.color == player]) - len([u for u in graph.V if u.color != player])

    def VDegSumHeuristic(graph, player):
        oursum = 0
        opposum = 0
        for v in graph.V:
            degree = len(PercolationPlayer.GetE(graph,v))
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

        return normalizedRedmondHeuristic + normalizedVDegHeuristic

    #at two degrees if graph smaller than 10 vertices
    def Children(graph, player):
        maxheur = -999
        result = None
        if len(graph.V) > 10:
            for v in [vertex for vertex in graph.V if vertex.color == player]:
                temp = copy.deepcopy(graph)
                PercolationPlayer.Percolate(temp, PercolationPlayer.GetV(temp, v.index))
                current = PercolationPlayer.combineHeuristics(temp, player)
                if current > maxheur:
                    maxheur = current
                    result = v
            return result
        else:
            for v in [vertex for vertex in graph.V if vertex.color == player]:
                temp = copy.deepcopy(graph)
                PercolationPlayer.Percolate(temp, PercolationPlayer.GetV(temp, v.index))
                ourH = PercolationPlayer.combineHeuristics(temp, player)
                theirH = 999
                for ve in [vert for vert in temp.V if vert.color == 1-player]:
                    temp2 = copy.deepcopy(temp)
                    PercolationPlayer.Percolate(temp2, PercolationPlayer.GetV(temp2, ve.index))
                    ok = (-1)*PercolationPlayer.combineHeuristics(temp2, 1-player)
                    if ok < theirH:
                        theirH = ok
                if ourH+theirH > maxheur:
                    maxheur = ourH+theirH
                    result = v
            return result

    def ChooseVertexToRemove(graph, player):
        return PercolationPlayer.Children(graph, player)

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
