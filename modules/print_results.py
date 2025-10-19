import os

def print_results(graph):
    """Imprime na tela e salva em arquivos"""
    
    print("\n" + "="*50)
    print("EXCENTRICIDADE:")
    for node in graph.nodes:
        print(f"{node.id} ({node.label}): {node.eccentricity}")
    
    print("\nCLOSENESS CENTRALITY:")
    for node in graph.nodes:
        print(f"{node.id} ({node.label}): {node.closeness:.6f}")
    
    os.makedirs("output", exist_ok=True)
    
    with open("output/eccentricity.txt", "w") as f:
        for node in graph.nodes:
            f.write(f"{node.id} {node.eccentricity}\n")
    
    with open("output/closeness_centrality.txt", "w") as f:
        for node in graph.nodes:
            f.write(f"{node.id} {node.closeness:.6f}\n")