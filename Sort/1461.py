import sys
import math

n,m= map(int,sys.stdin.readline().split(" "))

minus=[]
plus=[]
for i in list(map(int,sys.stdin.readline().split(" "))):
    if i<0:
        minus.append(-i)
    else:
        plus.append(i)
        
result=0

if len(plus)!=0:
    plus.sort(reverse=True)
    for i in range(max(math.ceil(len(plus)/m),1)):
        result+=plus[i*m]*2

if len(minus)!=0:
    minus.sort(reverse=True)
    for i in range(max(math.ceil(len(minus)/m),1)):
        result+=minus[i*m]*2

result-=max(max(minus,plus))

print(result)

# 음수, 양수 나눠서
# 왕복 계산하고 마지막 가장큰거 빼기 (다시 안돌아와도됨)
# 더러운 나의 코드 
