"""
-=-=-=-=-=-=-=-=-< Merge Sort >=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        — Tempo no melhor caso: O(n*log(n))
        — Tempo no pior caso: O(n*log(n))

>>> Funcionamento:
- Divisão de problema em subproblemas.
- Divide a lista continuamente pela metade, ordena e combina.

>>> Exemplo:
                [38, 27, 43, 3, 9, 82, 10]          (1) >>> lista de entrada
                    /              \ 
            [38, 27, 43, 3]       [9, 82, 10]
             /         \            /      \ 
        [38, 27]     [43, 3]    [9, 82]     [10]
        /     \      /     \    /   \          \ 
    [38]     [27] [43]    [3] [9]    [82]      [10]   (2) >>> Depois de separado, vamos ordenar.
     \       /      \     /    \     /          /
     [27, 38]       [3, 43]    [9, 82]        [10]
        \            /             \          /
        [3, 27, 38, 43]         [9, 10, 82]
                \                   /
                [3, 9, 10, 27, 38, 43, 82]            (3) >>> Ordenado

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""


def merge_sort(lista):
    if len(lista) > 1: 
        # (1) Para quebramos em valores separados, precisamos fazer uma função recursiva.
        divisao = len(lista) // 2
        esquerda = lista[:divisao]
        direita = lista[divisao:]
        merge_sort(esquerda)
        merge_sort(direita)
        a = b = c = 0

        # (2) Ordena esquerda e direita:
        while a < len(esquerda) and b < len(direita):
            if esquerda[a] < direita[b]:
                lista[c] = esquerda [a]
                a+=1
            else:
                lista[c] = direita[b]
                b += 1
            c += 1
        
        # (3) Ordenação final.
        while a < len(esquerda):
            lista[c] = esquerda[a]
            a += 1
            c += 1
        while b < len(direita):
            lista[c] = direita[b]
            b += 1
            c += 1
    return lista

v = [10, 40, 5, 15, 30, 70, 20]
print(merge_sort(v))

