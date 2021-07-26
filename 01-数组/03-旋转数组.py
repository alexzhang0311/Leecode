#-------------------解法1-------------------- 超时
# class Solution:
#     def rotate(self, nums, k) -> None:
#         while k >= 1:
#             b = nums[-1:][0]
#             for i in range(len(nums) - 2, -1, -1):
#                 nums[i + 1] = nums[i]
#             nums[0] = b
#             k -= 1
#         return nums
# print(Solution.rotate(self='self',nums=a,k=11939))
#-------------------解法2--------------------
# class Solution:
#     def rotate(self, nums, k) -> None:
#         lenth = len(nums)
#         nums = nums[lenth-k:] + nums[:lenth-k]
#         return nums
#
# print(Solution.rotate(self='self',nums=[1,2,3,4,5,6,7],k=3))
#-------------------解法3--------------------
class Solution:
    def rotate(self, nums, k) -> None:
        if k == 0 or len(nums) == 1:
            return nums
        else:
            k = k % len(nums) #K 超过数据长度
            if k == 0:
                return nums
            else:
                nums[:] = nums[::-1]
                nums[:k] = nums[k-1::-1]
                nums[k:] = nums[len(nums):k-1:-1]
        return nums

print(Solution.rotate(self='self',nums=[-1,2],k=2))

