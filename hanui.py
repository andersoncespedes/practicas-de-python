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
hanoi("a", "c", "b",5)