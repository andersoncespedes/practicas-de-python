import os
import time
paciente = {

}
def generarId():
    nuevaId = ((len(paciente.keys()) - 1) + 1) - 1 if len(paciente.keys()) > 0 else 0
    return nuevaId
def guardar(param, id = None):
    if(id == None):
        idR = generarId()
    else:
        idR = id
    paciente[idR] = {
        "nombre":param['nombre'],
        "edad":param['edad'],
        "peso":param['peso'],
        "sexo":param['sexo']
    }
def mostrar():
    os.system("clear")
    print("Nombre | Edad | peso | Sexo")
    print("\n".join([str(x) +" " + paciente[x]["nombre"] + " " +str(paciente[x]["edad"]) + " " + str(paciente[x]["peso"])+ " " +paciente[x]["sexo"] for x in paciente]) )
    time.sleep(3)
def menu():
    os.system("clear")
    print("1.Nuevo Paciente\n2.Editar datos de un paciente\n3.Borrar datos de un paciente\n4Listar todos los pacientes")
    time.sleep(3)
opc = ""
while opc.upper() != "S":
    menu()
    opc1 = input()
    if opc1 == "1":
        print('ingrese su nombre')
        nombre = input()
        print('ingrese su edad')
        edad = int(input())
        print('ingrese su peso')
        peso = float(input())
        print("Cual es su sexo F/M?")
        sexo = input()
        if sexo == "M" or sexo == "F":
            guardar({
                "nombre":nombre,
                "edad":edad,
                "peso":peso,
                "sexo":sexo
                })
            continue
        else:
            print("error")
    elif opc1 == "2":
        mostrar()
        print("escoja un paciente")
        opcP = int(input())
        print('ingrese su nombre')
        nombre = input()
        print('ingrese su edad')
        edad = int(input())
        print('ingrese su peso')
        peso = float(input())
        print("Cual es su sexo F/M?")
        sexo = input()
        try:
            guardar({
                "nombre":nombre,
                "edad":edad,
                "peso":peso,
                "sexo":sexo
                },opcP)
        except:
            print("error no se pudo guardar")
    elif opc1 == "3":
        mostrar()
        print("Elige el codigo del paciente")
        cod = int(input())
        try:
            del paciente[cod]
        except:
            print("error, no se pudo eliminar")
    elif opc1 == "4":
        mostrar()
    print("Desea Salir? S/N")
    opc = input()
        
