for i in range(int(input())):
    n=input()
    b=int(n,16)
    c=(bin(b)[2::])
    while len(c)%4!=0:
        c="0"+c
    print(c)