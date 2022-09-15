""" Case1
1. 정렬
2. 2중 for 문으로 접두어 확인
=> 효율떨어짐
"""
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(0,len(phone_book)-1):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[j][0:len(phone_book[i])] == phone_book[i]:
#                 answer = False
#                 return answer
#             else:
#                 answer = True
#     return answer
#

"""
Case2
1. 정렬하고 첫번째 전화번호 길이를 구함
2. 모든 리스트안에 값들 앞에서부터 그 길이만큼만  
3. 중복제거
4. 길이비교
=> ["123","1455","145982"] 안됨
"""
# def solution(phone_book):
#     phone_book.sort()
#     new_list=[]
#     for i in phone_book:
#         new_list.append(i[0:len(phone_book[0])])
#     if len(new_list)!=len(set(new_list)):
#         return False
#     else:
#         return True
    
"""
Case 3
1. 정렬
2. 
"""
def solution(phone_book):
    phone_book.sort()
    return True
