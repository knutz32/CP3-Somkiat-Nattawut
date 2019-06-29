menuList = []
priceList = []

while True:
    menuName = input("Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Enter Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    totalPrice = 0
    print((" Food Shop ").center(30,"-"))
    for i in range(len(menuList)):
        print("%s \t\t\t %s THB" % (menuList[i],priceList[i]))
        totalPrice += int(priceList[i])
    print("-"*30)
    print("Total Price \t %s THB" % (totalPrice))

showBill()
