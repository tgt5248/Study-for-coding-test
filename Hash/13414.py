"""Case 1
제한시간이 있기때문에 반복문에서 input() 사용 x
리스트보다 딕셔너리가 빠르다.
"""
# max,number=input( ).split()
# students=[]
# for i in range(int(number)):
#     s = input()
#     if s in students:
#         students.remove(s)
#     students.append(s)

# print(*students[:3],  sep='\n')

"""Case 2
sys.stdin.readline, 딕셔너리 사용
"""
import sys
max,number = map(int,sys.stdin.readline().split())
students=dict()
for i in range(number):
    students[sys.stdin.readline().strip()] = i  #같은 키라면 밸류값만 변경됨
sorted=sorted(students.items(),key=lambda x: x[1]) #밸류 기준으로 오름차순 정렬
for i in range(min(max,len(sorted))):   #출력개수 조절
    print(sorted[i][0])