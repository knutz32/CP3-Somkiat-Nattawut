def calculator(x,y):
    if operation == "+":
        print(x, "+", y, "=",x+y)
    elif operation == "-":
        print(x, "-", y, "=",x-y)
    elif operation == "*":
        print(x, "*", y, "=",x*y)
    elif operation == "/":
        print(x, "/", y, "=",x/y)
    else:
        print("Operation incorrect !")

number1 = int(input("Enter first number : "))
operation = input("Select operation (+, - , * , /) : ")
number2 = int(input("Enter second number : "))

calculator(number1, number2)
