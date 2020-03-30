
"""
Ordenamiento de Burbuja

    - EL ordenamiento de burbuja es un algoritmo que 
    recorre repetidamente una lista que necesita ordenarse. 
    Compara los elementos adyacentes y los intercambia 
    si están en el orden incorrecto. Este procedimiento 
    se repite hasta que no se requieren más intercambios,
    lo que indica que la lista se encuentra ordenada.

"""

import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) => O(n * n) Crecimiento polinominial

            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

if __name__ == "__main__":
    tamano_de_lista = int(input('De qué tamaño será la lista?'))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

