from Laberinto import Laberinto
from Pared import Pared
from Puerta import Puerta
from Habitacion import Habitación
from Bomba import Bomba
from Bicho import Bicho
from Agresivo import Agresivo
from Perezoso import Perezoso
from Boss import Boss
from Orientacion import Orientacion
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste

class Creator:
    def __init__(self):
        pass

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self,lad1,lad2):
        return Puerta(lad1,lad2)

    def fabricarHabitacion(self, num):
        hab = Habitación(num)
        hab.orientaciones.append(self.fabricarNorte())
        hab.orientaciones.append(self.fabricarSur())
        hab.orientaciones.append(self.fabricarEste())
        hab.orientaciones.append(self.fabricarOeste())

        pared_norte = self.fabricarPared()
        hab.ponerElementoEnOrientacion(pared_norte, Norte())
        pared_sur = self.fabricarPared()
        hab.ponerElementoEnOrientacion(pared_sur, Sur())
        pared_este = self.fabricarPared()
        hab.ponerElementoEnOrientacion(pared_este, Este())
        pared_oeste = self.fabricarPared()
        hab.ponerElementoEnOrientacion(pared_oeste, Oeste())
        return hab

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarBomba(self,em):
        return Bomba(em)
    
    def fabricarBicho(self, vidas, poder, posicion, modo):
        return Bicho(modo, vidas, poder, posicion)

    def fabricarAgresivo(self):
        return Agresivo()
    
    
    def fabricarPerezoso(self):
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
