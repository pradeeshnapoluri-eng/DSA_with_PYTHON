def Permutations_code(arr):
    n = len(arr)
    ind = -1
    ###(PIVOT)finding the index of the first element which is smaller than its next element from the right
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind = i  ##shows the pivot index.
            break
    ###if no such index is found, it means the array is in descending order and we need to reverse it to get the next permutation
    if ind == -1:
        arr.reverse()
        return arr
    ###finding the index of the smallest element which is greater than arr[ind] from the right
    for i in range(n-1,ind,-1):
        if arr[i] > arr[ind]:
            ###swapping the elements at ind and i
            arr[ind],arr[i] = arr[i],arr[ind]
            break
    ###reversing the elements from ind+1 to the end of the array to get the next permutation
    left = ind+1
    right = n-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr

##start 
arr=[1,3,5,6,7,2,3]
arr=[2,1,3,1,1]
arr=[6,5,4,3,2,1]
arr=[1,2,3]
arr=[1,3,2]
print(Permutations_code(arr))