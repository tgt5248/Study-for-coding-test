import math

def solution(progresses, speeds):
    list=[100]*len(progresses)
    # 100에서 progresses 뺀 값을 speeds로 나눠서 올림
    a=[math.ceil((x-y)/z) for x,y,z in zip(list,progresses,speeds)] 
    count=1
    b=[]
    while(len(a)>1):
        if a[0]>=a[1]:
            count+=1
            a.pop(1)
        else:
            a.pop(0)
            b.append(count)
            count=1
    b.append(count)
    return b