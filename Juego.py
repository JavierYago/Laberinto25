from Laberinto import Laberinto
from Habitacion import Habitación
from Pared import Pared
from Puerta import Puerta
from Bicho import Bicho
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste
from Orientacion import Orientacion
from Agresivo import Agresivo
from Perezoso import Perezoso
from Boss import Boss
from Bomba import Bomba
from ParedBomba import ParedBomba
from Ente import Personaje

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []
        self.personaje = None
        self.bicho_threads = {}

    def agregar_bicho(self, bicho):
        bicho.juego = self
        self.bichos.append(bicho)

    """def eliminar_bicho(self, bicho):
        self.bichos.remove(bicho) """

    """ def iniciar_juego(self):
        print("¡Bienvenido al juego del laberinto!")
        # Aquí puedes agregar la lógica para iniciar el juego """
    
    def lanzarBicho(self, bicho):
        import threading
        thread = threading.Thread(target=bicho.actua)
        if bicho not in self.bicho_threads:
            self.bicho_threads[bicho] = []
        self.bicho_threads[bicho].append(thread)
        thread.start()

    def terminarBicho(self, bicho):
        if bicho in self.bicho_threads:
            for thread in self.bicho_threads[bicho]:
                bicho.vidas=0

    def agregarPersonaje(self, name):
        self.personaje = Personaje(10,1,None,self, name)
        self.laberinto.entrar(self.personaje)

    def abrir_puertas(self):
        def abrirPuertas(obj):
            if obj.esPuerta():
                obj.abrir()
        self.laberinto.recorrer(abrirPuertas)

    def cerrar_puertas(self):
        def cerrarPuertas(obj):
            if obj.esPuerta():
                obj.cerrar()
        self.laberinto.recorrer(cerrarPuertas)

    def crearLaberinto2Habitaciones(self):
        self.laberinto = Laberinto()
        hab1 = Habitación(1)
        hab1.este = Pared()
        hab1.oeste = Pared()
        hab1.norte = Pared()

        hab2 = Habitación(2)
        hab2.sur = Pared()
        hab2.este = Pared()
        hab2.oeste = Pared()

        puerta = Puerta(hab1, hab2)
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto.agregar_habitacion(hab1)
        self.laberinto.agregar_habitacion(hab2)
        return self.laberinto

    def crearLaberinto2HabitacionesFM(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)
        puerta = creator.fabricarPuerta(hab1, hab2)
        hab1.ponerElementoEnOrientacion(puerta, Norte())
        hab2.ponerElementoEnOrientacion(puerta, Sur())

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto        
    
    def crearLaberinto2HabitacionesFMD(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)
        puerta = creator.fabricarPuerta(hab1, hab2)

        hab1.ponerElementoEnOrientacion(puerta, Norte())
        hab2.ponerElementoEnOrientacion(puerta, Sur())

        pared1 = creator.fabricarPared()
        bomba1 = creator.fabricarBomba(pared1)
        hab1.ponerElementoEnOrientacion(bomba1, Este())

        pared2 = creator.fabricarPared()
        bomba2 = creator.fabricarBomba(pared2)
        hab2.ponerElementoEnOrientacion(bomba2, Oeste())


        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

    def crearLaberinto4H4BFM(self, unFM):
        laberinto = unFM.fabricarLaberinto()

        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        hab3 = unFM.fabricarHabitacion(3)
        hab4 = unFM.fabricarHabitacion(4)

        puerta12 = unFM.fabricarPuerta(hab1, hab2)
        puerta13 = unFM.fabricarPuerta(hab1, hab3)
        puerta24 = unFM.fabricarPuerta(hab2, hab4)
        puerta34 = unFM.fabricarPuerta(hab3, hab4)

        hab1.ponerElementoEnOrientacion(puerta12, Sur())
        hab1.ponerElementoEnOrientacion(puerta13, Este())
        hab2.ponerElementoEnOrientacion(puerta12, Norte())
        hab2.ponerElementoEnOrientacion(puerta24, Este())
        hab3.ponerElementoEnOrientacion(puerta13, Oeste())
        hab3.ponerElementoEnOrientacion(puerta34, Sur())
        hab4.ponerElementoEnOrientacion(puerta24, Oeste())
        hab4.ponerElementoEnOrientacion(puerta34, Norte())

        bicho1 = unFM.fabricarBicho(5,10,hab1,unFM.fabricarAgresivo())
        self.agregar_bicho(bicho1)
        bicho3 = unFM.fabricarBicho(5,10,hab3,unFM.fabricarAgresivo())
        self.agregar_bicho(bicho3)
        bicho2 = unFM.fabricarBicho(5,1,hab2,unFM.fabricarPerezoso())
        self.agregar_bicho(bicho2)
        bicho4 = unFM.fabricarBicho(5,1,hab4,unFM.fabricarPerezoso())
        self.agregar_bicho(bicho4)

        hab1.bicho=bicho1
        hab2.bicho=bicho2
        hab3.bicho=bicho3
        hab4.bicho=bicho4

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)

        return laberinto
    
    def obtenerHabitacion(self, num):
        return self.laberinto.obtener_habitacion(num)
    
    """def crearLaberinto1H1BB(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        bichoBoss = creator.fabricarBoss()
        self.laberinto.agregar_habitacion(hab1)
        self.agregar_bicho(bichoBoss)
        bichoBoss.posicion = hab1
        return self.laberinto"""