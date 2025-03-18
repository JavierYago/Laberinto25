class Modo:
    def __init__(self):
        pass

    def actuar(self, unBicho):
        self.dormir(unBicho)
        self.camina(unBicho)
        self.atacar(unBicho)

    def dormir(self, bicho):
        pass

    def camina(self, bicho):
        pass

    def atacar(self, bicho):
        pass

    def __str__(self):
        return "Modo"

