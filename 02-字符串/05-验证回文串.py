'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
'''
s = ""
#空间复杂度O(N) 时间复杂度O(N/2)
def isPalindrome(s):
    s = ''.join([str(i) for i in s])
    s_new = ''.join(filter(str.isalnum, s)) #str.isalpha 判断是否为字母 #isalnum 为字母与数字的组合
    s_new = s_new.lower()
    for i in range(len(s_new)//2):
        if s_new[i] != s_new[len(s_new)-1-i]:
            return False
    return True

print(isPalindrome(s))

###官方答案
#1. 筛选+判断
def isPalindrome(s):
    sgood = "".join(ch.lower() for ch in s if ch.isalnum())
    return sgood == sgood[::-1]


#2. 双指针

class Solution:
    def isPalindrome(s):
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True

#3. 在原字符串上进行判断 空间复杂度O(1)
def isPalindrome(s):
    n = len(s)
    left, right = 0, n - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1

    return True

