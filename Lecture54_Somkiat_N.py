def Login():
    username = input("Enter username : ")
    password = input("Enter password : ")
    if username == "admin" and password == "password":
        print("Login Success !\n")
        showMenu()
    else:
        print("Username or Password incorrect !")
        return False

def showMenu():
    print("------ Shop ------")
    print("1. Price Calculator")
    print("2. Vat Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">> : "))
    if userSelected == 1:
        print("Total price include vat =", priceCalculate(), "THB")
    elif userSelected == 2:
        print("Price include vat =",vatCalculate(int(input("Enter price : "))), "THB")
    else:
        print("Incorrect !")

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice+(totalPrice*7/100)
    return result

def priceCalculate():
    price1 = int(input("First product price : "))
    price2 = int(input("Second product price : "))
    return vatCalculate(price1+price2)

Login()
