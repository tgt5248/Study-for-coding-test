import heapq
import sys

n,m =  map(int,sys.stdin.readline().split())
heap=[]
[heapq.heappush(heap,x) for x in map(int,sys.stdin.readline().split())]

for i in range(m):
    new=heapq.heappop(heap)+heapq.heappop(heap)
    for i in range(2):
        heapq.heappush(heap,new)

print(sum(heap))

# n개만큼 입력받는거는 못했음
