def solution(genres, plays):
    
    #장르별 총합 구하기
    sum = dict()
    for i in range(len(genres)): 
        if genres[i] in sum:
            sum[genres[i]]=sum[genres[i]]+plays[i]
        else:
            sum[genres[i]]=plays[i]
    sum=dict(sorted(sum.items(),key=lambda x:-x[1])) #내림차순

    album=list(zip(list(range(len(genres))),genres,plays)) # i, genres, plays 순서대로 리스트 생성
    album=sorted(album,key=lambda x:(-sum[x[1]],-x[2])) #총합 내림차순, plays 내림차순

    #결과
    result=[]
    for i in range(len(album)):
        print(i)
        if (i>1 and (album[i][1] == album[i-1][1] == album[i-2][1])):
            continue
        else:
            result.append(album[i][0])
    return result