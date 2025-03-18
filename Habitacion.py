from Contenedor import Contenedor

class Habitación(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num
        
    def entrar(self, alguien):
        print(f"Estás en una habitación{self.num}")
        alguien.posicion = self

    def __str__(self):
        return "Soy una habitación"