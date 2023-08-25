# DFS - Algoritmo para busca em profundidade

# Função para imprimir a DFS do grafo recebe o primeiro nó a ser visitado
def dfs(graph, start):
    visited = set()  # Conjunto para acompanhar os nós visitados
    stack = [start]  # Pilha para a busca em profundidade

    while stack:

        node = stack.pop()  # Pega o próximo nó da pilha

        if node not in visited:
            if node == entrada:
                print("Nó visitado: ", node, "Objetivo? Sim")
            else:
                print("Nó visitado: ", node, "Objetivo? Não")
            visited.add(node)    # Marca o nó como visitado
            # Adiciona vizinhos não visitados à pilha
            stack.extend(graph[node] - visited)


# Exemplo de um grafo representado como um dicionário de adjacências
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

start_node = 'A'  # Nó de início da busca
while True:
    entrada = input("Escolha uma letra objetivo (entre 'A' e 'F'): ").upper()

    if entrada in ('A', 'B', 'C', 'D', 'E', 'F'):
        print("Letra escolhida: ", entrada)
        print("----------")
        break
    else:
        print("Aí você é um imbecil")


print("Resultado da busca em profundidade:")
dfs(graph, start_node)
