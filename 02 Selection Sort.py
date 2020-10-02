"""
-=-=-=-=-=-=-=-=-<  Selection Sort  >=-=-=-=-=-=

        — Tempo no melhor caso: O(n²)
        — Tempo no pior caso: O(n²)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""

def Selection_sort(lista):

    for a in range(len(lista)):
        menor = a
        for b in range(a+1, len(lista)):
            if lista[b] < lista[menor]:
                menor = b 
        lista[menor], lista[a] = lista[a], lista[menor]
    return lista

v = [10, 40, 5, 15, 30, 70, 20]
print(Selection_sort(v))