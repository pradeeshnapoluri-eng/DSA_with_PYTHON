# arr=[10, 20, 30, 40]
# sum=0
# for i in arr:
#     sum+=i
# print('sum of elements in the array is:',sum)
# ###
# print()
# ##even and odd numbers in an array
# arr=[10, 15, 20, 25, 30]
# even_count=0
# odd_count=0
# for i in arr:
#     if i %2 == 0:
#         even_count+=1
#     else:
#         odd_count+=1
# total_count=even_count+odd_count
# print('total number of elements in the array is:',total_count)
# print('even numbers in the array is:',even_count)
# print('odd numbers in the array is:',odd_count)
# ####
# print()
# print("another model")
# arr=[10,11,12,13,14,15,21,34,19,23]
# even=0
# odd=0
# for i in arr:
#     if i % 2 == 0:
#         print(i, "is even")
#         even +=1
#     else:
#         print(i, "is odd")
#         odd += 1
# total=even+odd
# print("total is:",total)
# print("even are:",even)
# print("odd are:",odd)
print()
arr = [12,17,22,29,34,41]
even_num=0
odd_num=0
for i in arr:
    if i%2!=0:
        print(i,'is odd')
        odd_num +=1
    else:
        print(i,'is even')
        even_num+=1
total=even_num+odd_num
print("total is: ",total)
print("even are: ",even_num)
print("odd are: ",odd_num)