t=int(input())
su=0
for i in range(1,t):
    if(t%i==0):
        su+=i
if(su==t):
    print(True)
else:
    print("False")