"""
-=-=-=-=-=-=-=-=-< Insertion Sort  >=-=-=-=-=-=

        — Tempo no melhor caso: O(n)
        — Tempo no pior caso: O(n²)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""

def Insertion_sort(lista):
    for a in range(1, len(lista)):
        chave = lista[a]
        b = a -1
        while b >= 0 and lista[b] > chave:
            lista[b+1] = lista[b]
            b -= 1
        lista[b + 1] = chave 
    return lista

v = [10, 40, 5, 15, 30, 70, 20]
print(Insertion_sort(v))