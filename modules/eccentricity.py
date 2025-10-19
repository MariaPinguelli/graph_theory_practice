from modules.bfs import bfs

def calculate_eccentricity(graph):
    """ Método para calcular excentricidade dos vértices """
    # A excentricidade de um vértice é o maior caminho de um conjunto de distâncias, 
    # onde cada distância é a distância mínima entre o V e um dos vértices do grafo
    # Então para cada vértice iremos encontrar a distância mínima entre ele e todos
    # os outros vértices, e selecionar a maior distância

    for node in graph.nodes:
        # Passo 1: calcular as distâncias mínimas
        distTo, _ = bfs(graph, node.id)

        # Passo 2: selecionar a excentricidade
        max_distance = 0
        for distance in distTo.values():
            if distance != float('inf') and distance > max_distance:
                max_distance = distance
        
        node.eccentricity = max_distance
        node.distances = distTo