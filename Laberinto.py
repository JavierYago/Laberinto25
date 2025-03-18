from Contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()

    def agregar_habitacion(self, unaHabitacion):
        self.hijos.append(unaHabitacion)

    def eliminar_habitacion(self, unaHabitacion):
        self.hijos.remove(unaHabitacion)

    def obtener_habitacion(self, num):
        for habitacion in self.hijos:
            if habitacion.num == num:
                return habitacion
        return None

    def entrar(self,alguien):
        print("Estás en un laberinto")
        hab1=self.obtenerHabitacion(1)
        hab1.entrar(alguien)

    def __str__(self):
        return "Soy un laberinto"