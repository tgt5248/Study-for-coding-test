prices =[1, 2, 3, 2, 3]	
def solution(prices):
    ori=prices #원본
    list=[]
    while(prices):
        a=prices[0]
        count=0
        for i in range(1,len(prices)):
            count+=1
            if(a>prices[i]):
                break
        list.append(count)
        prices.pop(0)
    list=[]
    for i in range(len(prices)-1):
        count=0
        for j in range(i+1,len(prices)):
            count+=1
            if prices[i]>prices[j]:
                break
        list.append(count)
    
    print(list) 
solution(prices)