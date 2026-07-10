# arr=[1,2,3,4,5,6,7]
# k=3
# for i in range(k): ##3times rotation shifting
    # first = arr[0]  #3times change avvali kabati loop lo 1st ante arr[0] ki ochindi
    ##arr[len(arr)-1]=first ##idi 7 place lo first estadi
    # for j in range(len(arr)-1): #ikada total arr ki change
        # arr[j] = arr[j+1]
    # arr[len(arr)-1] = first ##nested loop bayata last element ni 1st ani rastunam
# print(arr)
print("======================")
arr=[1,2,3,4,5,6,7]
k=3
for i in range(k):
    last=arr[-1]
    for j in range(len(arr)-1,-1,-1):
        arr[j]=arr[j-1]
    arr[0]=last
print(arr)