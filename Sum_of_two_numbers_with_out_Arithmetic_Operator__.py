a,b=map(int,input().split())
while b:
    data=a&b
    a=a^b
    b=data<<1
print(a)
    