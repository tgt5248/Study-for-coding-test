def solution(participant, completion):

    par=sorted(participant)
    com=sorted(completion)
    
    for i in range(0,len(com)):
        if par[i] != com[i]:
            answer=par[i]
            break
        answer=par[i+1]
    return answer
  
solution
