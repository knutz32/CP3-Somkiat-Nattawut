systemMenu = {"ข้าวมันไก่":35,"ข้าวหมกไก่":35,"ข้าวมันไก่ทอด":40}
menuList = []

def showBill():
    totalPrice = 0
    print((" Food Shop").center(30,"-"))
    for i in range(len(menuList)):
        print("%s \t\t\t %s THB" % (menuList[i][0], menuList[i][1]))
        totalPrice += menuList[i][1]
    print("-" * 30)
    print("Total Price \t %s THB" % (totalPrice))

while True:
    menuName = input("Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()
