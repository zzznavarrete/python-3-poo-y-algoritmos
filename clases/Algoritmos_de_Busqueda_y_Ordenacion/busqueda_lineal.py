
"""
Búsqueda lineal

    - Busca en todos los elementos de manera secuencial
    - ¿Cuál es el peor caso? -> que el loop depende del largo del input, -> O(n)
"""
import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n) <- Cuando tenemos un loop que depende de un input
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    tamano_de_lista = int(input('De qué tamaño será la lista?'))
    objetivo = int(input('Qué número quieres encontrar?'))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo}  {"está" if encontrado else "no está"} en la lista')