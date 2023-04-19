'''2. Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa debe incorporar funciones para: 1. crear el archivo si este no existe, 2. para consultar el teléfono de un cliente, 3. 
añadir el teléfono de un nuevo cliente y 4. eliminar el teléfono de un cliente. El listado debe estar guardado
en el archivo de texto Directorio.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''
import io
import os
opc = ""
def menu():
    print("1.Consultar directorio\n2.Añadir el telefono\n3.Eliminar el telefono")
def act():
    try:
        archivo = open("directorio", "r")
        lista = archivo.readlines()
        list = [str(x)+ ". " + lista[x] + "\n" for x in range( len( lista) ) ]
        archivo.close()
    except FileNotFoundError:
        print("error")
    return list
act()
while opc.upper() != "S":
    os.system("clear")
    menu()
    opc1 = input()
    if opc1 == "1":
        act()
        print("".join(act()) )
    elif opc1 == "2":
        try:
            archivo = open("directorio", "a")
            nombre = input("ingrese el nombre")
            numero = input("ingrese el numero")
            archivo.write("\n"+ nombre + ", " + numero )
            archivo.close()
        except :
            print("error")
    elif opc1 == "3":
        try:
            print("".join(act()))
            x = act()
            archivo = open("directorio", "w")
            numero = int(input("elige un elemento"))
            x.pop(numero)
            archivo.write("".join(x))
            archivo.close()
        except:
            print("error")
    opc = input("desea salir? ")
    