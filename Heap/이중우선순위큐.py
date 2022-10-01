import heapq
 
def solution(operations):
    heap=[]
    for i in operations:
        if i[0]=="I":
            heapq.heappush(heap,int(i[2:]))
        elif len(heap)!=0:
            if i[2]=="-":
                heapq.heappop(heap)
            else:
                heap.remove(heapq.nlargest(1,heap)[-1])
                heapq.heapify(heap)
        
    if len(heap)>=2:
        return [heapq.nlargest(1,heap)[-1],heap[0]]
    else:
        return [0,0]
