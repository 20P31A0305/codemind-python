n=int(input())
b=bin(n)[2::]
c=[]
for i in b:
    if i=='1':
        i=0
        c.append(i)
    elif i=="0":
        i=1
        c.append(i)
c1=''.join([str(i) for i in c])
print(int(c1,2))