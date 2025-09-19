class Bus:
    lista_asientos = []
    def __init__(self,n_asientos):
        self.__asientos = n_asientos
        self.__asientos_vendidos = 0
        self.__asientos_max = n_asientos
        self.__vender = True
        
    def venta_ticket(self, pticket):
        if self.__asientos_vendidos < self.__asientos_max:
            self.lista_asientos.append(pticket)
            self.__asientos_vendidos += 1
            print(f"venta realizada ID_Ticket: BUS {pticket.get_ticket_id()}")
            return True
        else:
            return False
    
    def devolucion_ticket(self, ticket_id):
            
        if self.__asientos_vendidos > 0:
            for i in self.lista_asientos:
                if i.get_ticket_id() == ticket_id:
                    self.lista_asientos.remove(i)
                    break
            self.__asientos_vendidos -= 1
            print(f"devolución realizada ID_Ticket: {ticket_id}")
            return True
        else:
            return False
    
    def __str__(self):
        
        return f"Total: {self.__asientos_max}\nlibre:{self.__asientos_max - self.__asientos_vendidos}\nvendidos: {self.__asientos_vendidos}"
    
    def get_asientos_vendidos(self):
        for i in self.lista_asientos:
            print(i)
    
    def asientos_vendidos(self):
        return self.__asientos_vendidos
#end class Bus