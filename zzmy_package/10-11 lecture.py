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

