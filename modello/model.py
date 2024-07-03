import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def getSetAlbum(self, a1, dTot):
        connessa = nx.node_connected_component(self._graph, a1)
        self._bestSet = None
        self._bestScore = 0
        parziale = set(a1)
        # non mi serve
        connessa.remove(a1)
        self.ricorsione(parziale, connessa, dTot)
        return self._bestSet

    def ricorsione(self, parziale, connessa, dTot):
        # verificare se parziale è una soluzione ammissibile
        if self.durataTot(parziale) > dTot:
            return
        # verificare se parziale è migliore del best
        if len(parziale) > len(self._bestSet):
            self._bestSet = copy.deepcopy(parziale)
            self._bestScore = len(parziale)
        # ciclo su nodi raggiungibili
        for vicino in connessa:
            if vicino not in parziale:
                parziale.add(vicino)
                rimanenti=copy.deepcopy(connessa)
                rimanenti.remove(vicino)
                # ricorsione
                self.ricorsione(parziale, connessa, dTot)
                parziale.pop()


    def durataTot(self, listOfNodes):
        score = 0
        for n in listOfNodes:
            score += n.totD
        return toMillisec(score)

    def buildGraph(self, d):
        self._graph.clear()
        self._graph.add_nodes_from(DAO.getAlbums(toMillisec(d)))
        self._idMap = {a.AlbumId: a for a in list(self._graph.nodes)}
        # for a in list(self._graph.nodes):
        #     self._idMap[a.AlbumId] = a
        edges = DAO.getEdges(self._idMap)
        self._graph.add_edges_from(edges)

    def getConnessaDetails(self, v0):
        conn = nx.node_connected_component(self._graph, v0)
        durataTOT = 0
        for album in conn:
            durataTOT += toMinutes(album.totD)

        return len(conn), durataTOT

    def getGraphDeails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getNodes(self):
        return list(self._graph.nodes)

    def getGraphSize(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getNode(self,i):
        return self._idMap[i]


def toMillisec(d):
    return d * 60 * 1000


def toMinutes(d):
    return d / 1000 / 60
