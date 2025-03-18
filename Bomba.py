from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self,em):
        super().__init__(em)
        self.activa = False
    
    """def entrar(self):
        if self.activa:
            print("¡Te has chocado con una bomba!")
        else:
            self.em.entrar()"""

    def esBomba(self):
        return True
    
    def __str__(self):
        return "Soy una bomba"