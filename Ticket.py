from Person import Persona

class Ticket:
    __ticket_id = -1
    def __init__(self,  passenger):
        self.set_passenger(passenger)
        self.__ticket_id +=1 

    def set_passenger(self, passenger):
        self.__passenger = passenger
    
   ###
   #def devolucion_ticket(self, passenger, id_ticket):
    #    self.set_passenger(passenger)
    #    self.__ticket_id = id_ticket
    ###

    
    def get_ticker_id(self):
        return self.__ticket_id
    
    def __str__(self):
        return f"Ticket ID: {self.__ticket_id}, Passenger name: {self.__passenger.get_name()}, Passenger surname: {self.__passenger.get_surname()}"
