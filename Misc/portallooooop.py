# blah = ["cake", "oil", "cubes", "turret"]

# for blah in (blah):
#     print(blah+' this was a triumph')
#     print(blah+' i\'m making a note here')
# x = 1    
# while (x < 10):
#     print("I am NOT a MORON.")
#     x=x+1
   
    
# Write a function that takes in an array/list of strings and returns an array/list of the positions of the first 'a' in each string.

target= ["clarity","cake","potato","demonstrably"]

def firstA(target):
    indexA = target.index("a")
    return indexA
list=[]
for string in target:
    result=firstA(string)
    # print(result)
    list.append(result)
print(list)
# expected output: [2,1,3,7]

# print(firstA(target))

# foo=["acrobat", "bart", "kuntash"]
# for x, y in enumerate(foo):
#     print(x,y)