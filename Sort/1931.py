import sys

n=int(sys.stdin.readline().strip())
info=[]
for i in range(n):
    info.append(list(map(int,sys.stdin.readline().strip().split(" "))))
info.sort(key=lambda x:(x[1],x[0]))

count=1
end=info[0][1]
for i,j in info[1:]:
    if i>=end:
        count+=1
        end=j
        
print(count)