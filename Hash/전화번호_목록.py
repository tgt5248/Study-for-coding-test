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
1. 정렬 (string으로 된 숫자는 정수의 오름차순 정렬이 아님)
    ex) 1, 12, 125, 14, 2, ...
2. i번째와 i번째 길이만큼의 i+1번째가 같은지 확인하면 접두어 확인 가능
"""
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True


#내장함수 str.startsWith(searchString[, position]) : 어떤 문자열이 특정 문자로 시작하는지 확인하여 결과를 true 혹은 false로 반환.
# from itertools import combinations : for(a,b) in combinations(리스트,2) 리스트에서 2개씩 모든 조합을 구하기