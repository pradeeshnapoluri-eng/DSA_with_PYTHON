# arr = [10,20,30,40,50]
# left = 0
# right = len(arr)-1
# while left < right:
# #while right > left:
#     arr[left],arr[right] = arr[right],arr[left]
#     left += 1
#     right -= 1 
# print(arr)
# print()
# print("own model")
# arr = [11,22,33,44,55,66,77,88,99]
# left = 0
# right = len(arr) - 1
# while left < right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left += 1
#     right -= 1
# print(arr)
print("============with functions=====================================")
def reverse_arr(arr):
    left=0
    right=len(arr)-1
    while left < right:
        arr[left],arr[right]=arr[right],arr[left]
        left += 1
        right -= 1
    return arr
arr=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(reverse_arr(arr))

print("===========youtube==============")

# def reversed(input):
#     array=[]
#     for i in range(len(input)-1,-1,-1):
#         array.append(input[i])
#     return array
# input=[1,2,3,4,5,6]
# print(reversed(input))