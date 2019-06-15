username = input("Enter Username : ")
password = input("Enter Password : ")

if username == "admin" and password == "password" :
    print("Login Success !\n")
    print("#### Welcome to Fruits Shop ####")
    print("-------- List of fruits --------")
    print("1. Apple\t= 30 THB")
    print("2. Banana\t= 10 THB")
    print("3. Durian\t= 150 THB\n")
    userSelected = int(input("Please enter the number of fruit : "))
    qty = int(input("Please enter the quantity : "))
    if userSelected == 1:
        print("Total : Apple x", qty, "=", 30*qty, "THB")
    elif userSelected == 2:
        print("Total : Banana x", qty, "=", 10*qty, "THB")
    elif userSelected == 3:
        print("Total : Durian x", qty, "=", 150*qty, "THB")
    else:
        print("Incorrect number of fruits !")
else:
    print("Incorrect username or password.")
