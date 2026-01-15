input("Hello World")
int("Hello Eljaye")
int ('Hello Eljaye Single Quote')
int ('Raivene said "Hello, miss na kita!!"')
int ("Raivene said 'Hello, miss na kita!!'")
int ("Raivene said Hello, miss na kita!!")

int(input("Enter your name :"))

print("First Line")
print("Second Line")
print("Third Line")
print("Fourth Line")
print("Fifth Line")
print("Sixth Line")
print("Seventh Line")
print("Eight Line")
print("Nine Line")

#this is a single line comment
print("hello world")

'''
this is 
a 
multi
line 
comment
'''

a = input("enter first number : ")
b = input("enter second number : ")
c = input("enter third number : ")

mySum = int(a) + int(b) + int(c)

print(mySum)


#convert to int -> int(variable)
#convert to string -> str(variable)
#fstring or formatted string

myAge = 45
myName = "Raivene Rabo"

print ("I am : " + myName + " and my age is : " + str(myAge))

#Alternative Way
print (f"I am : (myName) and my age is : (myAge) ")

#java
#45 integer
#45.1 float
#45213421312321312 long
#45.21312321312323123123 double
#"hello" string
#'h' char
myNum1 = 45
myNum2 = 45.5
myNum3 = 45123213213123123216545454676576567456456456435645475456535435654765465354354654635435432543634564654653543463465465
myNum4 = 45.123123123123232

myString = "hello world !@#$%^&*() 12312312327"
age1 = "21"
age2 = "25"
sum = age1 + age2
print(sum)

myString1 = "Hello"
myString2 = " World"
sum = myString1 + myString2
print(sum)

#
import math

strFullName = "Raivene Rabo"
intLength = len(strFullName) #len for length

print(strFullName)
print(intLength)
print(strFullName[0])
print(strFullName[5])
print(strFullName[9])
print(strFullName[intLength-1])

mySubString = strFullName[3:7:1] #[start included, end excluded, step]
print(mySubString) #substring or slicing

#String methods

newvalue = strFullName.upper()
print(newvalue)
newvalue = strFullName.lower()
print(newvalue)
newvalue = strFullName.capitalize()
print(newvalue)
newvalue = strFullName.title()
print(newvalue)
newvalue = strFullName.split(" ")
print(newvalue)
newvalue = strFullName.split("iv")
print(newvalue)

newvalue = strFullName.replace("i" , "")
print(newvalue)
newvalue = strFullName.replace("abo", "epo")
print(newvalue)

myFirstName = "Raivene"
myMiddleName = "DeLara"
myLastName = "Rabo"

myFullNameList = [myFirstName, myMiddleName, myLastName]
print("-".join(myFullNameList))

newvalue = strFullName.count("e")
print(newvalue)


import math

intA = 25
intB = 15
intC = 5

intSum = intA + intB + intC
print(intSum)
intDiff = intA - intB
print(intDiff)
intProd = intA * intB
print(intProd)
intQuot = intA / intB
print(intQuot)
intResult = intA ** intB
print(intResult)


intAngle = 90
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)

intAngle = 45
result = round(math.cos(math.radians(intAngle)), 1)
print(result)
result = round(math.sin(math.radians(intAngle)), 1)
print(result)
result = round(math.tan(math.radians(intAngle)), 1)
print(result)

intx = 5
facResult = math.factorial(intx)
print(facResult)

myComA = 25+5j
myComB = 10-10j
comProd = myComA * myComB
print(comProd)

#Comparison Operator
# ==, >, <, >=. <, !=
#BOOLEAN DATATYPE True or Flase

intA = 5
intB = 6

isResult = intA == intB
print(isResult) #False

isResult = intA <= intB
print(isResult) #True

isResult = intA >= intB
print(isResult)

isResult = intA != intB
print(isResult)

isResult = intA > intB
print(isResult)

isResult = intA < intB
print(isResult)

isResult = "e" in "Raivene"
print(isResult)
isResult = "e" in "Raivana"
print(isResult)
isResult = "e" not in "Raivana"
print(isResult)
isResult = "e" not in "Raivene"
print(isResult)
myList = ["a", "b", "c"]
myList = ["luffy", "zoro", "chopper", "nami"]
isResult = "zoro" in myList
print(isResult)
isResult = "nami" in myList
print(isResult)
myList = ["luffy", "zoro", "chopper", "nami"]
isResult = "nami" not in myList
print(isResult)
myList = ["luffy", "zoro", "chopper", "nami"]
isResult = "luffy" not in myList
print(isResult)


myInput = "123123123hello3213 12the22 world12"

myOutput = " "

for char in myInput:
    if not char.isnumeric():
        myOutput = myOutput + char

print(myOutput)

#LIST
#CRUD - CREATE READ UPDATE DELETE

fruitsA = ['apple', 'apple', 'orange', 'strawberry', 'banana']
print(fruitsA)

fruitsA.append('orange')
print(fruitsA)

fruitsA.insert(2, 'lychee')
print(fruitsA)

fruitsA.index('banana')
print(fruitsA)

fruitsA[4] = ('pineappple')
print(fruitsA)
print(len(fruitsA))
print(fruitsA.count('apple'))

fruitsA.remove('orange')
print(fruitsA)

print(fruitsA[4])

fruitsA.clear()
print(fruitsA)

#.....
#LIST - ["string"]
#CRUD - CREATE(append.insert) READ(view) UPDATE(assign value by index) DELETE(pop, remove, clear)
fruitsA = ['apple', 'apple', 'orange', 'banana', 'grapes']
fruitsB = ['banana', 'mango', 'lychee', 'orange', 'mango']
fruitsC = ['mango', 'grapes', 'apple', 'mango', 'lychee']

fruitBasket = fruitsA + fruitsB + fruitsC
print(fruitBasket)
print(fruitBasket[2][3])

fruitBasketAdd = fruitsA + fruitsB + fruitsC
print(fruitBasketAdd)

fruitsA.extend(fruitsB)
fruitsC.extend(fruitsC)
print(fruitsA)


#....
#LIST OF A different data types and list
myInfoList = ["RaiBuu", 19, True, ["Chess", "Anime", "Sleeping"]]
print(myInfoList[0])
print(myInfoList[1])
print(myInfoList[2])
print(myInfoList[3])
print(myInfoList[3][1])

#....
#TUPLE - ("string") - enclosed by parenthesis

fruitsA = ('apple', 'apple', 'orange', 'banana', 'grapes')
print(fruitsA[3])
#fruitsA[3] = "pine apple" - not supported, immutable
#print(fruitsA[3])
print(fruitsA.count('apple'))
fruitsB = ('banana', 'mango', 'lychee', 'orange', 'mango')
fruitsC = ('mango', 'grapes', 'apple', 'mango', 'lychee')
fruitBasket = (fruitsA, fruitsB, fruitsC)
print(fruitBasket[2][4])

#....
#SET { } curly brace
#does not allow duplicate
#does not preserve the order
fruitsA = {'apple', 'orange', 'banana', 'grapes'}
fruitsB = {'grapes', 'apple', 'mango', 'lychee'}
fruitsC = {'orange', 'banana'}
fruitsD = {'orange', 'chico'}

fruitsUnion = fruitsA.union(fruitsB)
print(fruitsUnion)

fruitsIntersection = fruitsA.intersection(fruitsB)
print(fruitsIntersection)

fruitsDifference = fruitsA.difference(fruitsB)
print(fruitsDifference)

fruitsDifference = fruitsB.difference(fruitsA)
print(fruitsDifference)

fruitsA = {'apple', 'orange', 'banana', 'grapes'}
fruitsB = {'grapes', 'apple', 'mango', 'lychee'}
fruitsC = {'orange', 'banana'}
fruitsD = {'orange', 'chico'}

print(fruitsC.issubset(fruitsA))
print(fruitsD.issubset(fruitsA))


#....
#DICTIONARY - dict - CURLY BRACES, KEY-VALUE PAIR

myInfo = {"Name" : "Raivene Rabo", "Age" : 18, "Nickname": "RaiBuu"}
print(myInfo)

print(myInfo["Name"])
print(myInfo.get("Name"))
print(myInfo["Age"])
print(myInfo.get("Age"))
print(myInfo["Nickname"])
print(myInfo.get("Nickname"))

myInfo.update({"Age" : 19})
print(myInfo)
myInfo.update({"Address" : "South Caloocan"})
print(myInfo)

#....
myInfo = {
    "Name" : {
        "FirstName" : "Raivene",
        "LastName" : "Rabo"
    },
    "Age": 19,
    "Nickname": "RaiBuu",
    "Hobbies" : [
        "Anime", "Chess", "Sleeping"
        ]
}
print(myInfo)
print(myInfo["Name"]["FirstName"])
print(myInfo["Name"]["LastName"])
print(myInfo["Name"]["FirstName"] + " " + myInfo["Name"]["LastName"])
print(myInfo["Age"])
print(myInfo["Hobbies"])

import time

fruitList = ["apple", "orange", "banana", "cherry"]

for fruit in fruitList:
    print("fruit List includes : " + fruit)

myWord = "pneumonoultramicroscopicsilicovolcanoiosis"
for char in myWord:
    print(char.upper())

myInfo = {
    "name" : "Raivene",
    "age" : "19",
    "school" : "PUP"
}
for anyKey in myInfo:
    print(anyKey)

for anyValues in myInfo.values():
    print(anyValues)

for anyKey in myInfo:
    print(anyKey, myInfo[anyKey])

isConnected = "no"

for i in range(4):
    time.sleep(2)
    isConnected = input("Is Connected?")
    if isConnected == "yes":
        print("Connection is succesful")
        continue
    else:
        print("Request Timeout")


myGrade = 7878

if myGrade >= 97:
    print("Grade is : 1.0")
elif myGrade >= 94:
    print("Grade is : 1.25")
elif myGrade >= 91:
    print("Grade is : 1.50")
elif myGrade >= 88:
    print("Grade is : 1.75")
elif myGrade >= 85:
    print("Grade is : 2.00")
elif myGrade >= 82:
    print("Grade is : 2.25")
elif myGrade >= 79:
    print("Grade is : 2.50")
elif myGrade >= 76:
    print("Grade is : 2.75")

elif myGrade == 75:
    print("Grade is : 3.00")

elif myGrade >= 65:
    print("Grade is : 5.00")

else:
    print("Incoomplete/Withdraw/Dropped")

print("After If Else Condition")

#2nd part
shapeofyou = "ed sheeran"

if shapeofyou.lower() == "Rectangle":
    print("Rectangle")
elif shapeofyou.lower() == "Circle":
    print("Circle")
elif shapeofyou.lower() == "Triangle":
    print("Triangle")
elif shapeofyou.lower() == "Pentagon":
    print("Pentagon")
elif shapeofyou.lower() == "Hexagon":
    print("Hexagon")
elif shapeofyou.lower() == "ed sheeran":
    print("I'm in love with the shape of you")

else:
    print("crush ko si glydel")

print("We push and pull lie a magnet do")

#3rd part
age = 18
citizenship = "Filipino"
residency = 18
isRegistered = False

if citizenship.title() == "Filipino" and age >= 18 and residency >= 6:
    if isRegistered:
        print("You are qualified to vote")
        print("Vote Wisely!")
    else:
        print("You are not qualified to vote, please register first")
elif citizenship.title() == "Filipino" and age < 18 and residency >= 6:
    print("You are not qualified to vote yet due to your age")
elif citizenship.title() == "Filipino" and age >= 18 and residency < 6:
    print("You are not qualified to vote yet due to your insuffficient years of residency")
else:
    print("You cannot vote, failed to comply the guidelines")

#4th part
# ELIGIBLE TO VOTE - CHECKER
age = input("Please enter your age ")
citizenship = input("Please enter your citizenship ")
residency = input("Please enter your months of residency ")
isregistered = input("Are you a registered voter? yer or no ")

# registered, if none within if, else, elif
if citizenship == "Filipino" and int(age) >= 18 and int(residency) >= 6:
    if isregistered == "yes":
        print("You can vote")
    else:
        print("You cannot vote but you may register now")
elif citizenship == "Filipino" and int(age) < 18 and int(residency) >= 6:
    print("You cannot vote but when you are 18 you'll be old enough to register")
elif citizenship == "Filipino" and int(age) >= 18 and int(residency) < 6:
    print("You cannot vote but you can wait til months of residency is >= 6 months")

else:
    print("You cannot vote or register")

#5th part
#==================================================================================================================
print("before loop1")
for x in range(0,10,1):
    print(x)
print("after loop1")
#==================================================================================================================
print("before loop2")
for x in range(10):
    print(x)
print("after loop2")
#==================================================================================================================
print("before loop3")
for x in range(0,10):
    print(x)
print("after loop3")
#==================================================================================================================

#6th part
fruitList = ["apple", "banana", "cherry", "orange", "strawberry"]

for fruit in fruitList:
    print("Fruit List includes:" + fruit)

myWord = "hanggang_tingin_na_lang_ako_kay_glydel"
for char in myWord:
    print(char.upper())

myInfo = {
    "name": "John Lenard Cabradilla",
    "age": 18,
    "gender": "Male",
    "city": "San Juan City",
    "school" : "Polytechnic University Of The Philippines"
}

for anyKey in myInfo:
    print(anyKey)

for anyValues in myInfo.values():
    print(anyValues)

for anyKey in myInfo:
    print(anyKey, myInfo[anyKey])

#7th part
import time

isConnected = "no"

for i in range(4):
    time.sleep(2)
    isConnected = input("Is Connected?")
    if isConnected == "yes":
        print("Connection Successful")
        continue # or break
    else:
        print("Request Timeout")
    print("Will try again in 2 seconds, please be patient")




print("Processing your request now.....")

#8th part
myString = ("HANNAH")
newValue = ""
print(myString[::-1])

for char in myString:
    newValue = char + newValue

print(newValue)
if myString.lower() == newValue.lower():
    print("PALINDROME")
else:
    print("NONPALINDROME")

#9th part

charList = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9',  " ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
"-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"',
",", "<", ".", ">", "/", "?", "\\", "|", "`", "~"]

key = 45
inputMessage = "My Pin Number is 0123456789"
outputMessage = ""
indexCounter = 0

for letter in inputMessage:
    indexCounter = charList.index(letter)
    print(indexCounter)
    outputMessage = outputMessage + charList[(indexCounter + key) % len(charList)]
print(outputMessage)

inputMessage = ""

for letter in outputMessage:
    indexCounter = charList.index(letter)
    print(indexCounter)
    outputMessage = outputMessage + charList[(indexCounter - key) % len(charList)]
print(inputMessage)

letter = input("Please input the letter: ")
pos = charList.index(letter)
print(pos)
#pos1 = charList.index(pos + key)
#print(pos1)
#pos2 = charList.index(pos - key)
#print(pos2)
print(len(charList))

#RESOLVE THE POSSIBLE INDEX ERROR PROBLEM
#GO BACK TO START

#DECRIPTION CODE <------------outputMESSAGE
#----------> inputMESSAGE

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


