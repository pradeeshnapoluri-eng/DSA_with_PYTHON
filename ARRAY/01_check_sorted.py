# arr=[1,2,3,4,9]
# # arr = [1,2,5,3,4]
# # arr = [1,2,3,4,5,6,2]
# sorted_arr=True
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]: ##1st value is lesser than 2nd value?
#         sorted_arr=False
#         print('nottt')
#     else:
#         sorted_arr=True
#         print('sorted correctly')
# print('------------------------')
# if sorted_arr:
#     print("sorted successfully")
# else:
#     print("not sorted!")
print('===================================================================')
arr = [1,2,3,4,5,6,2]
sorted_arr=True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted_arr=False
        print('nottt')
        break
   
print('------------------------')
if sorted_arr:
    print("sorted successfully")
else:
    print("not sorted!")