# arr=[1,0,1,1,0,1]
# count=0
# max_count=0
# for i in arr:
#     if i==1:
#         count+=1
#         if count > max_count:  ##elago great ae
#             max_count = count
#     else:
#         count=0
# print(count)
# print(max_count)    

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        max_nums=0
        for i in nums:
            if i == 1:
                count += 1
                if count > max_nums:
                    max_nums=count
            else:
                count=0
        return count
        return max_nums
            