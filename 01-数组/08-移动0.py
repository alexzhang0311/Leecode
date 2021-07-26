nums=[0,1,0,3,12]

def moveZeroes(nums):
    for i in nums:
        if i == 0:
            nums.remove(0)
            nums.append(0)
    return nums

print(moveZeroes(nums))


