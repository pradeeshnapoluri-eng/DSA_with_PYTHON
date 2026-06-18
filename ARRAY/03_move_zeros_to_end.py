# arr=[1,0,2,0,3,0,4,0,5,0,6,1,4,0,3]
# new_arr=[]
# count=0
# for i in arr:
#     if i != 0:
#         new_arr.append(i)
#     else:
#         count += 1
# for i in range(count):
#     new_arr.append(0)
# print(new_arr)
# print(count)
print('-----------')
arr=[1,2,3,0,9,0,2,0,1]
new=[]
zeroes=0
for num in arr: ##1st for loop lo arr ni iterate chestham
    if num == 0:
        zeroes += 1 ##zeroes=zeroes+1 (iterate chestunam enni 0s unte annitini zeroes variable lo ki add cheymani okkotiga)
    else:
        new.append(num)
for i in range(zeroes): ##2nd for loop lo zeroes ki range() ae inka vadali
    new.append(0)        ##zeroes rasthe zeroes total ni enni unnayo aa number ni yestadi(eg: three zeroes unte [3,3,3])ani chestundi
print(f'new array is: {new}')
print(f'the count of zeroes are: {zeroes}')