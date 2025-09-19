class Persona:
    def __init__(self, pnombre, papellido):
        self.__nombre = pnombre
        self.__apellido = papellido
    
    def get_name(self):
        return f"Nombre: {self.__nombre}"
    
    def get_surname(self):
        return f"Nombre: {self.__apellido}"
    
    def setting(self, pnombre, papellido):
        self.__nombre = pnombre
        self.__apellido = papellido
#end class Persona
