string = input()
set=set()
for i in range(len(string)): # 한번에 비교할 개수
    for j in range(len(string)-i): #시작부분
        set.add(string[j:j+i+1])
        
print(len(set))
#이중포문이라 효율떨어지는거같음
# #처음부터 set으로 만들어서 넣으면 좀 더 줄일 수 있을듯