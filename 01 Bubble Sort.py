"""
-=-=-=-=-=-=-=-=-<  Bubble Sort  >=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        — Tempo no melhor caso: O(n)
        — Tempo no pior caso: O(n²)


DICAS:

A variável 'fazendoTrocas' faz com que caso parte da lista já esteja ordenado, o
algoritmo não volte do inicio para fazer novas checagens, ou seja, um pouco mais de
rapidez.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

def Bubble_sort(lista):
    indice = len(lista)-1

    fazendoTrocas = True
    while fazendoTrocas:
        fazendoTrocas = False
        for x in range(indice):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]
                fazendoTrocas = True
    return lista
    
v = [10, 40, 5, 15, 30, 70, 20]
print(Bubble_sort(v))
