# Which of the following are operators, and which are values?

# # *
# multiply operator
# # 'hello'
# string vallue that says hello
# # -88.8
# float value of -88.8 
# # -
# subraction operator
# # /
# division opperator
# # +
# addition operator
# # 5
# IT'S A 5. AN INTERGER 5.


# What does the following code do?
# while (spam = 10):

# What does the variable bacon contain after the following code runs?

# bacon = 20
# bacon + 1

# what happens if you run the following?
# 'I have eaten ' + str(99) + ' burritos.'

# a < b 

# b > a
# not a > b
def timesTable(Multiplier, MaxMultiplicand):
    i=1
    while i<=MaxMultiplicand:
        result=Multiplier*i
        #if result%10!=0:
        print(str(Multiplier)+" x "+str(i)+" = "+str(result))
        i=i+1
    
timesTable(
    int(input("Enter Multiplier value: ")),
    int(input("Enter Maximum value to be multiplied: ")))