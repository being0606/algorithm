def solution(brown, yellow): 
    
    TOTAL_CAFFET = brown+yellow
    
    weigh = 0
    hight = 0
    
    for i in range(TOTAL_CAFFET):
        flag = 0
        
        weigh = 3+i #4
        hight = int(TOTAL_CAFFET/weigh) #3
        
        if weigh<hight: # 조건체크
            continue
        
        if (weigh*hight == brown+yellow): # defalt check
            flag=flag+1
            
        if ( (weigh-2)*(hight-2) == yellow): # yellow check
            flag=flag+1
        
        if (weigh*2 + hight*2 - 4 == brown): # brown check
            flag=flag+1
            
        if (flag==3):
            break

        
    answer = [weigh,hight]
    
    return answer