from Modo import Modo
import time
class Boss(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self):
        print("El bicho Boss no está durmiendo")
        time.sleep(0)

    def atacar(self):
        print("El bicho Boss ataca con fuerza")
        

    def __str__(self):
        return "Soy el Bicho Boss del laberinto"