def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
def pre_prime(n):
    while prime(n)==False:
        n=n-1
    return n
def next_prime(n):
    while prime(n)==False:
        n=n+1
    return n
def nearst_prime(n):
    a=pre_prime(n)
    b=next_prime(n)
    c=n-a
    d=b-n
    if c<=d:
        print(c)
    else:
        print(d)
a=int(input())
nearst_prime(a)