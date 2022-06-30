def pal(a):
    rev=0
    temp=a
    while temp>0:
        rem=temp%10
        rev=(rev*10)+rem
        temp//=10
    if rev==a:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if pal(i)==1:
        print(i,end=" ")