# arr=[2,4,6,8,10,12,14]
# target=11
# low=0
# high=len(arr)-1

# found=False

# while low <= high:
#     mid = low + (high - low) // 2

#     if arr[mid] == target:
#         print(f'found at index:{mid}')
#         found=True
#         break

#     elif arr[mid] > target:
#         high = mid - 1

#     else:
#         low = mid + 1

# if not found:
#     print(-1)
# print('===========================================================')
arr=[2,6,7,8,3,4,5,1,9]
arr.sort()
# print(arr)
target=6
# arr=[1,3,5,7,9,11,13,15,17,19]
# target=13
low=0
high=len(arr)-1
while low <= high:
    mid=(low+high)//2
    if arr[mid] == target:
        print(f'found at index: {mid}')
        break
    elif arr[mid]>target:
        high=mid-1
    else:
        low=mid+1
