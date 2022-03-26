# min and max Binary heap tree
# 1) min binary heap tree
# 2) max binary heap tree

# purpose 
# 1) To implement priority queue
# 2) In heap sort algorithm
# 3) To find Kth largest or smallest element in list of number 

# using heapq module
import heapq

heap = []

heapq.heappush(heap,100)
heapq.heappush(heap,50)
heapq.heappush(heap,60)
heapq.heappush(heap,55)
heapq.heappush(heap,90)
print(heap)