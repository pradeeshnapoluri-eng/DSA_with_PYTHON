n = 13
count = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i,'in')
        count += 1
    
print('----------')
if count == 2:
    print(i,"is Prime")
else:
    print(i,"Not Prime")
print("count is: ",count)
print("======================================================")
# n = 13
# for i in range(1, n+1):
    # if n % i == 0:
        # print(i)