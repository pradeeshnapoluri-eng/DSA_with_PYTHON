arr=[7,1,5,3,6,4]
max_profit=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        profit=arr[j]-arr[i]
        if profit > max_profit:
            max_profit=profit
print(max_profit)