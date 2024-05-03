from sys import stdin


def read_input():
    graph = {}
    for line in stdin:
        line = line.strip().split()
        u, v, w = line
        try:
            assert int(w)
        except AssertionError:
            print("Error: weight must be a number.")
            return {}
        if not u in graph:
            graph[u] = []
        graph[u].append((v, int(w)))

    for node in graph:
        graph[node] = {i[0]: i[1] for i in graph[node]}
    return graph

def _reverse_graph(graph):
    graph_prime = {}
    for node in graph:
        for edge in graph[node].keys():
            if edge not in graph_prime.keys():
                graph_prime[edge] = {}
            graph_prime[edge][node] = graph[node][edge]
    return graph_prime


def _is_cycle(graph):
    for node in graph:
        # DFS
        visited = list()
        stack = [node]

        while stack:

            item = stack.pop()
            if item in visited:
                cycle = []

                while item not in cycle:
                    cycle.append(item)
                    # get first node of this item's path
                    item = _get_first(graph[item], "key")
                return cycle

            visited.append(item)
            if item in graph:
                all_n_nodes = list(graph[item].keys())
                for item in all_n_nodes:
                    stack.append(item)

    return None


def _get_first(Path, type) -> int:
    first = []
    if type == "value":
        first = []
        for i in Path.values():
            first.append(i)

    if type == "key":
        for i in Path.keys():
            first.append(i)

    return first[0] if first else None


def _prune(Graph, A, arbitrary_node_v_c, arbitrary_node_v_c_in_edges, arbitrary_node_v_c_out_edges):
    for node in list(A):
        if node == arbitrary_node_v_c:
            for node_in in A[node]:
                node_out = arbitrary_node_v_c_out_edges[node_in]
                if node_out not in A:
                    A[node_out] = {}
                A[node_out][node_in] = Graph[node_out][node_in]
        else:
            for dst in list(A[node]):
                if dst == arbitrary_node_v_c:
                    new_node_in = arbitrary_node_v_c_in_edges[node]
                    A[node][new_node_in] = Graph[node][new_node_in]
                    del A[node][dst]
    del A[arbitrary_node_v_c]
    return A, new_node_in
