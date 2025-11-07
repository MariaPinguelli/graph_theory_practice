from collections import deque

def calculate_betweenness_centrality(graph):
    """ Método para calcular excentricidade dos vértices """
    # A betweenness, ou intermediação, mede qual a frequência
    # em que dado vértice aparece no caminho mais curto entre o outros vértices do grafo
    # Esta medida consegue nos mostrar numa rede de conexões pessoas influentes;
    # Numa análise de redes de computadores onde pode ter um gargalo de conexões;
    # Ou até onde temos gargalos no trânsito a se resolver

    # Inicializa centralidade de todos os vértices
    for node in graph.nodes:
        node.betweenness = 0.0

    # Percorre cada nó como source da busca
    for source in graph.nodes:
        # Passo 1: inicialização
        stack = []  # para registrar a ordem dos nós visitados
        predecessors = {n.id: [] for n in graph.nodes}
        pathway_count = {n.id: 0 for n in graph.nodes}
        distance = {n.id: -1 for n in graph.nodes}

        pathway_count[source.id] = 1
        distance[source.id] = 0

        queue = deque([source.id])

        # Passo 2: BFS
        while queue:
            v_id = queue.popleft()
            stack.append(v_id)

            for neighbor_id in graph.adjacency[v_id]:
                # Se o vizinho ainda não foi visitado
                if distance[neighbor_id] < 0:
                    distance[neighbor_id] = distance[v_id] + 1
                    queue.append(neighbor_id)

                # Se encontramos um caminho mais curto até o vizinho
                if distance[neighbor_id] == distance[v_id] + 1:
                    pathway_count[neighbor_id] += pathway_count[v_id]
                    predecessors[neighbor_id].append(v_id)

        # Passo 3: acumular dependências
        dependency = {n.id: 0.0 for n in graph.nodes}

        # Processa os nós na ordem inversa de visita
        while stack:
            w_id = stack.pop()
            for v_id in predecessors[w_id]:
                if pathway_count[w_id] != 0:
                    proporcao = pathway_count[v_id] / pathway_count[w_id]
                    dependency[v_id] += proporcao * (1 + dependency[w_id])
            if w_id != source.id:
                # soma dependência ao valor de betweenness do nó
                node = next(n for n in graph.nodes if n.id == w_id)
                node.betweenness += dependency[w_id]

    # Passo 4: normalização
    n = len(graph.nodes)
    scale = ((n - 1) * (n - 2)) / 2.0

    for node in graph.nodes:
        node.betweenness /= scale

