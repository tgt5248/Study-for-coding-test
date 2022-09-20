"""Case 1
1. out 벨류가 in 벨류보다 작으면 추월했다라고 가정
=> 반례 :in=[abcd], out=[dacb]
"""
# import sys

# number = int(sys.stdin.readline())
# in_list={}
# out_list={}
# for i in range(number):
#     in_list[(sys.stdin.readline().strip())]=i
# for i in range(number):
#     out_list[(sys.stdin.readline().strip())]=i

# count=0
# for i in out_list.keys():
#     if out_list[i]<in_list[i]:
#         count+=1

# print(count)        

"""
Case 2
1. out 벨류리스트에서 i번째 이후 벨류에서 i번째 벨류보다 작은게 하나라도 있다면 추월
=> i번쨰 이후 벨류중 최소값과 i번째 벨류를 비교
"""
import sys

number = int(sys.stdin.readline())
in_list={}
out_list={}
for i in range(number):
    in_list[(sys.stdin.readline().strip())]=i
for i in range(number):
    out_list[(sys.stdin.readline().strip())]=i

for i in out_list: #out순서대로 in에 해당하는 인덱스 부여 
    out_list[i]=in_list[i]
out=(list(out_list.values()))

#결과
count=0
for i in range(len(out)): 
    if i!=len(out)-1 and out[i] > min(out[i+1:]):
        count+=1

print(count)
