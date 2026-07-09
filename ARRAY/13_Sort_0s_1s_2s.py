# arr=[2,0,1,0,2,1]
# new_arr=[]
# for i in arr:
#     if i==0:
#         new_arr.append(i)
# for j in arr:
#     if j==1:
#         new_arr.append(j)
# for k in arr:
#     if k==2:
#         new_arr.append(k)
# print(new_arr)
# print("=======def func=======")
# def sorted_num(arr,new_arr):
#     for i in arr:
#         if i==0:
#             new_arr.append(i)
#     for j in arr:
#         if j==1:
#             new_arr.append(j)
#     for k in arr:
#         if k==2:
#             new_arr.append(k)
# arr=[2,0,1,0,2,1,0,0,2,1,0,1,1,1,0,2,2]
# new_arr=[]
# sorted_num(arr,new_arr)
# print(new_arr)
# print("======check sorted.pytype====")
# arr=[2,0,1,0,2,1]
# arr.sort()
# print(arr)
# print("=============================================")
arr=[2,0,1,0,1,0,2,9,2,0]
new_arr=[]
for i in arr:
    if i != 0:
        new_arr.append(i)
new_arr.sort()
for j in arr:
    if j == 0:
        new_arr.append(j)
print(new_arr)