'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
'''


#思路：双指针 时间复杂度O(N), 空间复杂度(1)
s = ["H","a","n","n","a","h"]
def reverseString(s):
    for i in range(len(s)//2):
        s[i],s[len(s)-i-1] =  s[len(s)-i-1],s[i]
    return s

print(reverseString(s))




#字符串排序。思路，ASCII码转换后使用冒泡排序

s = ["h","e","l","l","o"]

def reverseString(s):
    for i in range(len(s)-1):
        for j in range(i,len(s)):
            if ord(s[i]) > ord(s[j]):
                s[i],s[j] = s[j],s[i]
    return s

print(reverseString(s))