print("enter two number to perform operation:")
a = int(input("value of a:\n"))
b =int(input("value of b:\n"))
print('enter the operation to be performed \n1 for multiply \n 2 for divide \n 3 for add \n 4 for subtract')
choice = int(input("from 1-4:\t"))
if(choice == 1):
    print("multiply: a*b:", a*b)
elif(choice==2):
    print("divide:", a/b)
elif(choice==3):
    print("add:", a+b)
else:
    print("subtract:", a-b)