
grafo_result={
        1:[2,5],
        2:[1,5],
        3:[5],
        4:[5],
        5:[1,2,3,4]
    }

visitado=[]
fila=[]

def bfs(visitado,grafo,node):
        visitado.append(node)
        fila.append(node)

        while fila:
            m = fila.pop(0)
            print (m," ") #no video print(m, end = " ")

            for visinho in grafo[m]:
                if visinho not in visitado:
                    visitado.append(visinho)
                    fila.append(visinho)

print("bora ver se é real")
bfs(visitado ,grafo_result , 2)







