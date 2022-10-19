import itertools

def solution(word):
    a=["A","E","I","O","U"]
    s=[]
    for i in range(1,6):
        s+=[''.join(list(n)) for n in itertools.product(a,repeat=i)]
    return sorted(s).index(word)+1 