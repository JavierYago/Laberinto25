from Orientacion import Orientacion

class Este(Orientacion):

    def __init__(self):
        super().__init__()

    def ponerElemento(self, elemento, contenedor):
        contenedor.este = elemento

    def recorrer(self, func, contenedor):
        if contenedor.este != None:
            func(contenedor.este)

    def __str__ (self):
        return "Este"