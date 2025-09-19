from Person import Persona
from Ticket import Ticket  
from bus import Bus


plazas = int(input("Ingrese el número de asientos\n"))
plazas_vendidas = 0
plazas_max = int(plazas)
#texto_saliente = str()
valor_texto = 0
vender = True


def devolucion(plazas, plazas_vendidas):
    tickets = int(input())
    if tickets <= plazas_vendidas:
#        print(f"Se devolvieron {tickets} billetes")
        plazas_vendidas -= tickets
        plazas += tickets
    else:
       plazas=plazas 
    return plazas, plazas_vendidas

def estado(plazas_max ,plazas, plazas_vendidas):
   print(f"Total: {plazas_max}")
   print(f"Libre: {plazas}")
   print(f"Vendido: {plazas_vendidas}")
   return

print("1.- Venta de billetes.")
print("2.- Devolución de billetes.")
print("3.- Estado de la venta.")
print("0.- Salir.")
bus_barcelona = Bus(plazas)   

while vender:
    opcion = input()
    if opcion == "1":
        cliente = Persona(input("Ingrese su nombre\n"), input("Ingrese su apellido\n"))
        venta =  Ticket(cliente)
        if venta is None:
            print("No se pudo realizar la venta")
        else:
            bus_barcelona.venta_ticket(venta)
        
    elif opcion == "2":
        id_ticket=int(input("ingrese id ticket a devolver\n"))
        #devolucion = Ticket.devolucion_ticket(cliente, id_ticket)
        bus_barcelona.devolucion_ticket(id_ticket)
    elif opcion == "3":
        print(bus_barcelona)

        
    elif opcion == "0":
        vender = False