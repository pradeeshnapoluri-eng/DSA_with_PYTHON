def sort_012(arr):

    zero = arr.count(0)
    one = arr.count(1)
    two = arr.count(2)

    for i in range(zero):
        arr[i] = 0

    for i in range(zero, zero + one):
        arr[i] = 1

    for i in range(zero + one, len(arr)):
        arr[i] = 2

    return arr


arr = [2,0,1,0,2,1]

print(sort_012(arr))

print("=======================================")
def sort_012(arr):

    zero = arr.count(0)
    one = arr.count(1)
    two = arr.count(2)

    for i in range(zero):
        arr[i] = 0

    for i in range(zero, zero + one):
        arr[i] = 1

    for i in range(zero + one, len(arr)):
        arr[i] = 2

    return arr


arr = [2,0,1,0,2,1]

print(sort_012(arr))