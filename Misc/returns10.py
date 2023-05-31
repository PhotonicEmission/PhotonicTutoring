#if the value is less than 10, if not less than 10, return the value, but regardless of prior statements, return even if it's even 
def ret10(bork):
    if bork%2==0:
        return "even"
    if bork<10:
        return bork+10
    else:
        return bork
    
print(ret10(20))
