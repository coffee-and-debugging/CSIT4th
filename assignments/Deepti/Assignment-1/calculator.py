x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
z=int(input("Enter 1 for addition,  2 for subtraction, 3 for multiplication, 4 for division: "))
if z==1:
    print("The sum is: ", x+y)
elif z==2:
    print("The difference is: ", x-y)
elif z==3:
    print("The product is: ", x*y)
elif z==4:  
    if y!=0:
        print("The quotient is: ", x/y)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")