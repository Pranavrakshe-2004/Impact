n=int(input("enter your no:"))
m=int(input("enter your no"))
for i in range(n,m):
    first=i//10
    last=i%10
    
    sum = first + last
    prod = first*last
    
    result = sum + prod
    
    if (result == i):
        print(i)