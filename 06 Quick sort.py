"""
-=-=-=-=-=-=-=-=-< Quick Sort >=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        — Tempo no melhor caso: O(n*log(n))
        — Tempo no pior caso: O(n²)
        (Quando o elemento pivot é o maior ou menor elemento.)

>>> Funcionamento:
- lista é dividida em sublistas que são chamados recursivamentes para ordenação.
- Divide para conquistar.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""

def particao(lista, inicio, final):
    pivo = lista[final]
    a = inicio-1
    for b in range(inicio, final):
        if lista[b] <= pivo:
            a += 1
            lista[a], lista[b] = lista[b], lista[a]
    lista[a+1], lista[final] = lista[final], lista[a+1] #Aqui ele colocar o pivot no meio.
    return a+1

def quick_sort(lista, inicio, final):
    if inicio < final:
        posicao = particao(lista, inicio, final)
        # Ordenamos a ESQUERDA:
        quick_sort(lista, inicio, posicao-1)
        # Ordenamos a DIREITA:
        quick_sort(lista, posicao + 1, final)

    return lista
v = [10, 40, 5, 15, 30, 70, 20]
print(quick_sort(v, 0, len(v)-1))
