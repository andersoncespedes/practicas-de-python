def hanoi(p1, p3, p2, n):
    if n > 1:
        print("p1 " + p1)
        print("p3 " + p3)
        print("p2 " +p2)
        hanoi(p1,p2,p3,n-1)
        hanoi(p1,p3,p2,1)
        hanoi(p2,p3,p1,n-1)
    else:
        print( p1 + "----->"+ p3)
def honor(a = 1):
    print(a)
def holor(a,b,**c):
    print(c)
honor(4)
holor(4,2,4,5,6,7,8,9)

