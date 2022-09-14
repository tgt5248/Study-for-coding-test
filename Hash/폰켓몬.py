def solution(nums):
    new=list(set(nums)) #중복제거
    if len(new)>=len(nums)/2:
        answer=len(nums)/2
    else: 
        answer=len(new) 
    return answer

# if문 말고 min()으로 간결하게