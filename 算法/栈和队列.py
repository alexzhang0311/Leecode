#双向队列

import collections

q = collections.deque([1,2,3,4,5])

q.pop() #右边弹出
q.popleft() #左边弹出
q.rotate(1) #顺时针旋转
q.rotate(-1) #逆时针旋转

q.extend([1]) #右边插入
q.extendleft([1]) #左边插入

