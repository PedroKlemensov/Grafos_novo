teste={1: None, 2: None, 3: None, 4: None, 5: None}

x=['1', '2', '2', '5', '5', '3', '4', '5', '1', '5']
x=list(map(int, x))
print(x)

def conectar (chave, novo_valor):
    if chave in teste:
        if teste[chave] is not None and None in teste[chave]:
            indice_none = teste[chave].index(None)
            teste[chave][indice_none] = novo_valor
        else:
            if teste[chave] is None:
                teste[chave] = [novo_valor]
            else:
                teste[chave].append(novo_valor)
    else:
        teste[chave] = [novo_valor]



print(teste)
while True:
    if len(x) == 0:
        break
    conectar(x[0], x[1])
    conectar(x[1], x[0])
    (x.pop(0))
    (x.pop(0))

print(teste)
vetor=[teste(1)]
print(vetor)

