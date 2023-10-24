def add(a,b):
    sum=a+b
    print("sum of",a,"and",b,"is",sum)

def subs(a, b):
        sub = a - b
        print("subtraction of", a, "and", b, "is", sub)

def mul(a, b):
            mult= a *b
            print("multiplication of", a, "and", b, "is", mult)
def div(a, b):
             divi =a/b
             print("division of", a, "and", b, "is", divi)

count=0
while count<=5:
 print("select operation:")
 choice=input("ADD\nsubtract\nmultiply\ndivide\nchoice:")

 if choice=="ADD":
    x=int(input("Enter value:"))
    y = int(input("Enter value:"))
    add(x,y)

 elif choice=="subtract":
    x = int(input("Enter value:"))
    y = int(input("Enter value:"))
    subs(x, y)
 elif choice == "multiply":
    x = int(input("Enter value:"))
    y = int(input("Enter value:"))
    mul(x, y)
 elif choice == "divide":
    x = int(input("Enter value:"))
    y = int(input("Enter value:"))
    div(x, y)

count=count+1


