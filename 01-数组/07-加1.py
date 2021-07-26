def plusOne(digits):
    a = '0'
    for i in digits:
        a += str(i)
    return [int(j) for j in str(int(a) + 1)]