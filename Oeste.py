from Orientacion import Orientacion

class Oeste(Orientacion):
    def __init__(self):
        super().__init__()

    def ponerElemento(self, elemento, contenedor):
        contenedor.oeste = elemento

    def recorrer(self, func, contenedor):
        if contenedor.oeste != None:
            func(contenedor.oeste)

    def __str__ (self):
        return "Oeste"