userInput = int(input("Enter number : "))
for x in range(userInput):
    print(" "*(userInput-(x+1))+("*"*(2*x+1))+" "*(userInput-(x+1)))
