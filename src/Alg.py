from sys import maxsize
from utils.helpers import _reverse_graph, _is_cycle, _get_first, _prune


class Alg:
    def __init__(self, root) -> None:
        self.root = root

    # Postavení grafu
    def _construct_weighted_graph(self, graph):
        graph_prime = {}
        rev = _reverse_graph(graph)

        for node in rev:
            if node == self.root:
                continue
            else:
                index = maxsize
                highest = maxsize
                for edge in rev[node].keys():
                    if rev[node][edge] <= highest:
                        index = edge
                        highest = rev[node][edge]
                graph_prime[node] = {index: highest}

        graph_prime[self.root] = {}
        return graph_prime

    # Algoritmus
    def execute(self, Graph):
        pi = self._construct_weighted_graph(Graph)
        cycle = _is_cycle(pi)
        if not cycle:
            P = _reverse_graph(pi)
            return P

        arbitrary_node_v_c = maxsize
        arbitrary_node_v_c_in_edges = {}
        arbitrary_node_v_c_out_edges = {}

        D_prime = {}

        for u in Graph:
            for v in Graph[u]:

                case_1 = (not u in cycle) and (v in cycle)
                case_2 = (u in cycle) and (not v in cycle)
                case_3 = (not u in cycle) and (not v in cycle)

                if case_1:

                    if u not in D_prime:
                        D_prime[u] = {}
                    w_prime_e = Graph[u][v] - _get_first(pi[v], "value")

                    if (arbitrary_node_v_c not in D_prime[u]) or (
                        arbitrary_node_v_c in D_prime[u] and D_prime[u][arbitrary_node_v_c] > w_prime_e
                    ):
                        D_prime[u][arbitrary_node_v_c] = w_prime_e

                        arbitrary_node_v_c_in_edges[u] = v

                elif case_2:

                    if arbitrary_node_v_c not in D_prime:
                        D_prime[arbitrary_node_v_c] = {}

                    w_prime_e = Graph[u][v]

                    if (v not in D_prime[arbitrary_node_v_c]) or (
                        v in D_prime[arbitrary_node_v_c] and D_prime[arbitrary_node_v_c][v] > w_prime_e
                    ):
                        D_prime[arbitrary_node_v_c][v] = w_prime_e

                        arbitrary_node_v_c_out_edges[v] = u

                elif case_3:

                    if u not in D_prime:
                        D_prime[u] = {}

                    D_prime[u][v] = Graph[u][v]

        # Rekurzivní hledání stroku od kořenu
        A = self.execute(D_prime)

        A_prime, incoming_node = _prune(
            Graph, A, arbitrary_node_v_c, arbitrary_node_v_c_in_edges, arbitrary_node_v_c_out_edges
        )

        for node in cycle:
            if node != incoming_node:
                first = _get_first(pi[node], "key")
                if not first in A_prime:
                    A_prime[first] = {}
                A_prime[first][node] = pi[node][first]

        return A_prime
