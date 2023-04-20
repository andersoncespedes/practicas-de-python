'''3. El archivo cotizaciones.csv contiene las cotizaciones de las empresas de la Bolsa de valores de Colombia con las siguientes columnas: 
Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), 
Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de pesos).

Construir una función reciba el archivo de cotizaciones y devuelva un diccionario con los datos del archivo por columnas.
Construir una función que reciba el diccionario devuelto por la función anterior y cree un archivo en formato csv con el valor promedio de cada columna.'''
'''arr = open("cotizaciones.csv", "r")
lista = arr.readlines()
parametro = lista[0].split(",")
parametro.pop()
valores = lista[1:len(lista)]
obj = {}
for i in parametro:
    obj[i] = []
    for j in valores:
        if i == "numero":
            obj[i].append(j.split(",")[0])
        elif i == "pesas":
            obj[i].append(j.split(",")[1])
print(obj)'''
import re
def dictc():
    arr = open("cotizaciones.csv", "r")
    lista = arr.readlines()
    obj = {}
    for i in range(len(lista)):
        if i > 0:
            opc = lista[i].split(",")
            obj[i] = {
                "nombre": opc[0],
                "final": int(opc[1]),
                "maximo":int(opc[2]),
                "minimo":int(opc[3]),
                "volumen":int(opc[4]),
                "efectivo":int(re.sub("\n", "",opc[5]))
            }
    return obj
def creacion(param):
    x = ""
    for i in param:
        x += param[i]["nombre"] + " "+  str(sum([param[i]["final"],param[i]["maximo"],param[i]["minimo"],param[i]["volumen"],param[i]["efectivo"]]) / 5) + "\n"
    archivo = open("cotizaProm.csv", "w")
    archivo.write(x)
    archivo.close()
creacion(dictc())