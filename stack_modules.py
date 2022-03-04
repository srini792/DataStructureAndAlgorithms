# stack is implemented using collection and queue.LifoQueue() modules

import collections 
stack_deque = collections.deque()

stack_deque.append(10)
stack_deque.append(20)
stack_deque.append(30)
print(stack_deque)
#----------------------------------------
# pop from stack_deque
stack_deque.pop()
stack_deque.pop()
print(stack_deque)
print(stack_deque[-1])
stack_deque.pop()
stack_deque.pop()

#-------------------------------------------------
# push operation in queue.LifoQueue() push - put(), pop - get()
import queue
stack = queue.LifoQueue()
stack.put(10)
#----- pop operation
print(stack.get())
print(stack.get(timeout=1))