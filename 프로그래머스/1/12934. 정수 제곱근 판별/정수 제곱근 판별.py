def solution(n):
    TARGET = n
    
    if n==1:
        return (n+1)*(n+1)
    elif n==2:
        return -1
    elif n==3:
        return -1
    for i in range(TARGET):
        muti = i*i
        if TARGET==muti:
            return (i+1) * (i+1)
        elif TARGET<muti:
            return -1
    return 


