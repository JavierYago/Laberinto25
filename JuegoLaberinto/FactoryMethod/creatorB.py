from Laberinto.juego import ParedBomba
from FactoryMethod.creator import Creator
class CreatorB(Creator):
    def fabricarPared(self):
        return ParedBomba()