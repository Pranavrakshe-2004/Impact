n=int(input("enter your no:"))
square=n*n
d=0
temp=n
while temp>0:
    temp=temp//10
    d+=1
divisor=1
i=0
while i<d:
    divisor*=10
    i+=1
right=square%divisor
left=square//divisor
if right+left==n:
    print("karpekar nunber")
else:
    print("not a karpekar number")