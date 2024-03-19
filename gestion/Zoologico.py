
class Zoologico:
    def __init__(self,nombre,ubicacion,zonas=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=zonas
    def agregarZonas(self,zona):
        if self._zonas==None:
            self._zonas=[zona]
        else:
            self._zonas.append(zona)
    def cantidadTotalAnimales(self):
        con=0
        for i in range(0,len(self._zonas)):
            con+=len(self._zonas[i]._animales)
        return con
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    def getZona(self):
        return self._zonas
    def setZona(self,zona):
        self._zonas=zona

