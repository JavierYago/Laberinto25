from creator import Creator, CreatorB
from juego import Juego

# Código de prueba
#Laberinto con 2 habitaciones
juego = Juego()
creator = Creator()
juego.laberinto = juego.crearLaberinto2HabitacionesFM(creator)
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)
print(hab1)
print(hab2)

#Laberinto con 2 habitaciones con paredes bomba
juego = Juego()
creator = CreatorB()
juego.laberinto = juego.crearLaberinto2HabitacionesFM(creator)
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)
print(hab1.norte.activa)
print(hab2)

#Laberinto con 2 habitaciones con bombas
juego = Juego()
creator = Creator()
juego.laberinto = juego.crearLaberinto2HabitacionesFMD(creator)
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)
print(hab1)
print(hab2)

#Laberinto con 4 habitaciones y 4 bichos
juego = Juego()
creator = Creator()
juego.laberinto = juego.crearLaberinto4H4BFMD(creator)
hab1 = juego.obtenerHabitacion(1)
hab2 = juego.obtenerHabitacion(2)
hab3 = juego.obtenerHabitacion(3)
hab4 = juego.obtenerHabitacion(4)
print(hab1)
print(hab2)
print(hab3)
print(hab4)

