from dataclasses import dataclass
@dataclass
class Interaction:
    c1: int
    c2: int
    GeneID1: str
    GeneID2: str
    Expression_Corr: float
    # in teoria non ci serve perchè non vogliamo che siano nodi
    #def __hash__(self):
    #    return hash(self.Chromosome)

    def __str__(self):
        return f"{self.GeneID1} {self.GeneID2} "
