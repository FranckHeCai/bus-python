class Bus:
    lista_asientos = []
    def __init__(self,n_asientos):
        self.__asientos_vendidos = 0
        self.__asientos_max = n_asientos
        
    def venta_ticket(self, pticket):
        if self.__asientos_vendidos < self.__asientos_max:
            self.lista_asientos.append(pticket)
            self.__asientos_vendidos += 1
            return f"venta realizada ID_Ticket: BUS {pticket.get_ticket_id()}"
        else:
            return "No hay asientos disponibles"
    def ticket_list(self):
        for i in self.lista_asientos:
            print(i)
        return
    def devolucion_ticket(self, ticket_id):
        if self.__asientos_vendidos > 0:
            for i in self.lista_asientos:
                #print(f"id del ticket {i.get_ticket_id()} vs id a devolver {ticket_id}")
                if i.get_ticket_id() == ticket_id:
                    self.lista_asientos.remove(i)
                    self.__asientos_vendidos -= 1
                    return "----Devolución realizada----"
            else:
                return"----El ticket no existe----"
    def __str__(self):
        return f"Total: {self.__asientos_max}\nlibre:{self.__asientos_max - self.__asientos_vendidos}\nvendidos: {self.__asientos_vendidos}"
    
    def get_asientos_vendidos(self):
        return self.__asientos_vendidos
#end class Bus
