from os import system

correct_users={'jefe': '7777', 'buyer': '0000'}

produc_store= [
{'Tipo de Iphone': 'Iphone 11', 'IMEI': '1111', 'Precio': 2000000, 'Almacenamiento': '128gb'},
{'Tipo de Iphone': 'Iphone 12', 'IMEI': '2222', 'Precio': 2500000, 'Almacenamiento': '256gb'},
{'Tipo de Iphone': 'Iphone 13', 'IMEI': '3333', 'Precio': 3000000, 'Almacenamiento': '256gb'},
{'Tipo de Iphone': 'Iphone 14', 'IMEI': '4444', 'Precio': 4000000, 'Almacenamiento': '1T'}]


bills= [
{'Tipo de iphone': 'Iphone 12','IMEI': '2222', 'Precio': 2500000, 'Almacenamiento': '256gb', 'Estado': 'SOLD'},
{'Tipo de iphone': 'Iphone 11', 'IMEI': '1111', 'Precio': 2000000, 'Almacenamiento': '128gb', 'Estado': 'SOLD'},
]

customer_history= [
{'Nombre': 'Juan Paez','Tipo': 'Iphone 13', 'Precio': '3000000', 'Almacenamiento': '256'},
{'Nombre': 'Tony Herbert','Tipo': 'Iphone 14', 'Precio': '4000000', 'Almacenamiento': '1T'},
]
def look_inv(lista):
    for i in lista:
        for x,y in i.items():
            print(f">{x} {y}")
        print()
    
def delete_cell():
    for i in produc_store:
        if imei_iphone in i.values():
            produc_store.remove(i)  

def fact_ventas():
    for i in produc_store:
        if imei_iphone in i.values():
            print(f'''Nombre: {i['Nombre:']}''')

def look_c(cus):
    for i in cus:
        for x,y in i.items():
            print(f"{x} {y}")   
            print()      

while True:
    system("cls")
    user= input("Ingrese su usuario--->: ")
    password=(input("Ingrese su contraseña--->: "))
    if user in correct_users:
        if password==correct_users['jefe'] or password==correct_users['buyer']:
            break
    else:
        print("ERROR. POR FAVOR, INGRESE BIEN SUS DATOS")
    
if user== 'jefe'and password == '7777':
    while True:
        system('cls')
        print("""<<<<<<<<MENÚ DEL JEFE>>>>>>>>

Seleccione la acción a realizar:

1. Ver inventario de celulares.
2. Agregar celulares al inventario.
3. Eliminar celulares del inventario.
4. Facturas de venta.
5. Todos los clientes.
""")
        
        while True:
            print()
            opc=input("Ingrese la opción que desea realizar>>: ")
            if opc=="1":
                system('cls')
                print("<<<<INVETARIO STORE>>>>")
                look_inv(produc_store)
                input("Toca para volver al menú")
                break
            elif opc=='2':
                while True:
                    system('cls')
                    print("<<<<AGREGAR CELULARES AL INVENTARIO>>>>")
                    tipo=input("Ingrese el tipo de Iphone--->>: ")
                    almacen=input("Ingrese la cantidad de almacenamiento--->>: ")
                    while True:
                        try:
                            imei=int(input("Ingrese el IMEI del iphone--->>: "))
                            price=int(input("Ingrese el costo del Iphone--->: "))
                            break
                        except:
                            ValueError (print("ERROR. Solo se admiten valores númericos"))
                    if price<=0:
                        print("ERROR. El precio que ha indicado no es válido")
                        break
                    else:
                        cell={"Tipo:": tipo,"IMEI:" : imei,"Precio:" : price, "Almacenamiento:": almacen,}
                        produc_store.append(cell)
                        print("SE HA AÑADIDO CORRECTAMENTE EL NUEVO CELULAR")
                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                        print("""
1. Return to menu.
2. Add other cellphone.
""")
                        while True: 
                            print()
                            opci=input("¿Qué desea hacer>>: ")
                            if opci=="1":
                                break
                            if opci=="2":
                                break
                    if opci=="1":
                        break
            elif opc=="3":
                while True:
                    system("cls")
                    print("HA SELECCIONADO ELIMINAR CELULAR DEL INVENTARIO")
                    look_inv(produc_store)
                    imei_iphone=input("Ingrese el IMEI del Iphone que desea eliminar>>>: ")
                    delete_cell()
                    print("""
SE HA ELIMINADO CORRECTAMENTE DEL INVENTARIO

1.Return to menu.
2. Delete other cellphone.
""")
                    while True:
                        print()
                        opci=input(">>>>: ")
                        if opci=="1":
                            break
                        if opci=="2":
                            break
                        else:
                            print("ERROR. Opción no valida")
                        print()
                        if opci=="1":
                            break
                if opci=="1":
                    break

            elif opc=="4":
                system("cls")
                print("HA SELECCIONADO VER FACTURAS DE COMPRAS")
                print("<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")
                look_inv(bills)
                print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>")
                input("Push enter to back")
                break
            elif opc=="5":
                system("cls")
                print("HA INGRESADO A VER EL HISTORIAL DE CLIENTES")
                print("<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>><<>>>>>>>")
                look_c(customer_history)
            
            if opci=="1":
                break
if user=="buyer" and password=="0000":
    while True:
     system("cls")   
     print("""=======================<MENU DE CLIENTE>=======================

Seleccione la acción a realizar:

1. BUY CELLPHONE.
2. SEARCH CELLPHONE.
3. PAY FEE.
4. BACK TO MENU.
5. LEAVE PAGE.
""")        
    
     while True:
      opc=input("Elija>>: ")
      if opc=="1":
        while True: 
            print("<<<<<<ESTÁ A PUNTO DE COMPRAR UN SMARTHPHONE>>>>>>")
            look_inv(produc_store)
            imei_iphone=input("Ingrese el IMEI del Iphone>>: ")
            print(">>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

            for i in produc_store:
                for imei in i.values():
                    if imei_iphone==imei:
                        for x,y in i.items():
                            print(f"{x} {y}")
                        break
                else:
                    continue
                break
            else:    
                print("ERROR")  
                    
            input("ENTER para menu")
            break
        break
      