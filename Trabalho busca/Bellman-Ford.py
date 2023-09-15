def bellman_ford(grafo, origem):
    # Passo 1: Inicialização
    distancias = {}
    predecessores = {}

    for vertice in grafo:
        distancias[vertice] = float('inf')  # Inicializa todas as distâncias como infinito
        predecessores[vertice] = None  # Inicializa todos os predecessores como nulos

    distancias[origem] = 0  # A distância da origem para ela mesma é 0

    # Passo 2: Relaxamento das arestas
    for _ in range(len(grafo) - 1):
        for vertice in grafo:
            for vizinho, peso in grafo[vertice]:
                nova_distancia = distancias[vertice] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = vertice

    # Passo 3: Verificação de ciclos de peso negativo
    for vertice in grafo:
        for vizinho, peso in grafo[vertice]:
            if distancias[vertice] + peso < distancias[vizinho]:
                print("caminho negativo encontrado")
                

    return distancias, predecessores


# Exemplo de uso com o grafo1 fornecido
grafo1 = {
    's': [['t', 6], ['y', 7]],
    't': [['x', 2], ['y', 8], ['z', -4]],
    'x': [['t', -2]],
    'z': [['x', 7], ['s', 2]],
    'y': [['z', 9], ['x', -3]]
}

grafo2 = {
    'a': [['b', -4]],
    'b': [['g', 4]],
    'c': [['d', 6]],
    'd': [['c', -3], ['g', 8]],
    'e': [['f', 3]],
    'f': [['g', 7], ['e', -6]],
    's': [['a', 3], ['c', 5], ['e', 2]],
    'g': []
}




# definindo o grafo e a origem
origem = "s"
grafo= grafo2


distancias, predecessores = bellman_ford(grafo, origem)

# Exibir os resultados
for vertice in grafo:
    print(f"Distância de {origem} para {vertice}: {distancias[vertice]}")
    print(f"Caminho mais curto de {origem} para {vertice}: ", end="")
    caminho = []
    predecessor = vertice
    while predecessor:
        caminho.append(predecessor)
        predecessor = predecessores[predecessor]
    caminho.reverse()
    print(" -> ".join(caminho))
