from Person import Persona
from Ticket import Ticket  
from bus import Bus

plazas_vendidas = 0

valor_texto = 0

def login():
    while True:
        usuario = input("Ingresa aquí tu usuario: ")
        contra = input("Ingresa aquí tu contraseña: ")

        if usuario == contra:
            print("\nEl usuario no puede ser el mismo que la contraseña.\n")
        elif usuario == "usuario123" and contra == "mario":
            print("\nBienvenido\n")
            return True
        else:
            print("\nUsuario o contraseña incorrectos. Inténtalo de nuevo.\n")

def plazas_bus():
    plazas = 0
    plazas_invalidas = True
    while  plazas_invalidas :
        plazas = str(input("Ingrese el número de asientos\n"))
        if plazas.isdigit():
            plazas_invalidas = False
        else:
            print("\n*******se requiere un numero para poder asignar las plazas*******\n")            
    return plazas

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

vender = login()

if vender:
    plazas = plazas_bus()
    plazas_max = int(plazas)
    bus_barcelona = Bus(plazas_max)   

#mostrar_menu()
while vender:
    mostrar_menu()

    opcion = input()
    
    if opcion == "1":
        print("----Venta de billetes----")
        cliente = Persona(input("Ingrese su nombre\n"), input("Ingrese su apellido\n"))
        venta =  Ticket(cliente)
        print(bus_barcelona.venta_ticket(venta))
        
    elif opcion == "2":
        print("----Devolución de billetes----")
        if bus_barcelona.get_asientos_vendidos() == 0:
            print("No hay tickets vendidos")
        else:
            id_ticket=input("ingrese id ticket a devolver\n")
            if id_ticket.isdigit():
                print("====Se requiere un numero para el id del ticket====")
                print(bus_barcelona.devolucion_ticket(id_ticket))
            else:
                print("====El id del ticket debe ser un numero====")
    elif opcion == "3":
        #bus_barcelona.ticket_list() #ver tickets vendidos id ticket, nombre y apellido
        print("----Estado de la venta----")
        print(bus_barcelona)
    
    elif opcion == "0":
        print("----Saliendo del programa----")
        vender = False
    
    else:
        print("====Opción no válida====")