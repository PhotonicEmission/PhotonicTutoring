#We are cooking a roast that will be done at 350 degrees.
def roast():
    temperature="done"
    return
done=350
temperature=72
while temperature<done:
    temperature=temperature+1
    if temperature%10==0: #report temperature every 10 degrees
        print(temperature)
print(temperature)
roast()
print(temperature)
