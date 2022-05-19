import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
A=s*(s-a)*(s-b)*(s-c)
print("%0.2f" %math.sqrt(A))