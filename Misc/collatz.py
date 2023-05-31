#Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1
#Write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.            
# print('Enter a number')
# number = int(input())
# while number!=1:
#      number=collatz(number)

#Exception statment extra credit
print('Enter a number: ')
try:
    number = int(input())
except ValueError:
    print('You must enter an integer type.')
#Input number into collatz() function while number variable is not 1.
while number!=1:
        number=collatz(number)