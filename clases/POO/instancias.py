

class Coordenada:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    # Diferencia al cuadrado de 2 coordenadas
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == "__main__":
    # Creando instancias de la clase Coordenada
    coord_1 = Coordenada(3,30)
    coord_2 = Coordenada(4,8)
    print(coord_1.distancia(coord_2))

    # Preguntando si coord_2 es instancia de coordenada
    print(isinstance(coord_2, Coordenada))