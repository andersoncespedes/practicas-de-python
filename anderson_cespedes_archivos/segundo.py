'''2. Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa debe incorporar funciones para: 1. crear el archivo si este no existe, 2. para consultar el teléfono de un cliente, 3. 
añadir el teléfono de un nuevo cliente y 4. eliminar el teléfono de un cliente. El listado debe estar guardado
en el archivo de texto Directorio.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''
import io
import os
import time
opc1 = ""
def menu():
    print("1.Consultar directorio\n2.Añadir el telefono\n3.Eliminar el telefono\n0.Salir")
def act():
    try:
        archivo = open("directorio.txt", "r")
        lista = archivo.readlines()
        list = [lista[x] for x in range( len( lista) ) ]
        archivo.close()
    except FileNotFoundError:
        archivo = open("directorio.txt", "w")
        archivo.close()
        return
    return list
act()
while opc1.upper() != "0":
    os.system("clear")
    menu()
    opc1 = input()
    if opc1 == "1":
        act()
        print("".join(act()) )
        time.sleep(3)
    elif opc1 == "2":
        try:
            archivo = open("directorio.txt", "a")
            nombre = input("ingrese el nombre: ")
            numero = input("ingrese el numero: ")
            archivo.write(nombre + ", " + numero+ "\n")
            archivo.close()
        except :
            print("error")
    elif opc1 == "3":
        try:
            x = act()
            archivo = open("directorio.txt", "w")
            for i in range(0, len(x)):
                print(str(i) + " "+ x[i])
            numero = int(input("elige un elemento: "))
            x.remove(x[numero])
            archivo.write("".join(x))
            archivo.close()
        except:
            print("error")
    