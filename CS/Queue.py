# # list
# queue=[4,5,6]
# queue.insert(0,5)
# queue.insert(0,7)
# # >> queue=[4,5,6,5,7]
# print(queue)
# queue.pop()
# queue.pop()
# # >> queue=[6,5,7]
# print(queue)

#deque
from collections import deque

queue=deque([4,5,6])
queue.append(5)
queue.append(7)
# >> queue=[4,5,6,5,7]
queue.popleft()
queue.popleft()
# >> queue=[6,5,7]