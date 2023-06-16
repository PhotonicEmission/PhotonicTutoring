#Write a python program that prints out the date and time, and congratulates the user if it's Friday.
# import datetime
from datetime import datetime

def tgif(dateTime):
    # d = dt.isoweekday()
    #print(d)
    if dateTime.isoweekday() == 5:
        print("Congradulations! It's Friday!")

dt = datetime.now()
# dt = datetime(2023, 5,19)
# print("The current date and time is: "+str(dt))
print(dt.strftime("The date and time: %c"))
# print(dt.strftime("The date and time: %I:%M %p %m/%d/%y"))
# print("The current date and time is: "+strfime)

#print("It is a "+dt.strftime('%A'))

tgif(dt)