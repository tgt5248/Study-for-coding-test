import heapq

def solution(scoville, K):
    count=0
    heapq.heapify(scoville) #힙으로 만들기
    while(True):
        if scoville[0]>=K:
            return count
        elif len(scoville)>=2:
            count+=1
            heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        else:    
            return -1

