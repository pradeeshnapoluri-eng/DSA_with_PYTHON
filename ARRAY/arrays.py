# arr=[10,20,30,40,50]
# print(arr)
# print(arr[2])
# arr[3]=100
# print(arr)
# print()

##traversing
# arr=[1,2,3,4,5]
# for i in arr: ##range used means; range(len(arr)) gives us the indices of the array, while iterating directly over arr gives us the values. Both methods are valid for traversing an array, but they serve different purposes. Using range(len(arr)) allows you to access both the index and the value if needed, while iterating directly over arr is more concise when you only need the values.
#     print(i) 
# print()
##
# arr=[1,2,3,4,5]
# large=max(arr)
# small=min(arr)
# print(f'Large: {large} , small: {small}')

##
# arr = [10,40,20,80,30,100]
# largest=arr[0]     #we can also use arr[-1] to access the last element of the array. This is a common practice in Python to access elements from the end of a list. So, largest=arr[-1] would also work correctly in this case.
# for i in arr:
    # if i>largest:
        # largest=i
# print("Largest element is:",largest)
################################################
#second largest
arr = [15, 8, 25, 10, 30, 26]
largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')
fourth_largest = float('-inf')
fifth_largest = float('-inf')
smallest = float('inf')
# for i in arr:
for i in arr:

    if i > largest:
        
        smallest=fifth_largest
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = second_largest
        second_largest = largest
        largest = i
    
    elif i > second_largest and i != largest:
        smallest=fifth_largest
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = second_largest
        second_largest = i
    elif i >third_largest and i != second_largest and i != largest:
        smallest=fifth_largest
        fifth_largest = fourth_largest
        fourth_largest = third_largest
        third_largest = i
    elif i > fourth_largest and i != third_largest and i != second_largest and i != largest:
        smallest=fifth_largest
        fifth_largest = fourth_largest
        fourth_largest = i
    elif i > fifth_largest and i != fourth_largest and i != third_largest and i != second_largest and i != largest:
        smallest=fifth_largest
        fifth_largest = i
    elif i < smallest:
        smallest = i
    
print("Largest element is:", largest)
print("Second largest element is:", second_largest)
print("Third largest element is:", third_largest)
print("Fourth largest element is:", fourth_largest)
print("Fifth largest element is:", fifth_largest)
print("Smallest element is:", smallest)
print()
