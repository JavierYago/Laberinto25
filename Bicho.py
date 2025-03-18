import Agresivo, Perezoso, Boss
from Modo import Modo
from Ente import Ente

class Bicho:
    def __init__(self, vidas, poder, posicion, modo):
        self.vidas = vidas
        self.poder = poder
        self.modo = modo
        self.posicion = posicion
        
    def actua(self):
        while self.estaVivo():
            self.modo.actua(self)

    """def esAgresivo(self):
        return self.modo.esAgresivo()
    
    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def esBoss(self):
        return self.modo.esBoss()"""

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

    def iniBoss(self):
        self.modo = Boss()
        self.poder = 20
        self.vidas = 10

    def estaVivo(self):
        return self.vidas > 0
    
    def __str__(self):
        return "Soy un bicho con "+str(self.vidas)+" vidas y "+str(self.poder)+" de poder"