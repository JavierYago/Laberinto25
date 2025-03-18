from Pared import Pared

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("Te has chocado con una Pared Bomba")

    def __str__(self):
        return "Soy una pared bomba"