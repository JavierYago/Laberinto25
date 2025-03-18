class ElementoMapa:
    def __init__(self):
        self.padre = None

    def entrar(self, alguien):
        pass

    def recorrer(self, func):
        pass
    
    def esPuerta(self):
        return False
    
    def __str__(self):
        return "Soy un ElementoMapa"
