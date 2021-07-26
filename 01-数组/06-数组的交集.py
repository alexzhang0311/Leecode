nums1 = [1,2]
nums2 = [1,1]

def intersect(nums1, nums2):
    rept = []
    if len(nums2) > len(nums1):
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                rept.append(i)
        return rept
    else:
        for i in nums2:
            if i in nums1:
                nums1.remove(i)
                rept.append(i)
        return rept
print(intersect(nums1,nums2))