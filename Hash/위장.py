"""
ex) {모자:3개, 상의:2개, 하의:2개}
    = (3c0+3c1) x (2c0+2c1) x (2c0+2c1) -1
    = (1+3) x (1+2) x (1+2) -1
    따라서 종류별 개수+1개를 리스트에 저장
"""
from math import prod
def solution(clothes):
    dic={}
    for key, value in clothes:
        if value in dic:
            dic[value]+=1
        else:
            dic[value]=2 #디폴트부터 개수+1
    return prod[list(dic.values())]-1 #리스트내 모든 원소를 곱함

# python 3.8부터 math의 prod 사용가능
# 계산방법.. 생각해내기 어려워서 고민하다가 태용이 코드 참조...

# 나중에 종류별로 1씩 더하는 방법
# def solution(clothes):
#     dic={}
#     for key, value in clothes:
#         if value in dic:
#             dic[value]+=1
#         else:
#             dic[value]=1
#     return prod([x+y for x,y in zip(list(dic.values()),len(dic.values())*[1])])-1