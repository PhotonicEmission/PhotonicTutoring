#use not in a statement
not 6 == 7
#use or in a statement. CORRECTLY.
(True or False) == True
(True and False) == False
# A*2 = A+A
# 4*2 = 4+4
# "apple"*2 = "appleapple"
34%100
# int(105)/int(4)
int(105/4)
#intialize x=7, iterate over: increment by 3 everytime, until it is at least 20.
# x=7
# while x<20:
#     x+=3
# print(x)
#take user input, and add 20 to it, print the result    
# x=input("Enter an integer")
# x=20+int(x)
# print(x)
spam=[1,2,3]
for x in spam*10:
    print(x)

# This program is a loop that takes the variable spam, and prints it line by line as it loops through the loop 10 times. In this case, because spam specifically has a list in it, the output is printed one line at a time rather than on a single line.