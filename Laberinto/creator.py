from juego import Habitación, Pared, Puerta, Laberinto, ParedBomba, Bomba, Agresivo, Perezoso, Boss, Norte, Sur, Este, Oeste

class Creator:
    def __init__(self):
        pass

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

    def fabricarHabitacion(self, num):
        hab = Habitación(num)
        hab.norte = self.fabricarPared()
        hab.sur = self.fabricarPared()
        hab.este = self.fabricarPared()
        hab.oeste = self.fabricarPared()
        return hab

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarBomba(self,em):
        return Bomba(em)

    def fabricarBichoAgresivo(self):
        return Agresivo()
    
    def fabricarBichoPerezoso(self):
        return Perezoso()
    
    def fabricarBoss(self):
        return Boss()
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()


class CreatorB(Creator):
    def fabricarPared(self):
        return ParedBomba()