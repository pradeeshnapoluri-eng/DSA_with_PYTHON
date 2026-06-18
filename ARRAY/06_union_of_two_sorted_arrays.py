arr1 = [1,2,3]
arr2 = [2,3,4]
arr3=[2,3,4,5,6]
union=[]
for i in arr1:
    if i not in union:
        union.append(i)
for j in arr2:
    if j not in union:
        union.append(j)
for k in arr3:
    if k not in union:
        union.append(k)
print(union)