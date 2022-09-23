def solution(arr):
    result=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i]!=result[len(result)-1]: #result[-1]
            result.append(arr[i])
    return result

# list[-1] : 리스트 마지막 요소 출력