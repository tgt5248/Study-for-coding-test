# import heapq

"""
Case 1
1. 배열의 두번째 요소 기준으로 heap
=> 0초부터 시작하는거 계산을 못함
"""
# def solution(jobs):
#     list=[]
    
#     for i,j in jobs:
#         heapq.heappush(list,[j,i])
#     length = len(list)
#     start=0
#     end=list[0][1]
#     result=0
#     for i in range(length):
#         print(list)
#         start=-list[0][1]
#         end+=list[0][0]
#         print(f'start={start} end={end}')
#         result+=start+end
#         print(result)
#         heapq.heappop(list)
#     return result//length
# solution(jobs)

"""
Case 2
1. 테스트케이스 추가
2. 현재 가능한 작업중에서 작업시간 작은 순서대로
 """
 
# jobs=[ [3, 5], [8, 6],[7, 8]]
# jobs=[[10, 8], [3, 5], [9, 6]]
# jobs=[[0, 10], [4, 10], [15, 2], [5, 11]]
# jobs= [[0, 16], [0, 14], [15, 1], [13, 13]]
# jobs=[[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
# jobs= [[0,1], [0,2], [0,3], [0,4]]
# jobs=[[0,4],[0,3],[0,2],[0,1]]
jobs=[[0, 3], [1, 9], [2, 6]]


def solution(jobs): 
    #처음에는 요청시간 제일 작은거부터
    index=jobs.index(min(jobs))
    now=jobs[index][0] 
    wait=0
    length=len(jobs)
    
    while(len(jobs)>0):   
        index=jobs.index(min(jobs)) #반복문마다 인덱스 초기화
        temp=jobs[index]    # 최소값 변경

        # 현재 가능한 작업중에서 작업시간 작은거 찾기
        for i in range(len(jobs)):
            if jobs[i][0]<=now and jobs[i][1]<temp[1]:
                temp=jobs[i]
                index=i
                
        # 기다린시간, 현재시간 계산식 (노가다로 방법 구함)
        if jobs[index][0]>now: 
            wait+=+jobs[index][1]
            now=jobs[index][0]+jobs[index][1]
        else:
            wait+=now-jobs[index][0]+jobs[index][1]
            now+=jobs[index][1]

        del jobs[index] #이미 한 작업은 삭제
            
    return wait//length

solution(jobs)
# 처음에는 현재시간하고 가까운 작업으로 코드짰었는데 가능한것중에 작업시간이 짧은거부터 해야하는구나