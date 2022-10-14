def mi(k,a):
    x=a[k]
    for i in range(k+1,len(a)):
        if a[i]<x:
            x=a[i]
    #print(x)
    return x
def re(b):
    e=[]
    for i in b:
        if i!=0:
            e.append(i)
    return e
n=int(input())
a=list(map(int,input().split()))
k=n
z=0
w=[]
a.sort()
while k>0:
    b=[]
    arr=[]
    v=mi(z,a)
    z+=1
    for i in range(n):
        b.append(a[i]-v)
    c=0
    for i in b:
        if i>=0:
            c+=1
    b=re(b)
    if c not in w:
        w.append(c)
    k-=1
for i in range(len(w)):
    print(w[i])