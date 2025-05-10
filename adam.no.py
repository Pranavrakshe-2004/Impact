''' reverse of suare of given no should reverse square of given no'''
num=int(input("enter your no:"))
m=num*num 
print(m)
n =int(input("enter your no:"))
x=n*n
print(x)
reversed_num = 0
while n> 0:
    digit = n % 10
    reversed_num = reversed_num *10 + digit
    n = n // 10
reversed_square=reversed_num*reversed_num    
print("after reverse the value of",reversed_square)
if reversed_square==m:
    print("adam no")
else:
    print("not a adam no")