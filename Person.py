
class Persona:
    def __init__(self, pnombre, pedad):
        self.__nombre = pnombre
        self.__edad = pedad
    
    def gettting(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    def setting(self, pnombre, pedad):
        self.__nombre = pnombre
        self.__edad = pedad
#end class Persona
