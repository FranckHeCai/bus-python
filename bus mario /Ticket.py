from Person import Persona

class Ticket:
    __ticket_id = -1
    def __init__(self,  passenger):
        self.set_passenger(passenger)
        self.set_ticket_id() 


    def set_passenger(self, passenger):
        self.__passenger = passenger
    
    def set_ticket_id(self):
        Ticket.__ticket_id += 1
        self.__ticket_id = Ticket.__ticket_id

    def get_ticket_id(self):
        return self.__ticket_id
    
    def __str__(self):
        return f"Ticket ID: {self.__ticket_id}, name: {self.__passenger.get_name()},  surname: {self.__passenger.get_surname()}"
