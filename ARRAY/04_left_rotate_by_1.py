# arr=[1,2,3,4,5,6,7,8,9]
# new=[]
# first=arr[0]
# for i in range(1,len(arr)): #1st index nunche kadha ani arr[0] ani pedthe len(arr) val loop lo issues ostay.(eg;arr[0]=7,len(arr)=5..so range(7,5)loop run avadu)
        # print(i, arr[i]) #arr[i] imp
        # new.append(arr[i])
# new.append(first)
# print('-------')
# print(new)
# print('==============================================')
# arr=[1,2,3,4,5,6,7,8,9]
# first=arr[0]
# for i in range(len(arr)-1):
    # arr[i]=arr[i+1]
# arr[len(arr)-1]=first  ##last element = first element ani
# print(arr)
# arr.append(arr[0])
# arr.remove(arr[0])
# print(arr)
print("====================================================")
# arr=[10,30,50,70,90]
arr=['ravi','bhanu','siri','pinky','siya']
first=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=first
print(arr)