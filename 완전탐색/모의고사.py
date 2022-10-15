answers=[1,3,2,4,2]
answers=[1,2,3,4,5]
def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[1]
    count=[0,0,0]
    for i in range(len(answers)):
        if answers[i]==p1[i%len(p1) if i>=len(p1) else i]:
            count[0]+=1
        if answers[i]==p2[i%len(p2) if i>len(p2) else i]:
            count[1]+=1
        if answers[i]==p3[i%len(p3) if i>len(p3) else i]:
            count[2]+=1
    answer=[]
    for i,v in enumerate(count):
        if v==max(count):
            answer.append(i+1)

    return answer

