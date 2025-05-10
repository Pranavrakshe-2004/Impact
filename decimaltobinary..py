''' convert decimal to binary without string '''
n=int(input("enter your no:")) 
binary=0
base=1
while n>0:
    rem=(n%2)
    binary=binary+rem*base 
    n=n//2
    base=base*10
print(binary)    
      