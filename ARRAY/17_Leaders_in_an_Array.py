##BRUTUAL FORCE
arr = [10,22,12,3,0,6]
n = len(arr)
new_arr = []
max_right=arr[-1] ##6 is always a leader because there is no element on the right side of it. so we can say that the last element is always a leader.
new_arr.append(arr[-1]) ##6 is added to newarray because it is a leader.

for i in range(n-1,-1,-1): ##index=5;so we want from 4,3,2,1,0 and no need the last index.thats why we use len(arr)-2.
    if arr[i] > max_right:
        max_right = arr[i]
        new_arr.append(arr[i])
new_arr.reverse()
print(new_arr)
print("=============my own==============")
arr=[2,7,8,9,3,0,2]
new_arr=[]
right_side=arr[-1]
new_arr.append(arr[-1])
for i in range(n-1,-1,-1):
    if arr[i] > right_side:
        right_side=arr[i]
        new_arr.append(arr[i])
new_arr.reverse()
print(new_arr)
print("---------------------------------")
##some optimal
# def leaders(arr):
#     n = len(arr)
#     ans = []
#     max_right = arr[-1]
#     ans.append(arr[-1])

#     for i in range(n - 2, -1, -1):
#         if arr[i] > max_right:
#             ans.append(arr[i])
#             max_right = arr[i]
#     ans.reverse()
#     return ans


# arr = [10,22,12,3,0,6]
# print(leaders(arr))

# #clean version
# print('=========chatgpt version=========')
# def leaders(arr):
#     ans = []
#     for i in range(len(arr)):
#         leader = True
#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[i]:
#                 leader = False
#                 break
#         if leader:
#             ans.append(arr[i])
#     return ans
# arr = [10,22,12,3,0,6]
# print(leaders(arr))
print("=============no function used own progra(build by me!)=======================")
arr=[2,7,8,9,3,0,2]
new_arr=[]
right_side=arr[-1]
new_arr.append(arr[-1])
for i in range(n-1,-1,-1):
    if arr[i] > right_side:
        right_side=arr[i]
        new_arr.append(arr[i])
print(new_arr)
##using reverse algorithm
left=0
right=len(new_arr)-1
while left < right:
    new_arr[left],new_arr[right]=new_arr[right],new_arr[left]
    left = left + 1
    right = right -1
print("new array is:",new_arr)