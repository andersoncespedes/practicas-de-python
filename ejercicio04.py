count = 0
num = int(input("Ingrese una altura: "))
while num > 0.5:
    num -= (num * 10) / 100
    count+=1
print(f"Cantidad de veces que la bola rebotadas: {count}") 

