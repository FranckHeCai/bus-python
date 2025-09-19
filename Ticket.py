from Person import Persona

class Ticket:
    def __init__(self, ticket_id, passenger):
        self.set_passenger(passenger)
        self.set_ticket_id(ticket_id)

    def set_passenger(self, passenger):
        self.__passenger = passenger
    
    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id
    
    def __str__(self):
        return f"Ticket ID: {self.__ticket_id}, Passenger name: {self.__passenger.get_name()}, Passenger surname: {self.__passenger.get_surname()}"
