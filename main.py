from Creator import Creator
from CreatorB import CreatorB
from Juego import Juego
import time

# Código de prueba
#Laberinto con 2 habitaciones
creator = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto2HabitacionesFM(creator)
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)
print(hab1.num)
print(hab2.num)

#Laberinto con 2 habitaciones con paredes bomba
creatorb = CreatorB()
juego.laberinto = juego.crearLaberinto2HabitacionesFM(creatorb)
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)
print(hab1.este.activa)
print(hab2.oeste.activa)


#Laberinto con 4 habitaciones y 4 bichos
creator = Creator()
juego.laberinto = juego.crearLaberinto4H4BFM(creator)

#Mostrar el número de cada habitación
for habitacion in juego.laberinto.hijos:
    print(f"Habitación: {habitacion.num}")

#Mostrar los bichos del juego
for bicho in juego.bichos:
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Modo: {bicho.modo}")
    print(f"Posición: {bicho.posicion}")


#Ejemplo de uso de recorrer con print
print("\nRecorriendo el laberinto e imprimiendo:")
juego.laberinto.recorrer(print)

juego.abrir_puertas()

juego.cerrar_puertas()

bicho=juego.bichos[0]
juego.lanzarBicho(bicho)
time.sleep(3)
bicho.vidas=0




"""#Primera implementación en Python: Bicho Boss
juego = Juego()
creator = Creator()
juego.laberinto = juego.crearLaberinto1H1BB(creator)
hab1 = juego.obtenerHabitacion(1)
print(hab1)"""