'''Read three integers and print their maximum.'''


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

if(a>b and c>a):
    print("a is maximum")
elif(b>c):
    print("b is maximum")
else:
    print("c is maximum")

