class Graph:
    """Classe para representar o grafo"""
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

        self.adjacency = self.__create_adjacency_list()
    
    def __create_adjacency_list(self):
        """Método privado para criar lista de adjacências"""
        adjacency = {}
        
        for node in self.nodes:
            adjacency[node.id] = []
        
        for edge in self.edges:
            adjacency[edge.source].append(edge.target)
            adjacency[edge.target].append(edge.source)
            
        return adjacency