"""Case 1
nsmallest 사용
=> 시간초과
""" 
# import sys
# import heapq
# import math

# n = int(sys.stdin.readline())
# heap=[]
# for i in range(1,n+1):
#     heapq.heappush(heap,int(sys.stdin.readline()))
#     print(heapq.nsmallest(math.ceil(i/2),heap)[-1])

"""
Case 2 
중앙값 직접 구하기
=> 시간초과
"""
    
# from statistics import median
# import sys
# import heapq

# n = int(sys.stdin.readline())
# heap=[]
# for i in range(1,n+1):
#     heapq.heappush(heap,int(sys.stdin.readline()))
#     if i%2 == 1:
#         print(median(heap))
#     else:
#         sort=sorted(heap)
#         print(sort[len(sort)//2 -1])


"""
Case 3
pop사용
=> 시간초과..
"""
    
# import sys
# import heapq

# n = int(sys.stdin.readline())
# heap=[]
# for i in range(n):
#     heapq.heappush(heap,int(sys.stdin.readline()))
#     list=heap.copy()
#     for j in range(i//2): 
#         heapq.heappop(list)
#     print(list[0])


"""
Case 4
pop사용
=> 원본 유지해야할듯
=> 반례 : 3 2 4 1 5 
"""
    
# import sys
# import heapq

# n = int(sys.stdin.readline())
# heap=[]
# for i in range(n):
#     heapq.heappush(heap,int(sys.stdin.readline()))
#     if i!=0 and i%2==0:
#         heapq.heappop(heap)
#     print(heap)

"""
Case 5

"""
    
import sys
import heapq

n = int(sys.stdin.readline())
heap=[]
for i in range(n):
    heapq.heappush(heap,int(sys.stdin.readline()))
