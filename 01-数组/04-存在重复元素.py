#给定一个整数数组，判断是否存在重复元素。
#如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false
#---------------------------解法1-------------------------------
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         breakflag = 0
#         for i in range(0,len(nums)):
#             count = 0
#             for j in range(0,len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#                 if count >= 2:
#                     breakflag = 1
#                     break
#             if breakflag == 1:
#                 break
#         if breakflag == 1:
#             return True
#         else:
#             return False

#--------------------------解法2----------------------------
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         breakflag = 0
#         for i in range(0, len(nums)):
#             if nums.count(nums[i]) >= 2:
#                 breakflag = 1
#                 break
#         if breakflag == 1:
#             return True
#         else:
#             return False
# print(Solution.containsDuplicate(self='self',nums=[2,14,18,22,22]))
#------------------解法3----------------------
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         if len(nums) == 0:
#             return False
#         for i in range(0, len(nums)):
#             if nums.count(nums[i]) >= 2:
#                 return True
#         return False
# print(Solution.containsDuplicate(self='self',nums=[2,14,18,22,22]))


#解法1,2,3超时

#----------------------无敌解法---------------------
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         return len(nums) > len(set(nums))
#
# print(Solution.containsDuplicate(self='self',nums=[2,14,18,22,22]))


nums = [1,1,1,1]
# count = 0
# for i in nums:
#     for j in nums:
#         if i == j:
#             count += 1
#     if count >= 2:
#         for k in range(count-1):
#             nums.remove(i)
#     count = 0
#
# print(nums)
