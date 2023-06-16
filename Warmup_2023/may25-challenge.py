#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

# userInput=input("Enter some values separtaed by commas: ")
testValue1 = "1,2,3"
testValue2 = "10, 20, 30"
testValue3 = "one, two three"
userInput = testValue2
result = list()

for stringValue in userInput.split(','):
    result.append(int(stringValue))
    # print(int(stringValue))
    

#result must be a list of the integers
print (result)
