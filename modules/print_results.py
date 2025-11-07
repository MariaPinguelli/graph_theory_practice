import os

def print_results(graph):
    """Imprime na tela e salva em arquivos"""
    
    print("\n" + "="*50)
    print("BETWEENNESS:")
    for node in graph.nodes:
        print(f"{node.id} ({node.label}): {node.betweenness:.4f}")
    
    os.makedirs("output", exist_ok=True)
    
    with open("output/saida.txt", "w") as f:
        for node in graph.nodes:
            f.write(f"{node.id} {node.betweenness}\n")