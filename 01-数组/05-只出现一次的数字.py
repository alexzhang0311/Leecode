#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#不使用额外空间
# class Solution:
#     def singleNumber(self, nums) -> int:
#         for i in range(0,len(nums)):
#             if nums.count(nums[i]) == 1:
#                 return nums[i]
#
# print(Solution.singleNumber(self='self',nums=[4,1,2,1,2]))


#--------------解法2：位运算----------------------

# class Solution:
#     def singleNumber(self, nums) -> int:
#         n = nums[0]
#         for i in range(1,len(nums)):
#             n = n^nums[i]
#         return n
# print(Solution.singleNumber(self='self',nums=[4,1,2,1,2]))

#------------解法3：投机取巧算法----------------

class Solution:
    def singleNumber(self, nums) -> int:
        sum1=sum(nums)
        sum2=sum(set(nums))
        result=2*sum2-sum1
        return result

print(Solution.singleNumber(self='self',nums=[4,1,2,1,2,3,3]))
