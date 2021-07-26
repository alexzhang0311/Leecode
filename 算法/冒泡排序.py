def bubblesort(num):
    for i in range(1,len(num)): #N个数，循环N-1次
        for j in range(0,len(num)-i): #每次循环结束，最后一位数为该次循环的最大数
            if num[j] > num[j + 1]:
                num[j],num[j+1] = num[j+1],num[j]
    return num

num=[4,3,2,1]

# print(bubblesort(num))



i = 0
while i < len(num)-1:
    j = i
    while j < len(num):
        if num[i] > num[j]:
            num[i],num[j] = num[j],num[i]
        j += 1
    i += 1

print(num)