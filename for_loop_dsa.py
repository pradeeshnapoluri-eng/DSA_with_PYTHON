# a=[1,9,78,54]
# for i in a:
#     print(a[2])
#      print(i)
# print("good job")
##################################################################
# a=[1,6,7,8,1,0,1,84]##here we used cuz b make the list based on a.like it ets the same length
# b=0
# for i in range(7):
#     if i==1:
#         b+=1
#     print(b)
# print("output is:\n")
# print(b)
#print("===================================================")
arr=[2,3,4,5,6,7,11,12,33,27,89,15,19,17,16,32]
for i,j in enumerate(arr): #i,j=index,value
    print([i],[j])

print('============================================')
arr=[12,33,9,10,78]
for i in range(len(arr)):
    print(arr[i])
print()
for i in range(len(arr)):
    if arr[i] % 3 == 0:
        print(arr[i], "is divisible by 3")
print() ##outside loop
print(arr[i]) ## this will print the last element of the array because after the loop i will be equal to the last index of the array which is 4 in this case.