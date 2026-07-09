arr=[2,8,7,4,5,9]
new_arr=[0,1,[]]
complete=True
while True:
    if arr not in new_arr:
        arr.sort()
        new_arr.append(arr)
    else:
        complete=False
        break
    print(new_arr)