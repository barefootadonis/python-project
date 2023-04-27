def deposit():
    while True :
     amount = input ("How much would you like to deposit? $")
     if amount.isdigit():
        amount = int(amount)
        if amount > 20:
           break
        else:
           print ("The amount should be greater than 20")
     else:
        print ("Please input a number")
    return amount

def main():
   balance = deposit()
   while True:
        print ("Your current balance is ", balance)
        red = input("Would you like to close the application?")
        if red.lower() == "yes":
           quit()
        else:
           continue

main()