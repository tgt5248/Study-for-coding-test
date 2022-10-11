citations=[0,0,0,0]
def solution(citations):
    if min(citations)>=len(citations): #[2,3] [5,6,7,8]
        return len(citations)
    elif max(citations)==0: #[0,0,0,0,0]
        return 0
    else: #[4,5,6,7,8,9] [1,3,6], [3,76,99,1000]
        citations.sort() 
        for i in range(len(citations)):
            if len(citations)-i<=citations[i] :
                return len(citations)-i
 
# len(citations)-i : i번째 값보다 더 많이 인용된 논문의 개수
# len(citations)-i<=citations[i] : 더 많이 인용된 개수가 해당 인덱스 값보다 작거나 같아지면 h가 될수없음? 
# 말로 표현을 못하겠네
# 문제 이해도 국어가 딸려서 힘들었음

solution(citations)