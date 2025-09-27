class Bus:
    lista_asientos = []
    def __init__(self,n_asientos, l_bus = ""):
        self.__asientos_vendidos = 0
        self.__asientos_max = n_asientos
        self.__linea_bus = l_bus
        
    def venta_ticket(self, pticket):
        if self.__asientos_vendidos < self.__asientos_max:
            self.lista_asientos.append(pticket)
            self.__asientos_vendidos += 1
            return f"venta realizada BUS: {self.__linea_bus} ID Ticket:{pticket.get_ticket_id()}"
        else:
            return "No hay asientos disponibles"
    def ticket_list(self):
        for i in self.lista_asientos:
            print(i)
        return
    def devolucion_ticket(self, ticket_id):
        if self.__asientos_vendidos > 0:
            for i in self.lista_asientos:
#debug para ver cual es la compracion de el id que se busca con el id que se esta asignando para poder realizar la eliminacion de usuario 
                print(f"id del ticket {i.get_ticket_id()} vs id a devolver {ticket_id}")
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
