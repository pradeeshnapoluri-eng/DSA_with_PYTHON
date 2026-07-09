arr=[10,20,30,40,50]
targeted_no=20
def linear_search(arr,targeted_no):
    for i in range(len(arr)):
        if arr[i]==targeted_no:
            return i
    return -1
ans=linear_search(arr,targeted_no)
if ans !=-1:
    print("Element found at index:",ans) 
else:
    print("Element not found!")

print()
#without using function
arr = [10,20,30,40,50]
target = 10

for i in range(len(arr)):
    if arr[i] == target:
        print(i)
        break
else:
    print("Element not found!")

print()
##own

arr=[10,20,30,40,50]
my_choice=20
for i in range(len(arr)):
    if arr[i]==my_choice:
        print(i)
        break
else:
    print("Element not found!")