import sys
import heapq

heap=[]

for i in range(int(sys.stdin.readline())):
    for j in list(map(int,sys.stdin.readline().strip().split(" "))):
        if i==0:
            heapq.heappush(heap,j)
        else:
            heapq.heappushpop(heap,j)
print(heap[0])
