nums = [1,5,3,2,2,7,6,4,8,9]

def findErrorNums(nums):
    compare = list(range(1,len(nums)+1))
    for i in compare:
        if i not in nums:
            absence = i
    sorted_nums = sorted(nums)
    for i in range(0, len(nums) - 1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            return sorted_nums[i],absence
    # count = 0
    # i = 0
    # j = 1
    # while i <= len(nums) - 1:
    #     while j <= len(nums) - 1:
    #         if nums[i] == nums[j]:
    #             count = 1
    #         if count == 1:
    #             repe = nums[i]
    #             break
    #         j = j + 1
    #     if count == 1:
    #         break
    #     else:
    #         i = i + 1
    #         j = i + 1

    # return repe,absence


print(findErrorNums(nums))
