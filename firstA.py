target= ["clarity","cake","potato","demonstrably"]

def firstA(target):
    indexA = target.index("a")
    return indexA
list=[]
for string in target:
    result = firstA(string)
    print(result)
    list.append(result)
print(list)

