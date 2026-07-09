arr = [10,20,30,40,50,40,23,90,45,98,40,12,40]
target = 40
for i in range(len(arr)):
    if arr[i] == target:
        print("element found at index: ",i)
##it checks whole array and finds where the elements in indexes.if one or more than 1 it will print .
##this can used for HASHING to find the frequency of elements in array without using dictionary and using for loop to check whole array and count the frequency of elements.