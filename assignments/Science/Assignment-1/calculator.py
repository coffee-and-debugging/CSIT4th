num1= float(input("enter first number here:"))
num2= float(input("enter second number"))

print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")

choice =int(input("enter your choice from 1-4:"))
if choice ==1:
    print(num1+num2)

elif choice ==2:
    print(num1-num2)

elif choice ==3:
    print(num1*num2)

elif choice ==4:
 print(num1/num2)

else:
   print ("Invalid  Input")