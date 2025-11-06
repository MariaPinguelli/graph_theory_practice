def calculate_betweenness_centrality(graph):
    queue = []

    for node in graph.nodes:
        # Passo 1: calcular as distâncias mínimas
        distTo, _, stack = bfs(graph, node.id)

        #Passo 2: visitar os vértices do stack em ordem reversa
        for v in stack.reverse():
            

