'''
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。
'''

nums = [1,0,1,0,1]
goal = 2
# nums = [0,0,0,0,0]
# goal = 0

#---------------我的答案 ——结果：超时----------------------------


# from collections import Counter
# def numSubarraysWithSum(nums, goal):
#     count = 0
#     if goal == 0:
#         window = 1
#     else:
#         window = goal
#     while window <= len(nums):
#         step = len(nums) - window + 1
#         # print('窗口:{} 步数:{}'.format(window,step))
#         start = 0
#         while step:
#             temp_list = nums[start:start+window]
#             if Counter(temp_list)[0] < window - goal:
#                 break
#             start += 1
#             step -= 1
#             if sum(temp_list) == goal:
#                 count += 1
#         window += 1
#     return count
#
# print(numSubarraysWithSum(nums,goal))
#
# print("长度:{}\n1的数量:{}\n0的数量:{}\n目标值:{}".format(len(nums),sum(nums),len(nums)-sum(nums),goal))



#正确解答（方式1）前缀+哈希表 时间复杂度：O(n) 空间复杂度：O(n)

# [1,0,1,0,1] goal=2 [1,0,1] [1,0,1] [1,0,1,0] [0,1,0,1
# from itertools import accumulate #获取前缀和
# from collections import defaultdict #若元素不在哈希表中，不会丢出错误
#
# class Solution:
#     def numSubarraysWithSum(self, nums,goal):
#         n = len(nums) #5
#         presum = [0] + list(accumulate(nums)) #[0, 1, 1, 2, 2, 3]
#         hashmap = defaultdict(int, {0:1})  #{0:1,1:2,2:2,3:1}
#         ans = 0
#         for i in range(n): #0-4
#             r = presum[i+1] #1,1,2,2,3
#             l = r - goal #-1,-1,0,0,2 r-goal 等于0
#             ans += hashmap[l]
#             hashmap[r] += 1
#         return ans



#正确解答（方式2）双指针 时间复杂度：O(n) 空间复杂度：O(1)
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        n = len(nums) #nums [1,0,1,0,1] n=5
        ans = l1 = l2 = s1 = s2 = 0
        for r in range(n): #r=0-4
            s1 += nums[r] #1,1,2,2,3
            s2 += nums[r] #1,1,2,2,3
            print("l1:{},l2:{},r:{},s1:{},s2:{},goal:{}".format(l1,l2,r,s1,s2,goal))
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            ans += l2 - l1
        return ans

print(Solution.numSubarraysWithSum(self=Solution,nums=nums,goal=goal))