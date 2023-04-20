empresas = {"Personas":[]}
import time
import os
def menu():
    os.system("clear")
    print("******************MENU******************")
    print('''1.AGREGAR  2.EDITAR
3.ELIMINAR 4.VISUALIZAR
0.SALIR''')
    time.sleep(3)
def generarId(param):
    id = param[len(param) - 1]["id"] + 1 if len(param) > 0 else 1
    return id
def create(param):
    empresas["Personas"].append({
    "id":generarId(empresas["Personas"]), 
    "nombre": param["nombre"], 
    "edad":param["edad"],
    "numDoc":param["numDoc"]})
def edit(param, id):
    empresas["Personas"][id - 1] = {
        "id":empresas["Personas"][id - 1]["id"], 
        "nombre": param["nombre"], 
        "edad":param["edad"],
        "numDoc":param["numDoc"]
    }
def show(param):
    x = 0
    print("NOMBRE | EDAD | DOCUMENTO")
    for i in empresas[param]:
        x+=1
        print(str(i["id"]) + " "  + i["nombre"] + " " + i["edad"] + "  " + i["numDoc"])
 
def form(cat,id=None):
    print("Nombre")
    nombre = input()
    print("Edad")
    edad = input()
    print("numero de documento")
    numdoc = input()
    if cat == "crear":
        try:
            create({"nombre":nombre, "edad":edad, "numDoc":numdoc})
            print("***CREACION EXITOSA***")
        except:
            print("error")
    elif cat == "editar":
        try:
            edit({"nombre":nombre, "edad":edad, "numDoc":numdoc}, id)
            print("***EDICION EXITOSA***")
        except:
            print("error")

opc = ""
while opc != "0":
    menu()
    opc = input()
    if opc == "1":
        form("crear")
    elif opc == "2":
        show("Personas")
        print("elige una id")
        id = int(input())
        form("editar",id)
    elif opc == "3":
        show("Personas")
        print("elige una id")
        id = int(input())
        try:
            empresas["Personas"].pop(id - 1)
            print("***ELIMINACION EXITOSA***")
            time.sleep(3)
        except:
            print("error no se pudo eliminar")
    elif opc == "4":
        show("Personas")
        time.sleep(3)