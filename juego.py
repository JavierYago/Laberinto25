class ElementoMapa:
    def __init__(self):
        pass
    
    def entrar(self):
        pass
class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()
        pass
    def entrar(self):
        print("¡Te has chocado con una pared")
        pass

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False
        def entrar(self):
            print("Te has chocado con una Pared Bomba")
        
class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2
        def entrar(self):
            if self.abierta:
                print("La puerta está abierta")
            else:
                print("La puerta está cerrada")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

class Habitación(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        def entrar(self):
            print("Estás en una habitación")

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def eliminar_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)

    def obtener_habitacion(self, num):
        for habitacion in self.habitaciones:
            if habitacion.num == num:
                return habitacion

        return None

    def entrar(self):
        print("Estás en un laberinto")

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

    def fabricarJuego(self):
        return Juego()


class CreatorB(Creator):
    def __init__(self):
        super().__init__()

    def fabricarPared(self):
        return ParedBomba()


    

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()

    def iniciar_juego(self):
        print("¡Bienvenido al juego del laberinto!")
        # Aquí puedes agregar la lógica para iniciar el juego

    def crearLaberinto2Habitaciones(self):
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

        laberinto = Laberinto()
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

    def crearLaberinto2HabitacionesFM(self):
        unFM = Creator()
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        puerta = unFM.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto = unFM.fabricarLaberinto()
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

    def crearLaberinto2HabitacionesFM(self, unFM):
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        puerta = unFM.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto = unFM.fabricarLaberinto()
        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

# Ejemplo de uso
"""if __name__ == "__main__":
    juego = Juego()

    # Crear habitaciones
    habitacion1 = Habitación(1)
    habitacion2 = Habitación(2)
    habitacion3 = Habitación(3)

    # Conectar habitaciones
    puerta1 = Puerta(habitacion1, habitacion2)
    puerta2 = Puerta(habitacion2, habitacion3)

    habitacion1.este = puerta1
    habitacion2.oeste = puerta1
    habitacion2.este = puerta2
    habitacion3.oeste = puerta2

    # Agregar habitaciones al laberinto
    juego.laberinto.agregar_habitacion(habitacion1)
    juego.laberinto.agregar_habitacion(habitacion2)
    juego.laberinto.agregar_habitacion(habitacion3)

    # Iniciar el juego
    juego.iniciar_juego()

    # Abrir puertas
    puerta1.abrir()
    puerta2.abrir()

    # Mostrar estado de las puertas
    print(f"Puerta 1 abierta: {puerta1.abierta}")
    print(f"Puerta 2 abierta: {puerta2.abierta}") """


#prueba del laberinto usando al metodo crearLaberinto2Habitaciones
if __name__ == "__main__":
    juego = Juego()
    laberinto = juego.crearLaberinto2Habitaciones()
    print(laberinto.habitaciones[0].norte)
    print(laberinto.habitaciones[0].sur)
    print(laberinto.habitaciones[0].este)
    print(laberinto.habitaciones[0].oeste)
    print(laberinto.habitaciones[1].norte)
    print(laberinto.habitaciones[1].sur)
    print(laberinto.habitaciones[1].este)
    print(laberinto.habitaciones[1].oeste)
    print(laberinto.habitaciones[0].sur.lado1)
    print(laberinto.habitaciones[0].sur.lado2)
    print(laberinto.habitaciones[1].norte.lado1)
    print(laberinto.habitaciones[1].norte.lado2)
