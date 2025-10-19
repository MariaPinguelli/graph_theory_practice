import xml.etree.ElementTree as ET

from models.node import Node
from models.edge import Edge
from models.graph import Graph

INPUT_FILE_NAME = 'data/LesMiserables.gexf'

def read_and_format_data():
    """ Método para leitura do grafo usando XML parser """
    nodes = []
    edges = []

    tree = ET.parse(INPUT_FILE_NAME)
    root = tree.getroot()
    
    ns = {'gexf': 'http://www.gexf.net/1.1draft'}
    
    for node in root.findall('.//gexf:node', ns):
        node_id = node.get('id')
        label = node.get('label', node_id)
        nodes.append(Node(node_id, label))
    
    for edge in root.findall('.//gexf:edge', ns):
        edge_id = edge.get('id')
        source = edge.get('source')
        target = edge.get('target')
        edges.append(Edge(edge_id, source, target))
      
    return Graph(nodes, edges)