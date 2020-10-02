"""
-=-=-=-=-=-=-=-=-< Shell Sort  >=-=-=-=-=-=

        — Tempo no melhor caso: O(n*log(n))
        — Tempo no pior caso: O(n²)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

def shell_sort(lista):
    intervalo = len(lista) // 2
    while intervalo > 0:
        for a in range(intervalo, len(lista)): 
            temp = lista[a]
            b = a
            while b >= intervalo and lista[b - intervalo] > temp:
                lista[b] = lista[b - intervalo]
                b -= intervalo
            lista[b] = temp
        intervalo = intervalo // 2
    return lista

v = [10, 40, 5, 15, 30, 70, 20]
print(shell_sort(v))