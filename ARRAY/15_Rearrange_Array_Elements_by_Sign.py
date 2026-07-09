arr=[3,5,-2,-4,-2,6,-1,-8,7,9,-3,1] #given array should equal number of positive and negative numbers
ans=[0]*len(arr) #creates an array of 0's with the same length as arr
pos=0   #it shows the index of the positive numbers in the ans array(even index)
neg=1   #it shows the index of the negative numbers in the ans array(odd index)
# print(ans)

for i in arr:  #iterating through the elements of the array
    if i > 0:
        ans[pos]=i #ans[pos] is assigned the value of i if i is positive
        pos+=2     #it increments the pos variable by 2 to move to the next even index for the next positive number
                   #0,2,4,6,...

    else:
        ans[neg]=i #ans[neg] is assigned the value of i if i is negative
        neg+=2     #it increments the neg variable by 2 to move to the next odd index for the next negative number
                   #1,3,5,7,...

print(ans)

# Positive → even indexes → jump by 2
# Negative → odd indexes → jump by 2