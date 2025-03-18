from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self, alguien):
        print("¡Te has chocado con una pared")

    def __str__(self):
        return "Soy una pared"