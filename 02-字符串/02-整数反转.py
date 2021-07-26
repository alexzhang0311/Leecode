'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

输入：x = 123
输出：321
'''

x = 0
def reverse(x):
    temp = [i for i in str(x)]
    if temp[0] == '-':
        for i in range(0, (len(temp)) // 2):
            temp[i], temp[len(temp) - i - 1] = temp[len(temp) - 1 - i], temp[i]
        temp.pop()
        outcome = -int(''.join(temp))
        if outcome < -(2 ** 31):
            return 0
        else:
            return outcome
    else:
        for i in range(0, (len(temp)) // 2):
            temp[i], temp[len(temp) - i - 1] = temp[len(temp) - 1 - i], temp[i]
        outcome = int(''.join(temp))
        if outcome > (2 ** 31) - 1:
            return 0
        else:
            return outcome

print(reverse(x))


###官解，数学方法：
def reverse(x):
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
    rev = 0
    while x != 0:
        # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
        if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
            return 0
        digit = x % 10
        # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
        if x < 0 and digit > 0:
            digit -= 10

        # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
        x = (x - digit) // 10
        rev = rev * 10 + digit

