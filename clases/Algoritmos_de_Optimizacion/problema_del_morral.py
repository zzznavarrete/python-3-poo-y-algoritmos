
"""
Problema del morral. (1-0)

    - Somos un ladrón que quiere entrar a un museo, pero sólo tenemos 1 mochila para cargar cosas
    y hay muchísimas más cosas de las que puedo cargar.
    Tengo que escoger cuales son los artículos que puedo meter a mi mochila que me garantizan
    que tendré el mayor valor posible. (Puedo tomar una cosa o no tomarla solamente)

"""

def morral(tamano_morral, pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)
    
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n -1))



    


if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    # Con una capacidad de 30, podríamos llevarnos el que pesa 30, pero lo más óptimo sería
    # llevarnos el de 10 y el de 20, porque ambos valen más (160) que el de 30 solo (120)
    tamano_morral = 30
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)


