#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
# uName=input("What is your name? ")
# uAge=input("What is your age? ")
import datetime
uName = "bob"
uAge=40
#what is teh air speed veloicity of a fully laden swallow
currentYear = datetime.datetime.now().year
u100=100-int(uAge)+currentYear

print("Hi "+uName+", you will be 100 years old in "+str(u100))