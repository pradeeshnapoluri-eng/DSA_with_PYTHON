# #finding largest to smallest elements in a array without using built in functions
# array=[10,13,9,76,21,24]
# largest=float('-inf')
# second_largest=float('-inf')
# third_largest=float('-inf')
# fourth_largest=float('-inf')
# fifth_largest=float('-inf')
# smallest=float('inf')

# for i in array:
#     if i > largest:
#         smallest=fifth_largest
#         fifth_largest = fourth_largest
#         fourth_largest = third_largest
#         third_largest = second_largest
#         second_largest = largest
#         largest = i
#     elif i>second_largest and i ==largest:
#         smallest=fifth_largest
#         fifth_largest = fourth_largest
#         fourth_largest = third_largest
#         third_largest = second_largest
#         second_largest = i

#     elif i>third_largest and i !=second_largest and i != largest:
#         smallest=fifth_largest
#         fifth_largest=fourth_largest
#         fourth_largest=third_largest
#         third_largest=i
#     elif i>fourth_largest and i !=third_largest and i !=second_largest and i !=largest:
#         smallest = fifth_largest
#         fifth_largest=fourth_largest
#         fourth_largest=i
#     elif i>fifth_largest and i!=fourth_largest and i !=third_largest and i !=second_largest and i !=largest:
#         smallest=fifth_largest
#         fifth_largest=i
#     elif i<smallest:
#         smallest=i
# print('largest element is:',largest)
# print('second largest element is:',second_largest)
# print('third largest element is:',third_largest)
# print('fourth largest element is:',fourth_largest)
# print('fifth largest element is:',fifth_largest)
# print('smallest element is:',smallest)
print()
print('Finding largest to smallest elements in an array without using built-in functions')
# arr = [10,40,20,80,30,100]
# arr.sort()
# print('sorted array is:',arr)
# print('largest element is:',arr[-1])
# print('smallest element is:',arr[0])
# arr.reverse()
# print('sorted array in reverse order is:',arr)

arr = [10,40,20,80,30,100]
largest=arr[0]     
print(largest)