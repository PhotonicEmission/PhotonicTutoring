# #print the number 1-10 using a while loop, but the nubmers all have to be on one line
# x=1
# while x<11:
#     print(x, end='')
#     if x<=9:
#         print(", ", end="")
#     x+=1

# print()

# x=1
# while x<10:
#     print(x, end=', ')
#     x+=1

# print(x, end='')

# for x in range(1,10):
#     print(x, end=', ')
# print(x)


# without deleting anything, add a statement to make this only print 0 through 7
# for i in range(100):
#     if i <= 7:
#         print(i)
#     else:
#         break

# print(i)

# for i in range(100):
#     print(i)
#     if(i>=7):
#         break

# print(i)


# Do not print 'sun'
# weather=["snow", "rain", "sun", "clouds"]
# for i in weather:
#     if i !="sun":
#         print(i)
    

# # Do not print 'sun'
# weather=["snow", "rain", "sun", "clouds", "meatballs"]
# for i in weather:
#     if i =="sun":
#         continue
#     print(i)    
    

# #take user input: temperature. If they have a fever, tell them.
# my_temp=float(input("What is your temperature: "))

# if my_temp>99:
#     print("You have a fever.")
# else:
#     print("Your temperature is fine")
# #my_temp=97.70

# print(round(my_temp))

#read integers from the user until it is not an integer, and then print all the integers back.

userInt=input("Input an integer: ")
try:
    while True:
        print(userInt)
except:
    print('That is not an integer.')