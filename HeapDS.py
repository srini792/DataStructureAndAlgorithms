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


heap1 = [100,99,98,97]

#heappop
heapq.heapify(heap1)
heapq.heappop(heap1)
print(heap1)

#pusppop
heap2 = [100,98,99,101]
heapq.heapify(heap2)
print(heapq.heappushpop(heap2,102))
print(heap2)

#heapq.nsmallest
heap3 = [5,4,3,2,1]
heapq.heapify(heap3)
print(heapq.nsmallest(2,heap3))

#heapq.nlargest
heap4 = [5,4,3,2,1]
heapq.heapify(heap4)
print(heapq.nlargest(2,heap4))


#priority queue
pq = [(100,"srinivas"),(1,"tvl")]
heapq.heapify(pq)
print(pq)
print(heapq.heappop(pq))
print(pq)

