import io
archivo_txt = open("nombres.txt", "r")
lista_nombre = archivo_txt.readlines()
archivo_txt.close()
print(lista_nombre)
for i in range(len( lista_nombre) ):
    print("Nombre:", lista_nombre[i])