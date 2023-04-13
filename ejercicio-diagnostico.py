import os
import time
campers = {
    "basico": {
        "trainers":{
            0:{
                "nombre":"duvall"
            }
        },
        0:{
            "nombre":"anderson",
            "mes":"abril",
            "grupo": "e4",
            "edad":19
        }
    },
    "intermedio":{
        "trainers":{
                0:{
                    "nombre":"duvall"
                }
            },
        0:{
            "nombre":"christian",
            "mes":"mayo",
            "grupo": "e12",
            "edad":31
        }
    },
    "avanzado":{
        "trainers":{
                0:{
                    "nombre":"duvall"
                }
            },
         0:{
            "nombre":"jhoan",
            "mes":"marxo",
            "grupo": "e20",
            "edad":30
        }
    }
}

#MENU DE ESTUDIANTES


def menu(param, num):
    os.system('clear')
    arr = [" CREAR GRUPO "+param +" CON CAMPERS Y SUS DATOS PERSONALES", 
           " Registrar Expert Trainer Del grupo "+param, 
           " Buscar Campers duplicados en 2 grupos", 
           " Eliminar campers por inasistencia",
           " LISTAR CAMPERS",
           " Traslado del camper de grupo",
           " Agregar Campers AL GRUPO",
           " Reportar los campers de mayor y menor edad"]
    print(f'''------MANTENIMIENTO Y PREMIOS CAMPERS CAMPUS---------
    0. TERMINAR PROCESO
    ---------------------------------------------------------------
    ''')
    count = 0
    for x in arr:
        print(str(num) + "." + str("" if count == 0 else count) + x.upper())
        count+=1
#MENU PRINCIPAL
def mainMenu():
    os.system('clear')
    print('''----------------MENU--------------------
    0. TERMINAR PROCESO
    -------------------------------------------------
    1. BASICO
    2. INTERMEDIO
    3. AVANZADO''')
opc = ""
#LISTAS DE ESTUDIANTES
def listaEst(cat):
    print('''NOMBRE | MES | GRUPO | EDAD''')
    for x in campers[cat]:
        if type(x) is int:
            print(campers[cat][x]["nombre"], " | " , campers[cat][x]["mes"], " | "  ,campers[cat][x]["grupo"], " | " ,str(campers[cat][x]["edad"]) )
    time.sleep(3)
#FUNCION DE GUARDADO DE ESTUDIANTES
def guardado(param):
    print("INGRESE EL NOMBRE DEL ESTUDIANTE")
    nombre = input()
    print("INGRESE EL MES DE INGRESO DEL ESTUDIANTE")
    mes = input()
    print("INGRESE GRUPO DEL ESTUDIANTE")
    grupo = input()
    print("INGRESE EDAD DEL ESTUDIANTE")
    edad= int(input())
    guardar([nombre, mes, grupo, edad], param)
#FUNCION DE GUARDADO DE TRAINERS
def guardTrain(param):
    id = generarId("basico", "trainer")
    print("INGRESE EL NOMBRE DEL TRAINER")
    nom = input()
    campers[param]["trainers"][id] = {
        "nombre":nom
    }
#GENERADOR DE ID
def generarId(cat, pas):
    if pas == "trainers":
        return (len(campers[cat][pas].keys()) - 1) + 1
    nuevaId = ((len(campers[cat].keys()) - 1) + 1) - 1
    return nuevaId
#ACTUALIZACION DE ESTUDIANTES
def guardar(camper, cat):
    id = generarId(cat, "")
    campers[cat][id] = {
        "nombre":camper[0],
        "mes":camper[1],
        "grupo": camper[2],
        "edad":camper[3]
    } 
#EJECUTADOR DEL PROGRAMA
while opc != "0":
    mainMenu()
    opc = input()
    if opc == "1":
        opcB = ""
        while opcB != "0":
            menu("BASICO", 1)
            opcB = input()
            if opcB== "1":
                guardado("basico")
            elif opcB == "2":
                guardTrain("basico")
            elif opcB == "4":
                listaEst("basico")
    if opc == "2":
        opcB = ""
        while opcB != "0":
            menu("INTERMEDIO", 2)
            opcB = input()
            if opcB== "1":
                guardado("intermedio")

            elif opcB == "4":
                listaEst("intermedio")
    if opc == "3":
        opcB = ""
        while opcB != "0":
            menu("AVANZADO", 3)
            opcB = input()
            if opcB== "1":
                guardado("avanzado")
            elif opcB == "4":
                listaEst("avanzado")