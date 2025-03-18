from Orientacion import Orientacion

class Sur(Orientacion):
    def __init__(self):
        super().__init__()
    
    def ponerElemento(self, elemento, contenedor):
        contenedor.sur = elemento

    def recorrer(self, func, contenedor):
        if contenedor.sur != None:
            func(contenedor.sur)

    def __str__(self):
        return "Sur"