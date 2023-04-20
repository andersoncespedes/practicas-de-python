import random as ra
arr = [[ra.randint(100,1000) for x in range(3)] for fila in range(3)]
columna = []
diagonal = []
secDiagonal = []
yUlt = len(arr) - 1
xUlt = len(arr) - 1
x= 0
for y in range(len(arr)):
    print(str(arr[y]))
    columna.append(arr[y][0])
    diagonal.append(arr[y][x])
    secDiagonal.append(arr[y][xUlt])
    yUlt-=1
    xUlt-=1
    x+=1
print("primera fila:", arr[0])
print("primera columna:",columna)
print("diagonal Izquierdo:", diagonal)
print("diagonal Derecho:", secDiagonal)



