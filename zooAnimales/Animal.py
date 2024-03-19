

class Animal:
    _totalAnimales=0
    ave=[]
    mamifero=[]
    pez=[]
    reptil=[]
    anfibio=[]
    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal._totalAnimales+=1
    def movimiento():
        return "desplazarse"
    def totalPorTipo(self):
        return (f"Mamiferos:{len(self.mamifero)}\nAves:{len(self.ave)}\nReptiles:{len(self.reptil)}\nPeces:{len(self.pez)}\nAnfibios:{len(self.anfibio)}")
    def __str__(self):
        if self._zona==None:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}")
        else:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.self._zoo}")
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre    
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad=edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self,habitat):
        self._habitat=habitat
    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero=genero
    def getZona(self):
        return self._zona
    def setZona(self,zona):
        if(self._zona==None):
            self._zona=[zona]
        else:
            self._zona.append(zona)