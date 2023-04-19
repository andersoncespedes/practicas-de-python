import time
import os

def generarId(para):
    nuevaId = (len(para.keys()) - 1) + 1 if len(para.keys()) > 0 else 0
    return nuevaId

articulos = {
    1:{"prod":"lapiz", "valor":2500},
    2:{"prod":"Cuaderno", "valor":3800},
    3:{"prod":"Borrador", "valor":1200},
    4:{"prod":"Calculadora", "valor":3500}, 
    5:{"prod":"Escuadra", "valor":3700}
    }
cliente = {
}
    
prod = [str(x) +"."+ articulos[x]["prod"] + " " + str(articulos[x]["valor"]) + "\n" for x in articulos]
opc = ""
while opc != "S":
    os.system("clear")
    print("".join( prod ))
    print("Seleccione un producto")
    selec = int(input())
    total = 0
    if selec <= len(articulos) and selec > 0:
        print("cantidad?")
        cant = int(input())
        cliente[generarId(cliente)] =  {
            "articulo":articulos[selec]["prod"],
            "cantidad":cant,
            "valor": articulos[selec]["valor"] * cant,
            }
    else:
        print("error")
        time.sleep(2)
        continue
    opc = input("desea continuar S/N?")
os.system("clear")
print('''Articulo | Cantidad | Valor''')
for i in cliente:
    print(f'''{cliente[i]["articulo"]}  {str(cliente[i]["cantidad"])}  {str(cliente[i]["valor"])}''')
print("total:", str(sum([cliente[x]["valor"] for x in cliente])))