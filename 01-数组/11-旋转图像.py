'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix)
j=0
outcome = []
while j < len(matrix[0]):
    temp = []
    for i in matrix[::-1]:
        temp.append(i[j])
    j += 1
    outcome.append(temp)

print(outcome)

#时间复杂度O(n^2),空间复杂度O(n)
# def rotate(matrix):
#     hashmap = {}
#     column = 0
#     while column < len(matrix[0]):
#         row = 0
#         while row < len(matrix):
#             value = matrix[::-1][row][column]
#             location = str(column) + str(row) #若column & row 为双位数，则会出问题
#             hashmap[value] = location #若value相同，location会被刷新
#             row += 1
#         column += 1
#     print(hashmap)
#     for value in hashmap:
#         location = hashmap[value]
#         matrix[int(location[0])][int(location[1])] = value
#     return matrix
#
# print(rotate(matrix))


# def rotate(matrix):
#     hashmap = {}
#     column = 0
#     while column < len(matrix[0]):
#         row = 0
#         while row < len(matrix):
#             value = matrix[::-1][row][column]
#             location = str(column) + '|' + str(row)
#             hashmap[location] = value
#             row += 1
#         column += 1
#     for location in hashmap:
#         value = hashmap[location]
#         matrix[int(location.split('|')[0])][int(location.split('|')[1])] = value
#     return matrix
#
# print(rotate(matrix))


#提示：
'''
瞬时间旋转：

matrix[i][j] = matrix[len(matrix)-j-1][i]

逆时针旋转:

matrix[len(matrix)-j-1][i] = matrix[i][j]

沿对角线折叠：
matrix[i][j] = matrix[j][i]

沿中线对折 横：
matrix[i][j] == matrix[len(matrix)-1-i][j]

沿中线对折 竖：
matrix[i][j] == matrix[i][len(matrix)-1-j]

'''

# for i in range(len(matrix)):
#     for j in range(len(matrix)-1):
#         matrix[i][j] = matrix[len(matrix)-1-j][i] #00 = 30 01 = 20 02 = 10 03 = temp



########官方答案###########
#解法1：使用辅助数组。 时间复杂度O（N^2） 空间复杂度O（N^2）
# class Solution:
#     def rotate(self, matrix):
#         n = len(matrix)
#         # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝 更改matrix_new 会使得matrix的值发生变化
#         matrix_new = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 matrix_new[j][n - i - 1] = matrix[i][j]
#         # 不能写成 matrix = matrix_new
#         matrix[:] = matrix_new
#         return matrix
#
# print(Solution.rotate(self=Solution,matrix=matrix))

#解法2: 原地旋转.时间复杂度：O(N^2) 空间复杂度：O(1)

# class Solution:
#     def rotate(self, matrix):
#         n = len(matrix)
#         for i in range(n // 2):
#             for j in range((n + 1) // 2):
#                 matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
#                     = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
#         return matrix
#
# print(Solution.rotate(self=Solution,matrix=matrix))


#解法3: 用翻转代替旋转,时间复杂度：O(N^2) 空间复杂度：O(1)

class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

print(Solution.rotate(self=Solution,matrix=matrix))
