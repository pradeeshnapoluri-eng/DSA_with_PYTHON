# arr=[2,7,2,11,15,17] #2nd code ki raskovachu
# target=9
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             print([i],[j])
# print('=====================================================')
# arr=[2,7,1,15,11]
# target=20
# for i in range(len(arr)): #5(our arr)
#     for j in range(i+1,len(arr)): #(start,stop)
#         for k in range(i+2,len(arr)): #(start from that index,stop at last)
#             if arr[i]+arr[j]+arr[k]==target:
#                 print([i],[j],[k])
print('==========================================================')
# arr = [3,2,3,5,2,4,3,3,6,4]
# target = 6
# seen={}
# for i in arr:
#     if i in seen:
#         seen[i]+=1
#         print('if')
#     else:
#         seen[i]=1
# print(seen)
print('====================using dict as arr(key:value)(OLD)(num:index)(NEW)================================')
freq={
    3:2,
    4:39,
}
i=4
print(freq[i])



















# print('------------------CHATGPT----------------------------------------------')
# arr = [2, 7, 11, 15]
# target = 9
# i = 0
# while i < len(arr):
#     j = i + 1
#     while j < len(arr):
#         if arr[i] + arr[j] == target:
#             print(i, j)
#         j += 1
#     i += 1