import time
from Modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def esAgresivo(self):
        return True
    
    def dormir(self, bicho):
        print("Agresivo: Voy a descansar un poco ....")
        time.sleep(1)

    def caminar(self,bicho):
        print("Agresivo:Buscando al jugador ....")

    def atacar(self,bicho):
        print("Agresivo: Atacando al jugador ....")

    def __str__(self):
        return "Soy un Bicho Agresivo"