from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
        
    """def obtenerElementoOR(self, orientacion):
        return orientacion.obtenerElementoOR(self)"""

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.ponerElemento(elemento, self)

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)