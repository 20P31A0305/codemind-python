n=int(input())
b=0
c=1
while n>0:
    r=n%10
    b+=r
    c*=r
    n//=10
if b==c:
    print('Spy Number')
else:
    print('Not Spy Number')