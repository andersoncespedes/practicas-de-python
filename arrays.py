arr = [
[0,0,0], 
[0,0,0], 
[0,0,0]]
car = []
f = 1
x = 1
y = 0
while f <=  len(arr) * len(arr):
    if y < 0:
        y = len(arr) - 1
    if x == len(arr):
        x = 0 
    if arr[y][x] != 0:
        y+= 2 if y+2 < len(arr) else 0 
        x-= 1 if x -1 >= 0 else len(arr) - 1
    if arr[y][x] == 0:
        arr[y][x] = f
    x+=1
    y-=1
    f+=1        
a = [str(x) + "\n" for x in arr]
print("".join(a))