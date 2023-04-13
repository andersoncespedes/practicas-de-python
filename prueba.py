def factorial(num):
    if num != 0:
        print("hola")
        x = num*factorial(num-1)
    else:
        return 1 
    return x
n = int(input("ingrese el de todos los 'n' elementos: "))
r = int(input("ingrese el de todos los 'r' elementos:  "))
y = n - r
factorialN = factorial(n)
factorialR = factorial(r)
factorialNR = factorial(y)
C = factorialN/(factorialNR * factorialR)
print(C)