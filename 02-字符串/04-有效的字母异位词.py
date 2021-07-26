'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
'''
s = "anagram"
t = "nagaram"
import collections
def isAnagram(s, t):
    hashmap_s = collections.Counter([i for i in s])
    hashmap_t = collections.Counter([i for i in t])
    if hashmap_s == hashmap_t:
        return True
    else:
        return False


print(isAnagram(s,t))