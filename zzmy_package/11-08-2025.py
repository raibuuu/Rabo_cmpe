
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