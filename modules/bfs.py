from collections import deque

def bfs(graph, start_node_id):
    """
    Breadth-First Search para calcular distâncias mínimas
    Retorna: dicionário com distâncias mínimas do start_node_id para todos os nós
    """
    marked = {}
    distTo = {}
    edgeTo = {}
    
    for node in graph.nodes:
        marked[node.id] = False
        distTo[node.id] = float('inf')
        edgeTo[node.id] = None
    
    distTo[start_node_id] = 0
    marked[start_node_id] = True
    
    queue = deque([start_node_id])
    
    while queue:
        current_node_id = queue.popleft()
        
        for neighbor_id in graph.adjacency[current_node_id]:
            if not marked[neighbor_id]:
                marked[neighbor_id] = True
                edgeTo[neighbor_id] = current_node_id
                distTo[neighbor_id] = distTo[current_node_id] + 1
                queue.append(neighbor_id)
    
    return distTo, edgeTo

def has_path_to(distTo, node_id):
    """Verifica se há caminho para o nó"""
    return distTo[node_id] != float('inf')

def distance_to(distTo, node_id):
    """Retorna a distância mínima para o nó"""
    return distTo[node_id]

def path_to(edgeTo, start_node_id, target_node_id):
    """Retorna o caminho mínimo do start para o target"""
    if not has_path_to({target_node_id: edgeTo.get(target_node_id)}, target_node_id):
        return None
    
    path = []
    current = target_node_id
    
    while current != start_node_id:
        path.append(current)
        current = edgeTo[current]
    
    path.append(start_node_id)
    path.reverse()
    return path