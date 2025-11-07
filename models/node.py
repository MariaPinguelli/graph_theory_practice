class Node:
    """Classe para representar os Vértices do grafo"""
    def __init__(self, id, label):
        self.id = id
        self.label = label
        self.betweenness = None