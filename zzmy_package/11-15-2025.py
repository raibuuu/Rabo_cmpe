import time
#difference of Continue and Return

def any_function_name():
    """This function is a sample code for Continue and Return."""
    message = "Stop kana!"
    for i in range(0, 100, 1):
        time.sleep(0.2)
        if i == 50:
            continue
        elif i == 75:
            return message
        print("Value of i is : " + str(i))
    return None

print(any_function_name())



listofNumbers = [25, 33, 45, 67, 90]

def add_function(a, b):
    """This function is used to add two numbers and return sum."""
    return a + b

def average_function(inputList):
    average = 0
    totalsum = 0
    for i in inputList:
        totalsum = add_function(totalsum, i)
    average = totalsum / len(inputList)
    return average

print(average_function(listofNumbers))


import time
#SIMPLE DEMO OF ATM WITHDRAWAL FLOW

amount = 5000
raivene_balance = 1000
raivene_pin = "123456"

def welcome_message():
    print("================================")
    print("WELCOME TAXPAYER!!")
    print("================================")
    time.sleep(0.5)
    print("Please Insert Your Card")
    print("================================")
    time.sleep(0.5)

def card_reader(isCardDetected):
    if isCardDetected.upper() == "YES":
        print("Card Detected")
        return True
    else:
        return False

def card_ejection():
    print("Card is ejected. Please get your card")

def input_pin_number_and_validate():
    for i in range(3):
        input_pin = input("Please Insert Your PIN Number: ")
        if input_pin == raivene_pin:
            print("PIN Number is valid!!")
            return True
        else:
            print("PIN Number is invalid. Please try again (attempt : " + str(i + 1))
    print("Card is blocked due to 3 failed attempts")
    return False

def transaction_selection():
    print("Available Transcations : WITHDRAW, CHECK BALANCE, CANCEL")
    transaction = input("Please Enter Your Transaction: ")
    return transaction

def cash_dispense():
    print("Please get your cash now")

def print_receipt():
    global raivene_balance
    raivene_balance = raivene_balance - amount
    print("Your Balance : " + str(raivene_balance))
    print("Please get your receipt")

def transaction_validation(amount):
    global raivene_balance
    if amount <= 0:
        print("Invalid Amount")
        return False
    elif raivene_balance > amount:
        print("Valid Amount to Withdraw")
        return True
    else:
        print("Insufficient Balance. Pleae contact your sugar daddi")
        return False


while True:
    welcome_message()
    isCardDetected = input("Is Card Detected? (YES/NO)")

    if not card_reader(isCardDetected):
        time.sleep(0.5)
        continue

    if not input_pin_number_and_validate():
        card_ejection()
        time.sleep(0.5)
        continue

    transaction_selected = transaction_selection()
    if transaction_selected.upper() == "WITHDRAW":
        print("Transaction Selected is WITHDRAW")
        amount = float(input("Please Enter Amount"))
        if transaction_validation(amount):
            card_ejection()
            time.sleep(0.5)
            cash_dispense()
            time.sleep(0.5)
            print_receipt()
            time.sleep(0.5)
        else:
            card_ejection()
            time.sleep(0.5)
    elif transaction_selected.upper() == "CHECK BALANCE":
        print("Transaction Selected is CHECK BALANCE")
        print(raivene_balance)
        card_ejection()
        isContinue = input("Do you want another transaction")
        if isContinue.upper() == "YES":
            print("Please Wait ...")
        else:
            card_ejection()
            break
    else:
        print("Transaction is Cancelled")
        time.sleep(0.5)
        card_ejection()
        continue

    print("Next Step")
    time.sleep(0.5)


