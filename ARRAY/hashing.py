# freq={
#     'mom':2,
#     'dad':1,
#     'bro':3,
# }
# print('mom appears:', freq['mom'], 'times')
# print('dad appears:', freq['dad'], 'times')
# print('bro appears:', freq['bro'], 'times')
# print('------------------------------------------------------------------')
##without DICTIONARY
# arr=[2,2,3,4,5,1,2,2]
# my=3
# count=0
# # for i in range(len(arr)): ##both are same
# for i in arr:
#     if arr[i] == my:
#         count += 1
# print(my, 'appears:', count, 'times')
# print('--------------------------------------------------------------------')
# arr=[3,1,2,3,3,5,7,3]
# target=3
# count=0
# for i in arr:
#     if arr[i] == target:
#         count += 1
#     else:
#         count=1
# print(target, 'appears:', count, 'times')
# print('----------------------------------------------------------------------')
arr=[1,7,11,13,5]
target=9
seen = {}
for i, num in enumerate(arr):
    partner = target - num
    print(arr[i],partner)
    