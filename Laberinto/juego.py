class ElementoMapa:
    def __init__(self,padre):
        self.padre = padre
        pass
    
    def entrar(self):
        pass

    def entrar(self,alguien):
        pass

class Orientacion:
    def __init__(self):
        pass

    def ponerElemento(self, em, unContenedor):
        pass

class Norte(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.norte = em

    def obtenerElementoOR(self, unContenedor):
        return unContenedor.norte

class Sur(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.sur = em

    def obtenerElementoOR(self, unContenedor):
        return unContenedor.sur

class Este(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.este = em

    def obtenerElementoOR(self, unContenedor):
        return unContenedor.este

class Oeste(Orientacion):
    def ponerElemento(self, em, unContenedor):
        unContenedor.oeste = em

    def obtenerElementoOR(self, unContenedor):
        return unContenedor.oeste
    
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()

class Decorator(Hoja):
    def __init__(self,em):
        super().__init__()
        self.em = em
        pass

class Bomba(Decorator):
    def __init__(self,em):
        super().__init__(em)
        self.activa = False
    
    def entrar(self):
        if self.activa:
            print("¡Te has chocado con una bomba!")
        else:
            self.em.entrar()

class Bicho:
    def __init__(self, vidas, poder, modo, posicion):
        self.vidas = vidas
        self.poder = poder
        self.modo = modo
        self.posicion = posicion

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

    def iniBoss(self):
        self.modo = Boss()
        self.poder = 20
        self.vidas = 10

class Modo:
    def __init__(self):
        pass

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

class Boss(Modo):
    def __init__(self):
        super().__init__()

class Contenedor(ElementoMapa):
    def __init__(self, hijos, orientaciones):
        super().__init__()
        self.hijos = hijos
        self.orientaciones = orientaciones

    def agregarHijo(self, em):
        self.hijos.append(em)

    def eliminarHijo(self, em):
        self.hijos.remove(em)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
        
    def obtenerElementoOR(self, orientacion):
        return self.obtenerElementoOR(orientacion)

    def ponerEnOr(self, em, orientacion):
        self.ponerElemento(em, orientacion)
class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("¡Te has chocado con una pared")

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

class Habitación(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num
        
    def entrar(self):
        print(f"Estás en una habitación{self.num}")

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        self.hijos = []

    def agregar_habitacion(self, hijo):
        self.hijos.append(hijo)

    def eliminar_habitacion(self, hijo):
        self.hijos.remove(hijo)

    def obtener_habitacion(self, num):
        for hijo in self.hijos:
            if hijo.num == num:
                return hijo

        return None

    def entrar(self):
        print("Estás en un laberinto")
    

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho) 

    def iniciar_juego(self):
        print("¡Bienvenido al juego del laberinto!")
        # Aquí puedes agregar la lógica para iniciar el juego

    def crearLaberinto2Habitaciones(self):
        laberinto = Laberinto()
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

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto

    def crearLaberinto2HabitacionesFM(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)
        puerta = creator.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto
    
    def crearLaberinto2HabitacionesFMD(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)

        pared1 = creator.fabricarPared()
        bomba1 = creator.fabricarBomba(pared1)
        hab1.este = bomba1

        pared2 = creator.fabricarPared()
        bomba2 = creator.fabricarBomba(pared2)
        hab2.oeste = bomba2

        puerta = creator.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto
    
    def crearLaberinto4H4BFMD(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        hab2 = creator.fabricarHabitacion(2)
        hab3 = creator.fabricarHabitacion(3)
        hab4 = creator.fabricarHabitacion(4)

        puerta1 = creator.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta1
        hab2.norte = puerta1

        puerta2 = creator.fabricarPuerta(hab1, hab3)
        hab1.este = puerta2
        hab3.oeste = puerta2

        puerta3 = creator.fabricarPuerta(hab2, hab4)
        hab2.este = puerta3
        hab4.oeste = puerta3

        puerta4 = creator.fabricarPuerta(hab3, hab4)
        hab3.sur = puerta4
        hab4.norte = puerta4

        bicho1 = creator.fabricarBichoAgresivo()
        bicho2 = creator.fabricarBichoAgresivo()
        bicho3 = creator.fabricarBichoPerezoso()
        bicho4 = creator.fabricarBichoPerezoso()

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)
        self.agregar_bicho(bicho1)
        self.agregar_bicho(bicho2)
        self.agregar_bicho(bicho3)
        self.agregar_bicho(bicho4)

        bicho1.posicion = hab1
        bicho2.posicion = hab3
        bicho3.posicion = hab2
        bicho4.posicion = hab4
        return laberinto
    
    def obtenerHabitacion(self, num):
        return self.laberinto.obtener_habitacion(num)
    
    def crearLaberinto1H1BB(self, creator):
        laberinto = creator.fabricarLaberinto()
        hab1 = creator.fabricarHabitacion(1)
        bichoBoss = creator.fabricarBoss()
        laberinto.agregar_habitacion(hab1)
        self.agregar_bicho(bichoBoss)
        bichoBoss.posicion = hab1
        return laberinto
       
