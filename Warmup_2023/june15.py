import copy
    

a = [1,2,[3,4]]
# a is a reference - list - which is 1, 2, {list reference}
# a = MEM1
# MEM1 = 1, 2 ,MEM2
# MEM2 = 3, 4

b = copy.copy(a)
# first layer copy
# goes to MEM1 and copies all the data in it
# new MEM3 = 1, 2, MEM2
# b = MEM3
c = a
# no copy
# c is set to exactly a so
# c = MEM1

d = copy.deepcopy(a)
# deep copy - goes to MEM1, copies, and goes into every sublist and copies those too
# d = MEM4
# MEM4 = 1, 2, MEM5
# MEM5 = 3, 4

print(a)
print(b)
print(c)
print(d)


b[1]="b1"
c[1]="c1"
print()
print(a)
print(b)
print(c)


b[2][0]="b-2-0"
d[2][1]="d-2-1"

print()
print(a)
print(b)

# a=[0,"new",[3,4]]