def solution(num):
    trial=0
    TARGET = 1
    while(1):
        if num==1:
            break
        trial += 1
            
        if num%2==0:
            num = num/2
        else:
            num = 3*num+1
            
        if (num==TARGET):
            break
            
        if (trial==500):
            trial=-1
            break
        
        
        
    answer = trial

    return answer