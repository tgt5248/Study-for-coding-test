import itertools

k= 80
dungeons=[[80,20],[50,40],[30,10]]	
def solution(k, dungeons):
    max=0
    all=itertools.permutations([i for i in range(len(dungeons))],len(dungeons))
    for n in all:
        now=k
        count=0
        for j in n:
            if now>=dungeons[j][0]:
                now-=dungeons[j][1]
                count+=1
                if max<count:
                    max=count
    print(max)
    
    # count=0
    # max=0
    # if k>[0]:
    #     # continue
    #     print(1)
    # else:
    #     k-[1]
    #     count+=1
    # if max<count:
    #     max=count   
    answer = -1
    return answer

solution(k,dungeons)
