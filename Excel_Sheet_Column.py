n=int(input())
s=''
while(n>0):
    rem=(n-1)%26
    s=chr(65+rem)+s
    n=(n-1)//26
print(s)