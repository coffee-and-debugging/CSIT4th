# Common calulation performer(simple calculator) code, developed by Aamos Raut.


a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
print("\n ++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("Select the operation you want to perform:\n")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("\n ++++++++++++++++++++++++++++++++++++++++++++++++++\n")


add = a+b
sub = a-b
mul = a*b
div = a/b


choice = input("Enter your choice (1/2/3/4): ")
if choice == '1':
    print(f"Addition of {a} and {b} is {add}")
elif choice == '2':
    print(f"Subtraction of {a} and {b} is {sub}")
elif choice == '3':
    print(f"Multiplication of {a} and {b} is {mul}")
elif choice == '4':
    print(f"Division of {a} and {b} is {div}")
else:
    print("Invalid input! Please select a valid operation.")
