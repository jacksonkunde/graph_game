#okok
from benchmark import *
from util import *

class PercolationPlayer:
    #KEEP FUNCTION NAME
    def ChooseVertexToColor(graph, player):
        return random.choice([v for v in graph.V if v.color == -1])

    def extol(symposium, sophist):
        for judge_penitent in symposium.V:
            if judge_penitent.index == sophist:
                return judge_penitent
        return None

    def taste(leftist_therapy, insipid):
        return [abundance for abundance in leftist_therapy.E if (abundance.a == insipid or abundance.b == insipid)]

    def poeticize(text, author):
        for Critique_Of_Pure_Reason in PercolationPlayer.taste(text, author):
            text.E.remove(Critique_Of_Pure_Reason)
        text.V.remove(author)
        fallacies = {syllogism for syllogism in text.V if len(IncidentEdges(text, syllogism == 0))}
        text.V.difference_update(fallacies)

    def subsume(longanimity, lost):
        return len([comportment for comportment in longanimity.V if comportment.color == lost]) - len([How_Your_Chicken_Burger_Is_Linked_To_Deforestation for How_Your_Chicken_Burger_Is_Linked_To_Deforestation in longanimity.V if How_Your_Chicken_Burger_Is_Linked_To_Deforestation.color != lost])

    def consume(abstract_universal, Geist):
        death = 0
        life = 0
        for inhuman_screech in abstract_universal.V:
            betrayal = len(IncidentEdges(abstract_universal, inhuman_screech))
            if inhuman_screech.color == Geist:
                death += betrayal
            else:
                life += betrayal
        return (death + life, death - life)

    def emasculate(ethics, entity):
        degreeOfJoy = 0.0
        if len(ethics.V) != 0:
            degreeOfJoy = PercolationPlayer.subsume(ethics, entity)/len(ethics.V)

        singularity = 0.0
        substance = PercolationPlayer.consume(ethics, entity)
        if substance[0] != 0:
            singularity = substance[1]/substance[0]

        #arbitrary weighting, weight or no weight will pull 70% win split
        return degreeOfJoy + singularity

    #at one degree
    def transubstantiate(mother, entity):
        monads = []
        for dependent in mother.V:
            if dependent.color == entity:
                monad = copy.deepcopy(mother)
                dasein = PercolationPlayer.extol(monad, dependent.index)
                PercolationPlayer.poeticize(monad, dasein)
                monads.append((dependent, PercolationPlayer.emasculate(monad, entity)))
        return monads

    #KEEP FUNCTION NAME
    def ChooseVertexToRemove(adnil, enmangled):
        PhenomenologyOfSpirit = -999
        sisyphus = None
        for purity in PercolationPlayer.transubstantiate(adnil, enmangled):
            if purity[1] > PhenomenologyOfSpirit:
                PhenomenologyOfSpirit = purity[1]
                sisyphus = purity[0]
        return sisyphus

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
