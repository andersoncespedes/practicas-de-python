import json
from time import sleep
from os import system
#MENU
def show():
    system("clear")
    print("----------------MENU----------------")
    print('''1.MOSTRAR                2.GUARDAR
3.MOSTRAR POR NOMBRE     4.EDITAR
5.ELIMINAR               0.SALIR ''')
#MODULO PARA MOSTRAR LOS DATOS DEL JSON
def jsonOpen():
    with open('Biblioteca.json', 'r') as f: data = json.load(f)
    x = data
    f.close()
    return x
#MODULO PARA MOSTRAR LOS DATOS DEL LIBRO
def showData():
    system("clear")
    biblio = jsonOpen()
    print("titulo\t\tAutor\t\tAño\t\tPrecio\t\tCategoria\n".ljust(15))
    for dato in biblio["bookstore"]["book"]:
        if type(dato["author"]) is not list:
            print(dato["title"]["__text"] + "\t\t" + dato["author"] + "\t" + dato["year"] + "\t\t" + dato["price"] + "\t\t" + dato["_category"].ljust(15), end="\n")
        elif(type(dato["author"]) is list):
            print(dato["title"]["__text"] + "\t\t" + ", ".join(dato["author"]) + "\t\t" + dato["year"] + "\t\t" + dato["price"] + "\t\t" + dato["_category"], end="\n")
    input("-- ingresa cualquier tecla para continuar... ")
#MODULO PARA ELIMINAR EL LIBRO SEGUN EL TITULO
def save(param):
    tabla = jsonOpen()
    tabla["bookstore"]["book"].append({"title":{
            "_lang":param["lan"],
            "__text":param["titulo"]
        },
        "author":param["author"] if len(param["author"])>1 else param["author"][0],
        "year":param["year"],
        "price":param["price"],
        "_category":param["category"]
        })
    with open("Biblioteca.json", "w") as archivo: json.dump(tabla, archivo)
    archivo.close()
#MODULO DE EDICION POR MEDIO DE NOMBRES
def edit(param, name):
    books = jsonOpen()
    try:
        #BUSQUEDA DE LOS ELEMENTOS POR NOMBRE
        search = [x for x in range(len(books["bookstore"]["book"])) if books["bookstore"]["book"][x]["title"]["__text"].lower() == name.lower()]
        books["bookstore"]["book"][search[0]] = {"title":{
            "_lang":param["lan"],
            "__text":param["titulo"]
        },
        "author":param["author"] if len(param["author"])>1 else param["author"][0],
        "year":param["year"],
        "price":param["price"],
        "_category":param["category"]
        }
        with open("Biblioteca.json", "w") as archivo: json.dump(books, archivo)
        print("BIBLIOTECA ACTUALIZADA CORRECTAMENTE")
        sleep(3)
    except:
        print("HUBO UN ERROR AL MOMENTO DE ACTUALIZAR")
        sleep(3)
#CONTENEDOR DE LOS FORMULARIOS DE REGISTRO
def formulario(param,name = None):
    try:
        print("-- INGRESE EL NOMBRE DEL LIBRO")
        title = input()
        print("-- INGRESE EL IDIOMA DEL LIBRO")
        idioma = input()
        opc2 = ""
        autores = []
        while opc2.lower() != "n":
            print("-- INGRESE EL AUTOR DEL LIBRO")
            autor = input()
            autores.append(autor)
            opc2 = input("desea continuar añadiendo autores? S/N")
        print("-- INGRESE EL AÑO DEL LIBRO")
        year = input()
        print("-- INGRESE EL PRECIO DEL LIBRO")
        price = input()
        print("-- INGRESE LA CATEGORIA DEL LIBRO")
        categ = input()
        if param == "guardar":
            save({"titulo":title, "lan":idioma, "author":autores, "year":year, "price":price, "category":categ})
            sleep(3)
            print("LIBRO REGISTRADO EXITOSAMENTE")
            
        elif param == "editar":
          edit({"titulo":title, "lan":idioma, "author":autores, "year":year, "price":price, "category":categ}, name) 
    except:
        print("ERROR EN EL REGISTRO")
#MOSTRAR POR NOMBRE DEL LIBRO
def showByName(name):
    books = jsonOpen()
    try:
        search = [x for x in books["bookstore"]["book"] if x["title"]["__text"].lower() == name.lower()]
        print("titulo\t\tAutor\t\tAño\t\tPrecio\t\tCategoria")
        print(search[0]["title"]["__text"],"\t\t", search[0]["author"], "\t\t",search[0]["year"],"\t\t", search[0]["price"], "\t\t",search[0]["_category"])
        input("-- ingresa cualquier tecla para continuar... ")
    except:
        print("NO SE ENCONTRO DICHO LIBRO")
opc = ""
def eliminar(name):
    books = jsonOpen()
    try:
        search = [x for x in range(len(books["bookstore"]["book"])) if books["bookstore"]["book"][x]["title"]["__text"].lower() == name.lower()]
        books["bookstore"]["book"].pop(search[0])
        print("LIBRO ELIMINADO CORRECTAMENTE")
        with open("Biblioteca.json", "w") as archivo: json.dump(books, archivo)
        archivo.close()
        sleep(3)
    except:
        print("HUBO UN ERROR AL MOMENTO DE ELIMINAR")
while opc != "0":
    show()
    opc1 = input()
    match opc1:
        case "1":
            showData()
        case "2":
            formulario("guardar")
        case "3":
            print("INGRESE EL NOMBRE DEL LIBRO QUE DESEA BUSCAR")
            name = input()
            showByName(name)
        case "4":
            showData()
            print("INGRESAR EL NOMBRE DEL LIBRO QUE DESEA EDITAR")
            name = input()
            formulario("editar",name)
        case "5":
            showData()
            print("INGRESAR EL NOMBRE DEL LIBRO QUE DESEA ELIMINAR")
            name = input()
            eliminar(name)
        