from zooAnimales.animal import Animal
class Ave(Animal):
    _listado=[]
    halcones=0
    aguilas=0
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    def cantidadAves(cls):
        return len(cls._listado)
    def movimiento():
        return "volar"
    def crearHalcon(self,nombre,edad,genero):
        halcon=Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        Ave.halcones+=1
        return halcon
    def crearAguila(self,nombre,edad,genero):
        aguila=Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        Ave.aguilas+=1
        return aguila
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,colorPlumas):
        self._colorPlumas=colorPlumas
    def getListado(cls):
        return cls._listado
    def setListado(cls,listado):
        cls._listado=listado
