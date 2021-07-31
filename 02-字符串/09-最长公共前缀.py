'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
输入：strs = ["flower","flow","flight"]
输出："fl"
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
'''

#双指针,找到最短的字符串

strs = ["dog","racecar","car"]

def longestCommonPrefix(strs):
    p1 = 0
    str_len_pre = 200
    for i in strs:
        str_len_now = len(i)
        if str_len_now < str_len_pre:
            str_len_pre = str_len_now

    while p1 < str_len_pre:
        pre = strs[0][p1]
        p2 = 1
        while p2 < len(strs):
            now = strs[p2][p1]
            if now == pre:
                p2 += 1
            else:
                break
        if p2 == len(strs):
            p1 += 1
        else:
            break
    return strs[0][:p1]

print(longestCommonPrefix(strs))