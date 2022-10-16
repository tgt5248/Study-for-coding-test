brown=24
yellow=24

def solution(brown, yellow):
    s=[]
    sum=brown+yellow
    for i in range(1,sum//2):
        if (brown+yellow)%i ==0:
            s.append([i,sum//i])
    for y,x in s:
        if x>=3 and y>=3 and yellow==(x-2)*(y-2) :
            return [x,y]


solution(brown,yellow)
