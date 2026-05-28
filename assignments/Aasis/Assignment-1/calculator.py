#calculator using python
a=int(input("enter first number:"))
b=int(input("enter second number:"))
ch=input("enter operation(*,+,-,/):")
if ch=='+':
    print( "sum=",a+b)
elif ch=='-':
    print("subtraction=",a-b)
elif ch=='*':
    print("multiplication=",a*b)
elif ch=='/':
    print ("division=",a/b)
else:
    print("invalid choice")