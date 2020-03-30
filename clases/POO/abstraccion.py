
"""
Abstracción
 - Al usuario no le interesa o más bien no le debe interesar funciones más complejas
que tiene consigo el ejecutar una acción, como por ejemplo, al ocupar una lavadora
no tiene porque saber cómo añadir jabón, lavar o centrifugar, sólo debe escoger una temperatura
o dejar la que viene por default y la lavadora debe hacer el resto.

El principio de abstracción conlleva a sólo enfocarnos en lo que necesitamos para realizar
una acción como usuario final y no en todo lo que conlleva por detrás.
"""

class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()


    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')
    
    def _añadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando')


if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
