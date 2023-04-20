for i in range(5):
    print("ingrese el nombre del estudiante")
    nombre = input()
    print("Ingrese la nota 1 ")
    nota1 = float(input())
    print("Ingrese la nota 2 ")
    nota2 = float(input()) 
    print("Ingrese la nota 3 ")
    nota3 = float(input())
    prom = (nota1 + nota2 + nota3) / 3
    paso = " reprobado"
    if(prom >= 3):
        paso = " aprobado"
    print(f"Nombre:{nombre}\nnota1:{nota1}\nnota2:{nota2}\nnota3:{nota3}\nPromedio: \n{prom}{paso}") 