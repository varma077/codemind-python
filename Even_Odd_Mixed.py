a=int(input())
ec=oc=0
while a>0:
    r=a%10
    if r%2==0:
        ec+=1
    else:
        oc+=1
    a//=10
if ec!=0 and oc==0:
    print("Even")
elif ec==0 and oc!=0:
    print("Odd")
elif ec>0 and oc>0:
    print("Mixed")