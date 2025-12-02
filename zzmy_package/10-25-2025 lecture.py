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
