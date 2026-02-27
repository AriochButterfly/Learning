# Variables for List Items
FruitsList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "rhubarb"]
NumberList = [1, 5, 7, 9, 3]
BoolList = [True, False, False]
AllList = ["abc", 34, True, 40, "male"]
FruitsList2 = list(("apple", "banana", "cherry"))

# Python List
print("Start of Python List")
print(FruitsList)
print(len(FruitsList))
print(type(FruitsList))
print(FruitsList2)

# Access List Items
print("Start of Access List Items")
print(FruitsList[1])
print(FruitsList[-1])
print(FruitsList[2:5])
print(FruitsList[:4])
print(FruitsList[2:])
print(FruitsList[-4:-1])

if "apple" in FruitsList:
    print("Yes, 'apple' is in the fruits list.")

if "rhubarb" in FruitsList:
    print("Rhubarb is a vegetable dumbass.")

# Change List Items
print("Start of Change List Items")
FruitsList[7] = "tomato"
print(FruitsList)
print("This list is now actually all fruits, you're welcome.")
FruitsList[1:3] = ["blackcurrant", "watermelon"]
print(FruitsList)
FruitsList[1:2] = ["blackcurrant", "watermelon"]
print(FruitsList)
FruitsList[1:3] = ["watermelon"]
print(FruitsList)
FruitsList.insert(4, "strawberries")
print(FruitsList)

# Add List Items
print("Start of Add List Items")


# Remove List Items
print("Start of Remove List Items")


# Loop Lists
print("Start of Loop List")


# List Comprehension
print("Start of List Comprehension")


# Sort Lists
print("Start of Sort List")


# Copy Lists
print("Start of Copy List")


# Join Lists
print("Start of Join List")
