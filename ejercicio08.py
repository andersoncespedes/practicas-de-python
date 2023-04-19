tupla = (1,2,3)

milist =[9,8,7,6,5,4,3,2,1]
m = len(milist)
for i in range(m-1):
    for j in range(i+1, m):
        if milist[i] > milist[j]:
            t = milist[i]
            milist[i] = milist[j]
            milist[j] = t
arr = [{"asd":10, "animal":"perro"}, {"asd":7, "animal":"gato"},{"asd":1, "animal":"leon"}, {"asd":4, "animal":"jirafa"},]
def fun(a):
    return a["asd"]
arr.sort(key=fun)
print(arr)
print(milist)