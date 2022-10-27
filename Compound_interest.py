p,r,t=map(int,input().split())
ci=p*((1+r/100)**t)
ci="{:.2f}".format(ci)
print(ci)