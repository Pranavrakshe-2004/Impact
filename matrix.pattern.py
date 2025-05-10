'''pyramid'''
n=int(input("enter your no:"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
         print("*",end=" ")
    print() 