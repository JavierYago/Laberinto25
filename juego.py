class ElementoMapa:
    def __init__(self):
        pass

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

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

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()

    def iniciar_juego(self):
        print("¡Bienvenido al juego del laberinto!")
        # Aquí puedes agregar la lógica para iniciar el juego

# Ejemplo de uso
if __name__ == "__main__":
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
    print(f"Puerta 2 abierta: {puerta2.abierta}")
