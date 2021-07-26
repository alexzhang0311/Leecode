'''
给定一个化学式formula（作为字符串），返回每种原子的数量。
原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
'''

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack, dic = [], {} # (K, 4, 0)
        i, flag = 0, 0
        while i < n:
            if formula[i].isupper():    # 情况一 大写字母
                atom, atom_multi = '', 0
                atom += formula[i]
                i += 1
                while i < n and formula[i].islower():   # 找小写字母 组成atom
                    atom += formula[i]
                    i += 1
                while i < n and formula[i].isdigit():   # 找数字
                    atom_multi = 10  * atom_multi + int(formula[i])
                    i += 1
                atom_multi = 1 if atom_multi == 0 else atom_multi
                stack.append([atom, atom_multi, flag])
            elif formula[i] == '(':      # 情况二 左括号
                flag += 1
                i += 1
            elif  formula[i] == ')':     # 情况三 右括号
                brac_multi = 0
                i += 1
                while i < n and formula[i].isdigit():  # 找数字
                    brac_multi = 10 * brac_multi + int(formula[i])
                    i += 1
                brac_multi = 1 if brac_multi == 0 else brac_multi
                end = len(stack)
                while stack and stack[end - 1][2] == flag: # 找到这个括号里的atom 相乘
                    stack[end - 1][1] *= brac_multi
                    stack[end - 1][2] -= 1
                    end -= 1
                flag -= 1
        for atom in stack:
            dic[atom[0]] = dic.get(atom[0], 0) + atom[1]
        dic = sorted(dic.items(), key = lambda obj: obj[0])
        ans = ''
        for atom, multi in dic:
            multi = '' if multi == 1 else multi
            ans += atom + str(multi)
        return ans