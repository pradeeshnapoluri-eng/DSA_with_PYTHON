# arr=[1,2,3,4,5]
# k=2
# for i in range(len(arr)):
#     current_sum = 0
#     for j in range(i, len(arr)):
#         current_sum += arr[j]
#         if current_sum == k:
#             current_sum += 1
# print(current_sum)
print("----------CHATGPT------------------")
arr = [1,2,3,4]
k = 3
max_len = 0
for i in range(len(arr)): #4
    current_sum = 0
    for j in range(i, len(arr)): #0,4
        current_sum += arr[j]
        # print(arr[j], arr[i], i, j)

        if current_sum == k:
            length = j - i + 1 
            if length > max_len:
                max_len = length

print(max_len)