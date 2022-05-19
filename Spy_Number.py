t=int(input())
su=0
mu=1
while(t>0):
    r=t%10
    su+=r
    mu*=r
    t//=10
if(su==mu):
    print("Spy Number")
else:
    print("Not Spy Number")