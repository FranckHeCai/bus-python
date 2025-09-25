from Person import Persona
from Ticket import Ticket  
from bus import Bus

plazas = int(input("Ingrese el número de asientos\n"))
plazas_vendidas = 0
plazas_max = int(plazas)
valor_texto = 0
vender = True

def devolucion(plazas, plazas_vendidas):
    tickets = int(input())
    if tickets <= plazas_vendidas:
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

def mostrar_menu():
    print("1.- Venta de billetes.")
    print("2.- Devolución de billetes.")
    print("3.- Estado de la venta.")
    print("0.- Salir.")
    return

bus_barcelona = Bus(plazas)   
mostrar_menu()

while vender:
    opcion = input()
    if opcion == "1":
        cliente = Persona(input("Ingrese su nombre\n"), input("Ingrese su apellido\n"))
        venta =  Ticket(cliente)
        print(bus_barcelona.venta_ticket(venta))
    elif opcion == "2":
        if bus_barcelona.get_asientos_vendidos() == 0:
            print("No hay tickets vendidos")
        else:
            id_ticket=int(input("ingrese id ticket a devolver\n"))
            print(bus_barcelona.devolucion_ticket(id_ticket))
    elif opcion == "3":
        print(bus_barcelona)
    elif opcion == "0":
        vender = False
