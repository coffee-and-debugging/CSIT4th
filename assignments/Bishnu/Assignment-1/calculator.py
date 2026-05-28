num1=float(input("enter first number "))
num2=float(input("enter second number"))


print(f"num1:={num1}")
print(f"num2:={num2}")

sign = input("enter operator    :")
try:
    if sign == "+":
        print(num1+num2)

    elif sign == "-":
        print(num1-num2)
     
    elif sign == "*":
        print(num1*num2)
    
    elif sign == "/":
        print(num1/num2)
except:
    print("error occoured")

finally:
    print("done")
