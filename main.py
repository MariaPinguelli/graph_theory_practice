from modules.graph_reader import read_and_format_data
from modules.eccentricity import calculate_eccentricity
from modules.closeness_centrality import calculate_closeness_centrality
from modules.print_results import print_results

def main():
    # Tratar dados de entrada
    graph = read_and_format_data()

    # Calcular excentricidade do grafo
    calculate_eccentricity(graph)

    # Calcular closeness centrality dos vértices
    calculate_closeness_centrality(graph)

    # Imprime resultados no terminal, e guarda em arquivos txt
    print_results(graph)

if __name__ == '__main__':
    main()