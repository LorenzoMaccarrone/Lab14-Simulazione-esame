import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._allCromosomi = DAO.getAllCromosomi()
        self._grafo = nx.DiGraph()

    def creaGrafo(self):
        self._grafo.add_nodes_from(self._allCromosomi)
        self._allGenes= DAO.getAllGenes()
        for a in self._allCromosomi:
            for b in self._allCromosomi:
                if a!=b:
                    listaCorretta= DAO.getAllInteractions(a,b)
                    if len(listaCorretta)!=0:
                        peso = self.calcolaPeso(listaCorretta)
                        self._grafo.add_edge(a, b, weight=peso)

    def calcolaPeso(self, lista):
        peso=0
        for a in lista:
            peso+=a.Expression_Corr
        return peso
    def getValMin(self):
        listaArchi = list(self._grafo.edges(data=True))
        listaArchi.sort(key=lambda x: x[2]["weight"])
        return listaArchi[0][2]["weight"]
        #con [0] indichiamo che vogliamo il primo elemento della lista mentre con
        #[2]["weight"] indichiamo che, di tutto l'arco, vogliamo solo l'informazione sul peso
    def archiMinori(self,soglia):
        listaArchi = list(self._grafo.edges(data=True))
        count=0
        for a in listaArchi:
            if a[2]["weight"]<soglia:
                count+=1
        return count


    def archiMaggiori(self,soglia):
        listaArchi = list(self._grafo.edges(data=True))
        count = 0
        for a in listaArchi:
            if a[2]["weight"] > soglia:
                count += 1
        return count

    def getValMax(self):
        listaArchi = list(self._grafo.edges(data=True))
        listaArchi.sort(key=lambda x: x[2]["weight"], reverse = True)
        return listaArchi[0][2]["weight"]

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)







