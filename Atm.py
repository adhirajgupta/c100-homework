cbalance = 50000
nBalance = 50000
def withdraw():
    amount = int(input("how much do you want to withdraw - "))
    nBalance = cbalance - amount
    print("Your new balance is - ",nBalance)    

def balanceCheck(nBalance):
    print(nBalance)




cardno = int(input("Enter your card number - "))
pin = int(input("Enter your pin - "))
option = input("Do you want to withdraw or check your balance - ")
if(option == 'withdraw'):
    withdraw()
else:
    balanceCheck(nBalance)    



