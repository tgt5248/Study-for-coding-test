def solution(sizes):
    sizes=[[y,x] if x<y else [x,y] for x,y in sizes]
    return max(sizes)[0]*max(sizes,key=lambda x:x[1])[1]