'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]

[3,2,4] [3,3] [2,7,11,15]
'''

nums = [2,7,11,15]
target = 9

# 解法1：哈希表 时间复杂度O(n) 空间复杂度O(n) 哈希表最多需要存n-1个键值对，使用的容量与数组线性相关
# 查找表法 以空间换时间 有两种常见的方式 1.哈希表 2.平衡二叉搜索树 由于不需要维护查找表中的顺序性，因此哈希表是首选
def twoSum(nums, target):
    outcome = []
    hashmap = dict(enumerate(nums))
    for index,value in enumerate(nums):
        n = target - value
        hashmap.pop(index)
        if n in hashmap.values() :
            outcome.append(index)
        hashmap[index]=value
    return outcome

print(twoSum(nums,target))


####最标准答案
def twoSum(nums, target):
    hashmap={}
    for index,value in enumerate(nums):
        if target-value in hashmap.keys():
            return sorted([index,hashmap[target-value]])
        else:
            hashmap[value]=index

print(twoSum(nums,target))


#解法2：暴力枚举 时间复杂度O(n2) 空间复杂度O(1)，只用到常数个临时变量 可以遍历出所有情况

def twoSum(nums, target):
    for index1,value1 in enumerate(nums):
        for index2,value2 in enumerate(nums[index1+1:]):
            if value1 + value2 == target:
                return sorted([index1,index1+1+index2])

print(twoSum(nums,target))

def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSum(nums,target))
