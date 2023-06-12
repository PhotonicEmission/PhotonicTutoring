#read integers from the user until it is not an integer, and then print all the integers back.
userList= []
# userItem=(int(input("Input an integer: ")))

try:
    while True:
    #while isinstance(userItem,int)==True:
        #userList.append(userItem)
        
        userList.append(int(input("Input an integer: ")))
        continue
except:
    print('That is not an integer.')
print('\n'+"Here are the integers you enetered: ")    
print(*userList,sep='\n')