'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
s = "leetcode"
返回 0
'''

#思路，哈希表

s = "loveleetcode"
s = "leetcode"

# 时间复杂度O(N^2) 空间复杂度O（1）
# def firstUniqChar(s):
#     for i in range(len(s)):
#         flag = 0
#         for j in range(len(s)):
#             print(i,j,flag)
#             if s[i] == s[j]:
#                 flag += 1
#
#         if flag == 1:
#             return i
#
#     return -1
# print(firstUniqChar(s))

# 时间复杂度O(N) 空间复杂度O(N)
# def firstUniqChar(s):
#     temp_list = [i for i in s]
#     for i in range(len(temp_list)):
#         compare_list=[]
#         compare_list[:] = temp_list
#         compare_list.remove(temp_list[i])
#         if temp_list[i] not in compare_list:
#             return i
#     return -1
#
# print(firstUniqChar(s))

#时间复杂度 O(N) 空间复杂度O(N)
def firstUniqChar(s):
    hashmap={}
    for i in range(len(s)):
        value = s[i]
        if value in hashmap:
            hashmap[value] += 1
        else:
            hashmap[value] = 1
    i = 0
    temp_list = [i for i in hashmap.keys()]
    while i < len(hashmap):
        if hashmap[temp_list[i]] == 1:
            return i
        i+=1
    return -1

print(firstUniqChar(s))

#时间复杂度 O(N) 空间复杂度O(N)
def firstUniqChar(s):
    temp_list = [i for i in s]
    no_replica_list = [] #按顺序创建一个不重复的数组，不可以用set，顺序会乱
    for i in range(len(s)):
        if s[i] not in no_replica_list:
            no_replica_list.append(s[i])
    for i in no_replica_list:
        compare_list=[]
        compare_list[:] = temp_list
        compare_list.remove(i)
        if i not in compare_list:
            for index in range(len(temp_list)):
                if temp_list[index] == i:
                    return index
    return -1

print(firstUniqChar(s))


#官方答案
#1.collection.counter() 函数创建哈希表，时间复杂度O(N),空间复杂度 O(∣Σ∣)，其中 \SigmaΣ 是字符集，在本题中s只包含小写字母，因此 ∣Σ∣≤26
import collections
def firstUniqChar(s):
    frequency = collections.Counter(s)
    for i, ch in enumerate(s):
        if frequency[ch] == 1:
            return i
    return -1
print(firstUniqChar(s))

#2. 哈希表+队列

def firstUniqChar(s):
    position = dict()
    q = collections.deque()
    for i, ch in enumerate(s):
        if ch not in position:
            position[ch] = i
            q.append((s[i], i)) #将字符串中第一次出现的字符和index推入队列 q[0][0] 就是最早出现的字符
        else:
            position[ch] = -1 #若字符出现第二次，则将其index改为-1
            while q and position[q[0][0]] == -1: #若队列的第一个字符的index 为 -1, 代表有重复，则推出队列
                q.popleft()
    return -1 if not q else q[0][1] #若队列中无数据，代表所有字符均有重复，否则返回队列第一个数据的index


print(firstUniqChar(s))

