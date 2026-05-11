a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

print("maximum of three number is: ",max(a ,b , c))

if a>=b and a>=c :
    max_num = a
elif b>=a and b>=c :
    max_num = b
else:
    max_num = c

print("maximum of three number is: ",max_num )
