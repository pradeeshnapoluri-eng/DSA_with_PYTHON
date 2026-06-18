arr=[2,2,3,3,3,4,1,5,1,1]
new_arr=[]
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
print(new_arr)