'''
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
0 <= s.length <= 200
s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成
'''
# s = "    -91283472332"
# s = "42"
# s = "   -42"
# s = "4193 with words"
# s = "words and 987"
# s = "-91283472332"
s = "3.14159"
# s = "   -42"
# def myAtoi(s):
#     temp_list=[]
#     if s[0].isspace() or s[0].isdigit() or s[0] == '-':
#         for i in s:
#             if str(i).isdigit() or i =='-' or i =='.':
#                 temp_list.append(i)
#         if '.' in temp_list:
#             for i in temp_list:
#                 if i != '.':
#                     outcome = int(''.join(i))
#                 else:
#                     break
#         else:
#             outcome = int(''.join(temp_list))
#
#         if outcome >= - 2 ** 31:
#             if outcome <= 2 ** 31 - 1:
#                 return outcome
#             else:
#                 return 2 ** 31 -1
#         else:
#             return - 2 ** 31
#     else:
#         return 0
#
#
# print(myAtoi(s))
s = ""
def myAtoi(s):
    i = 0
    temp = []
    temp2 = []
    while i < len(s):
        if str(s[i]).isspace() and len(temp) == 0:
            i += 1
        else:
            temp.append(s[i])
            i += 1
    if len(temp) > 0:
        if temp[0]=='-' or temp[0] == '+' or temp[0].isdigit():
            temp2.append(temp[0])
            for i in range(1,len(temp)):
                if temp[i].isdigit():
                    temp2.append(temp[i])
                else:
                    break
        else:
            return 0
    else:
        return 0
    try:
        outcome = int(''.join(temp2))
    except: return 0

    if outcome <= - 2**31:
        return -2 ** 31
    elif outcome >= 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return outcome

print(myAtoi(s))

#官方答案
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)] #通过获取当前值来判断处于什么状态
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans
