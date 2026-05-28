def add(a,b):
    return a+b

def subtract(a,b):
    return a-b;

def multiply(a,b):
    return a*b

def divide(a,b):
    if b ==0:
        return "Error: infinity"
    else:
        return a/b
    
def modulo(a,b):
    if b==0:
        return "Error: infinity"
    else:
        return a%b

while True:
    print("----- CALCULATOR 😊 -----")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulo")
    print("6.Exit")
    print("-----------------------")

    choice = int(input("Enter your choice from 1 to 6:\n"))

    if choice == 6:
        print("CLEAR BYE! 👋")
        break
    else:
        a = float(input("Enter first number:\n"))
        b = float(input("Enter second number:\n"))

        if choice == 1:
            print("Result:", add(a,b))
        elif choice == 2:
            print("Result:", subtract(a,b))
        elif choice == 3:
            print("Result:", multiply(a,b))
        elif choice == 4:
            print("Result:", divide(a,b))
        elif choice == 5:  
            print("Result:", modulo(a,b))     
        else:
            print("Wrong choice! please enter 1/2/3/4/5/6")


