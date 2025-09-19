class bus:
    def __init__(self,n_asientos):
        self.__asientos = n_asientos
        self.__asientos_vendidos = 0
        self.__asientos_max = n_asientos
        self.__vender = True
    def asientos_vendidos(self):
        return self.__asientos_vendidos
