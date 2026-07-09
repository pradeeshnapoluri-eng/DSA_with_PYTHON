# arr = [-2,1,-3,4,-1,2,1,-5,4]
arr=[1,2,-3,4,5,6,7,8,9,10]
max_sum = float('-inf')
for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
        
print(max_sum)
