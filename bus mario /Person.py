class Persona:
    def __init__(self, pnombre, papellido):
        self.set_name(pnombre)
        self.set_surname(papellido)
    
    def set_name(self, pnombre):
        self.__nombre = pnombre 
    def set_surname(self, papellido):
        self.__apellido = papellido
    
    def get_name(self):
        return self.__nombre
    
    def get_surname(self):
        return self.__apellido
    
    def setting(self, pnombre, papellido):
        self.__nombre = pnombre
        self.__apellido = papellido
#end class Persona

