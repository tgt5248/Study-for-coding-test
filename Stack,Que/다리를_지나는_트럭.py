def solution(bridge_length, weight, truck_weights):
    i=0 #시간
    onb=[] #다리 위 트럭
    while(True):
        i+=1
        if len(onb)==bridge_length: 
            onb.pop(0)
        if len(onb)<bridge_length:
            if sum(onb) + truck_weights[0] <= weight:
                onb.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                onb.append(0)
            if(len(truck_weights)==0): 
                return i+bridge_length
                #마지막 차 올라가면 다리 건널떄까지 여태 시간 + bridge_length만큼 시간 더 걸림