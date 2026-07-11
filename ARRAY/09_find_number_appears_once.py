# arr=[1,2,2,3,3,3,4,4]
# found=False
# for i in range(1,8):
#     if arr.count(i) == 1:
#         found=True
#         print('once appeared:',i)
# if found == False:
#     print("No single element")

class Leetcode:
    def single_element(self,nums=list[int]):
        result=0
        for i in nums:
            result ^= i
        return result
sol=Leetcode()
# nums=[4,1,2,1,2]
nums=[3,3,4,1,2,4,5,5,2]
print(sol.single_element(nums))
