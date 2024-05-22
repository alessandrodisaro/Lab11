import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}

    def getColori(self):
        return DAO.getAllColori()


    def buildGrafo(self, anno, colore):
        nodi = DAO.getAllNodes(anno, colore)
        self.grafo.add_nodes_from(nodi)
        for nodo in nodi:
            self._idMap[nodo.Product_number] = nodo

        edges = DAO.getAllEdges(anno, colore, self._idMap)
        for arco in edges:
            self.grafo.add_edge(arco.p1, arco. p2, weight=arco.peso)

        return self.grafo.edges, self.getNumNodes(), self.getNumEdges()



    def getNumNodes(self):
        return self.grafo.number_of_nodes()


    def getNumEdges(self):
        return self.grafo.number_of_edges()
