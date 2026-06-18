arr=[1,2,2,3,3,3,4,4]
found=False
for i in range(1,8):
    if arr.count(i) == 1:
        found=True
        print('once appeared:',i)
if found == False:
    print("No single element")