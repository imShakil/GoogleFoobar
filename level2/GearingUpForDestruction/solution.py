import random

def solution(pegs):
    
    # set maximum possible radius for peg 1
    maximum = pegs[1] - pegs[0]
    
    # apply brute-force to find possible radius from 1 to maxmimum
    for s in range(1, maximum):
        GearSizes = [s]
        
        # determine all gear sizes
        for n in range(1, len(pegs)):
            GearSizes.append(pegs[n] - pegs[n-1] - GearSizes[-1])
        
        print(GearSizes)    
        if min(GearSizes) <= 0:
            continue
        if s == 2 * GearSizes[-1]:
            #print(x, gear_sizes)
            return [s, 1]

        if s+1 == 2 * GearSizes[-1]:
            #print(s, GearSizes)
            return [(s * 3) + 1, 3]
        if s+2 == 2 * GearSizes[-1]:
            #print(s, GearSizes)
            return [(s * 3) + 2, 3]

    return [-1, -1]

#print(solution([4, 30, 50]))
#print(solution([4, 17, 50]))
print(solution([4, 6, 8, 9, 10]))