import math

with open ("D:\projetos\Grafos\Grafos_novo\Trabalho busca\entrada_grafo.txt", "r") as arquivo:
    texto = arquivo.read()
    x = texto.split()
    print(x)
    Total_vertices=int(x[0])
    x.pop(0)
    x=list(map(int, x))
    print(x)
    grafo={}

for i in range(Total_vertices):

    grafo.update({i+1:None})
    print(grafo)

def conectar (chave, novo_valor):
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

print(grafo)
visitado=[]
fila=[]
distancia=0

def bfs(visitado,grafo,node,distancia):
        visitado.append(node)
        fila.append(node)

        while fila:
            m = fila.pop(0)
            print (m,"distancia", math.ceil(distancia / 2)) #no video print(m, end = " ")
            for visinho in grafo[m]:
                if visinho not in visitado:
                    distancia += 1
                    visitado.append(visinho)
                    fila.append(visinho)


print("bora ver se é real")
bfs(visitado ,grafo , 4 ,distancia)





