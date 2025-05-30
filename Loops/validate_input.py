#keep asking user for input until they enter a number between 1 to 10

while True :
    num=int(input("enter a number between 1 and 10 : "))
    if 1<=num <=10:
        print("Thanks")
        break
    else:
        print("Invalid number,try again!")