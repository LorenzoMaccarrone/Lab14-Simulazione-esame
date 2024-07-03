from dataclasses import dataclass
@dataclass
class Cromosoma:
    GeneID: str
    Function: str
    Essential: str
    Chromosome: int

    def __hash__(self):
        return hash(self.Chromosome)

    def __str__(self):
        return f"{self.GeneID} {self.Chromosome} "
