n=int(input())
sum=0
temp=n
while(n>0):
    rem=n%10
    fact=1
    n//=10
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
if(sum==temp):
    print("The number {} is a strong number".format(temp))
else:
    print("The number {} is not a strong number".format(temp))