n=int(input("enter your no:"))
x=int(input("enter your no:"))
count=0
while n!=0:
    m=n%10
    if m==x:
        count+=1
    n=n//10
print(count)    
