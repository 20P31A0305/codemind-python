n,m=map(int,input().split())
a=[int(x)for x in input().split()]
b=[int(x)for x in input().split()]
c=0
for i in b:
    if i in a:
        if b.count(i)==a.count(i):
            print("Yes")
            break
else:
    print("No")