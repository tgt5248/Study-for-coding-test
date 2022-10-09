
numbers=[998,997,99] 
def solution(numbers):
    result=''
    new=sorted([str(x)*3 for x in numbers], reverse=True)
    for i in new:
        result+=i[:len(i)//3]
    return print(str(int(result)))
solution(numbers)

# 원소가 1000까지니까 숫자 3번씩 반복해서 비교하면 더 큰거 알수있음 
# ex) '553' '55' => '553553553' < '555555'  => 55553