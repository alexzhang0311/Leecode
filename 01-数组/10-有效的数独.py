# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board=[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

#时间复杂度O(N^2) 空间复杂度O(N)
#思路：行中有无重复，列中有无重复，3*3中有无重复

def isValidSudoku(board):
    for i in board: #row 判断
        temp = []
        for j in i:
            if j != '.':
                temp.append(j)
        if len(set(temp)) != len(temp):
            return False

    for i in range(9): #column 判断
        temp_list = []
        for j in range(9):
            temp_list.append(board[j][i])
        temp = []
        for j in temp_list:
            if j != '.':
                temp.append(j)
        if len(set(temp)) != len(temp):
            return False

    for column in range(0, 9, 3):  # 3 * 3判断
        for row in range(0, 9, 3):
            temp_list = []
            i = column
            while i < column + 3:
                j = row
                while j < row + 3:
                    temp_list.append(board[i][j])
                    j += 1
                i += 1
            temp = []
            for j in temp_list:
                if j != '.':
                    temp.append(j)
            if len(set(temp)) != len(temp):
                return False
    return True



print(isValidSudoku(board))


#官方答案 一次迭代 + 哈希表记录
#枚举 3*3 的子数独 box_index = (row // 3) * 3 + columns // 3

def isValidSudoku(board):
    hashmap_row = [{} for i in range(len(board))]
    hashmap_column = [{} for i in range(len(board))]
    hashmap_box_index = [{} for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            values = board[i][j]
            box_index = (i // 3) * 3 + j // 3
            if values != '.' and values in hashmap_row[i]:
                return False
            else:
                hashmap_row[i][values] = 1
            if values != '.' and values in hashmap_column[j]:
                return False
            else:
                hashmap_column[j][values] = 1
            if values != '.' and values in hashmap_box_index[box_index]:
                return False
            else:
                hashmap_box_index[box_index][values] = 1

    return True


print(isValidSudoku(board))


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # init data
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    # validate a board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                num = int(num)
                box_index = (i // 3) * 3 + j // 3

                # keep the current cell value
                rows[i][num] = rows[i].get(num, 0) + 1 # dict.get(key, default=None)
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                # check if this value has been already seen before
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True

print(isValidSudoku(board))
