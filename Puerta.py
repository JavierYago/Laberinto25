from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self, alguien):
        print("Pasando por la puerta")
        if self.abierta:
            if alguien.posicion == self.lado1:
                self.lado2.entrar(alguien)
            else:
                self.lado1.entrar(alguien)
        else:
            print("¡La puerta está cerrada!")

    def abrir(self):
        print("¡La puerta se ha abierto!")
        self.abierta = True

    def cerrar(self):
        print("¡La puerta se ha cerrado!")
        self.abierta = False

    def esPuerta(self):
        return True
    
    def __str__(self):
        return "Soy una puerta"