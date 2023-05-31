#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
fname=fname[::-1]
lname=lname[::-1]
print(str(lname)+" "+str(fname))