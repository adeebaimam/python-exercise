# Count distinct ways of climbing from 0th stair to nth stair if a child can either take 1 step or 2 step.


def climb(n):    #here n is the number of stairs
    if n<0:
        return 0     # here if stair is less than n numbers of stairs it doesnt mean any sense so it returns 0
    if n==0:
        return 1     #if child climbs on same stair which he was on befor or from where he has to start then no climbing is possible at remains on same place where he was 
    else:
        return climb(n-1) + climb(n-2)    #here (n-1) is the stair just before the last stair and (n-2) is the stair 2 stepd before the last stair
climb(3)
