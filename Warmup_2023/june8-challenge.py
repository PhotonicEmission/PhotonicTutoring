#read integers from the user until it is not an integer, and then print all the integers back.
userList= []
# userItem=(int(input("Input an integer: ")))

# rawInput=input("int: ")
# convertedInput=int(rawInput)
    #while isinstance(userItem,int)==True:
        #userList.append(userItem)

try:
    while True:
        userList.append(int(input("Input an integer: ")))
except:
    print('That is not an integer.')
print('\n'+"Here are the integers you entered: ")    
print(*userList,sep='\n')
# print(*userList,sep='\n')

# Input an integer: 4
# Input an integer: -
# That is not an integer.

# Here are the integers you en