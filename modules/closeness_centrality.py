def calculate_closeness_centrality(graph):
    """ Método para calcular closeness centrality dos vértices """
    # Closeness centrality, ou Coeficiente de Proximidade é o valor que indica quão 
    # conectado o vértice é ao grafo
    # É a média das distâncias do vértice até os outros vértices do grafo
    # para cacular vamos usar (Quantidade de Vértices - 1) / Soma das distâncias
    # o (- 1) é para retirar o vértice  atua da conta
    n = len(graph.nodes)

    for node in graph.nodes:
        sum_distances = sum(dist for dist in node.distances.values() if dist != float('inf'))
        node.closeness = ((n - 1) / (sum_distances))