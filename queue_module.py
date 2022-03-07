import collections
q = collections.deque()

q.appendleft(10)
q.appendleft(11)
q.appendleft(12)

print(q)

q.pop()
print(q)

import queue
q = queue.Queue()

q.put(10)
q.put(30)
q.put(60)

print(q)

q.get()
q.get()
q.get()
q.get_wait()