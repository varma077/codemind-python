a=input()
sum=0
for i in a:
     if i.isdigit():
        sum+=ord(i)-48
print(sum)