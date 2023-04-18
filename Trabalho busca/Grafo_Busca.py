from queue import Queue
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#leitura do arqueivo
with open("D:\projetos\Grafos\pyton\Trabalho busca\entrada_grafo.txt", "r") as arquivo:
    texto = arquivo.read()
    x = texto.split()
    print(x)
    Total_vertices = int(x[0])
    x.pop(0)
    x = list(map(int, x))
    print(x)
    grafo = {}
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#criacao das vertices
for i in range(Total_vertices):
    grafo.update({i + 1: None})
    print(grafo)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#funçao de juncao das arestas
def conectar(chave, novo_valor):
    if chave in grafo:
        if grafo[chave] is not None and None in grafo[chave]:
            indice_none = grafo[chave].index(None)
            grafo[chave][indice_none] = novo_valor
        else:
            if grafo[chave] is None:
                grafo[chave] = [novo_valor]
            else:
                grafo[chave].append(novo_valor)
    else:
        grafo[chave] = [novo_valor]


while True:
    if len(x) == 0:
        break
    conectar(x[0], x[1])
    conectar(x[1], x[0])
    print(grafo)
    (x.pop(0))
    (x.pop(0))
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#funçao do BFS
print(grafo)
visitado = []
fila = []


def bfs(visitado, grafo, node):
    visitado.append(node)
    fila.append(node)

    while fila:
        m = fila.pop(0)
        print(m, " ")  # no video print(m, end = " ")

        for visinho in grafo[m]:
            if visinho not in visitado:
                visitado.append(visinho)
                fila.append(visinho)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#funçao da distancia
def distancia(grafo, inicio):
    Q =Queue()
    distance = {k: 9999999 for k in grafo.keys()}
    visited_vertices = set()
    Q.put(inicio)
    visited_vertices.update({inicio})
    while not Q.empty():
        vertex = Q.get()
        if vertex == inicio:
            distance[vertex] = 0
        for u in grafo[vertex]:
            if u not in visited_vertices:
                if distance[u] > distance[vertex] + 1:
                    distance[u] = distance[vertex] + 1
                Q.put(u)
                visited_vertices.update({u})
    return distance

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#chamadas de funçao
comeco = 2
print("bora ver se é real")
bfs(visitado, grafo, comeco)
(print(distancia(grafo, comeco)))
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
