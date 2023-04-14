import random as ra
arr = [[ra.randint(100,1000) for x in range(4)] for fila in range(4)]
columna = []
diagonal = []
secDiagonal = []
yUlt = len(arr) - 1
for y in range(len(arr)):
    print(str(arr[y]))
    xUlt = len(arr) - 1
    for x in range(len(arr[y])):    
        if x == 0:
            columna.append(arr[y][x])
        if x == y:
            diagonal.append(arr[y][x])
        if yUlt == xUlt:
            secDiagonal.append(arr[yUlt][xUlt])
        xUlt -=1
    yUlt-=1

print("primera fila:", arr[0])
print("primera columna:",columna)
print("diagonal", diagonal)
print("segundo diagonal", secDiagonal)



