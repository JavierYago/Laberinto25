from Orientacion import Orientacion

class Norte(Orientacion):
    def __init__(self):
        super().__init__()

    def ponerElemento(self, elemento, contenedor):
        contenedor.norte = elemento

    def recorrer(self, func, contenedor):
        if contenedor.norte != None:
            func(contenedor.norte)

    def __str__ (self):
        return "Norte"