#calculator (2num only)

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
operator = input("Enter  an operator: ")

if operator == "-":
 print("Result:", num1 - num2)

elif operator == "+":
 print("Result:", num1 + num2)

elif operator == "*":
 print("Result:", num1 * num2)

elif operator == "/":
 if num2 == 0:
  print(" number cannot divide by zero")
 else:
  print("Result:" , num1 / num2)

else:
 print("operator is invalid")