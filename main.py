from modules.graph_reader import read_and_format_data
from modules.betweenness import calculate_betweenness_centrality
from modules.print_results import print_results

def main():
    # Tratar dados de entrada
    graph = read_and_format_data()

    # Calcular betweenness centrality dos vértices
    calculate_betweenness_centrality(graph)

    # Imprime resultados no terminal, e guarda em arquivos txt
    print_results(graph)

if __name__ == '__main__':
    main()