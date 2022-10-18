
from itertools import permutations

def solution(numbers):
    result=0
    cset=set()
    for i in range(1,len(numbers)+1): #조합개수
        for n in permutations(numbers,i): #모든 조합 구하기
            cset.add(int(''.join(list(n)))) #중복제거
    for num in cset: #숫자마다
        count=-1 #디폴트 -1
        if num>1: #0,1은 패스
            count+=1  #2일경우에
            for j in range(2,num//2+1): #시간초과떠서 전체 다 비교안하고 중간정도까지
                if num%j==0: #소수인지 체크
                    count+=1  
                    break
            if count==0:    #소수일경우
                result+=1
    return result