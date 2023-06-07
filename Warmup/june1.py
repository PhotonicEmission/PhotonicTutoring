# #make a slice that captures the seccond item through the last item of a list
# spam = [1,2,3]
# # spam[1:-1]
# # spam[1:]
# # # spam[start:end:step]
# # spam[2]
# # # spam[2]=4
# print(spam*10)
# del spam[1]
# print(spam)
# spam.insert(1,2)
# print(spam)

#print 1,2,3 ten times, each on it's own line
spam=[1,2,3]
# def vaca():
#     spam=[1,2,3]
#     print(spam)

# for x in range(11):
#     x=0
#     x+=x
#     vaca()

for x in spam*10:
    print(x)