import queue
q = queue.PriorityQueue() # this module put and get value in queue but it remove(get) element based on priority (priority based on element ie) lowest value is highest priority)

q.put(40)
q.put(10)
q.put(1)
print(q)

q.get()
q.get()
q.get()
