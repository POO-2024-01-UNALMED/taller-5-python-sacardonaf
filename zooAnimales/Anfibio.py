from zooAnimales import Animal
class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    def cantidadAnfibios(cls):
        return len(cls._listado)
    def movimiento():
        return "saltar"
    def crearRana(self,nombre,edad,genero):
        rana=Anfibio(nombre,edad,"selva",genero,"rojo",True)
        Anfibio.ranas+=1
        return rana
    def crearSalamandra(self,nombre,edad,genero):
        salamandra=Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        Anfibio.salamandras+=1
        return salamandra
    def getListado(cls):
        return cls._listado
    def setListado(cls,listado):
        cls._listado=listado
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso
