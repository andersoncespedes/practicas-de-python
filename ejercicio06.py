arr = [1,2,3,4,5,6,7,8,9,10]
print("pares:", [x for x in arr if x % 2 == 0])
print("impares:", [x for x in arr if x % 2 != 0])
print("primer elemento:", arr[0])
print("ultimo elemento:", arr[-1])
arr.reverse()
print(arr)