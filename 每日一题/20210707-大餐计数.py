'''
大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 任意 两道餐品做一顿大餐。

给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i​​​​​​​​​​​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。结果需要对 109 + 7 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。
输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
'''


deliciousness = [1,1,1,3,3,3,7]
print(deliciousness)
# def countPairs(deliciousness):
#     big_meal = []
#     for i_key, i in enumerate(deliciousness):
#         for j_key, j in enumerate(deliciousness):
#             temp_foods = []
#             if i_key != j_key:
#                 if i+j > 0:
#                     if (i+j) & (i+j-1) == 0:
#                         temp_foods.append(i)
#                         temp_foods.append(j)
#             if len(temp_foods) > 0:
#                 big_meal.append(sorted(temp_foods))
#     count = len(big_meal)/2
#     return count

# print("%.0f" % countPairs(deliciousness))
# a = 0
# for i in range(len(deliciousness)):
#     print(i)
#     for i in range(a+1,len(deliciousness)):
#         print(i)
#     a +=1
#     print(2 * "----------")
#
# def countPairs(deliciousness):
#     flag = 0
#     count = 0
#     outcome = []
#     for i in range(len(deliciousness)):
#         for j in range(flag+1,len(deliciousness)):
#             temp = []
#             cal = deliciousness[i] + deliciousness[j]
#             if cal > 0 and cal & (cal-1) == 0:
#                 temp.append(deliciousness[i])
#                 temp.append(deliciousness[j])
#                 count += 1
#             if len(temp) > 0:
#                 outcome.append(temp)
#         flag += 1
#     return count
# # print("%.0f" % countPairs(deliciousness))
#
# print(countPairs(deliciousness))


# def countPairs(deliciousness):
#     flag = 0
#     count = 0
#     deliciousness = sorted(deliciousness)
#     for i in range(len(deliciousness)):
#         for j in range(flag+1,len(deliciousness)):
#             cal = deliciousness[i] + deliciousness[j]
#             if cal > 0 and cal & (cal-1) == 0:
#                 count += 1
#         flag += 1
#     return count
# # print("%.0f" % countPairs(deliciousness))
#
# print(countPairs(deliciousness))



from collections import Counter
class Solution:
    mod = 10 ** 9 + 7
    maximum = 1 << 21
    def countPairs(self, deliciousness):
        hashmap = Counter(deliciousness)
        ans = 0
        for x in hashmap:
            i = 1  #i 为2的幂
            while i <= self.maximum:
                t = i - x # x+t = 2的幂
                if t in hashmap:
                    if t == x: # 相同数n*n-1
                        ans += (hashmap[x] - 1) * hashmap[x]
                    else:
                        ans += hashmap[x] * hashmap[t]
                i <<= 1
        ans >>= 1 #等同于ans / 2,因（1,7）（7,1）重复计算因此除以2
        return ans % self.mod