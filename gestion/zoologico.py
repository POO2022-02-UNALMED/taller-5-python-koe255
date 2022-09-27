class Zoologico:
    _zonas = []

    def __init__(self, nombre=None, ubicacion=None):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    @classmethod
    def getZona(self):
        return self._zonas

    @classmethod
    def setZona(self, zonas):
        self._zonas = zonas

    @classmethod
    def agregarZonas(cls, zona):
        cls._zonas.append(zona)

    def cantidadTotalAnimales(self):
        i = 0
        for zona in self._zonas:
            i += zona.cantidadAnimales()
        return i
