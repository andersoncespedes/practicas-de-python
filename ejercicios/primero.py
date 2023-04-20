import io
print("nombre del archivo")
nombre = input()
try:
    archivo_txt = open(nombre + '.txt', 'r')
    linea = int(input("ingrese la linea del archivo"))
    lista_nombre = archivo_txt.readlines()
    archivo_txt.close()
    print(lista_nombre[linea - 1])
except:
    print("ingreso mal el nombre")

