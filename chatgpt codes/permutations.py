def next_permutation(arr):

    n = len(arr)
    ind = -1

    # Step 1: Find pivot
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            ind = i
            break

    # Step 2: Last permutation
    if ind == -1:
        arr.reverse()
        return arr

    # Step 3: Find smallest greater element
    for i in range(n - 1, ind, -1):
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]
            break

    # Step 4: Reverse suffix
    left = ind + 1
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = [1,3,2]
print(next_permutation(arr))