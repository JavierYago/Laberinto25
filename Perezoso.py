from Modo import Modo
import time

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Perezoso: Voy a descansar un pocZzzzzzzzzzzzzz....")
        time.sleep(5)

    def camina(self, bicho):
        print("Perezoso: No me apetece caminar")

    def atacar(self, bicho):
        print("Perezoso: Intentaré atacar... pero no prometo nada")

    def __str__(self):
        return "Soy un Bicho Perezoso"