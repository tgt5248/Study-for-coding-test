def solution(priorities, location):
    count=1 #빠져나오는 순서
    a=list(zip(priorities,list(range(len(priorities)))))
    while(len(a)>1):
        if a[0][0] >= max(a[1:])[0]:
            if a[0][1] == location:
                return count                 
            a.pop(0)
            count+=1
        else:
            a.append(a[0])
            a.pop(0)
    return count