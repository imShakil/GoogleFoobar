def solution(x, y):
    a = int(x)
    b = int(y)

    total_cycles = 0

    while min(a, b) > 1:
        a, b = min(a, b), max(a, b)
        if b % a == 0:
            return str("impossible")
        elif a%2 == 0 and b%2 == 0:
            return str("impossible")
        else:
            total_cycles += (b//a)
            b %= a
            
    total_cycles += abs(a-b)
    return str(total_cycles)


#print(solution('1', '1'))
#print(solution('3', '2'))
#print(solution('4', '3'))
#print(solution('5', '4'))
#print(solution('1', '10'))
#print(solution('3', '3'))
#print(solution('10', '8'))
#print(solution('10', '5'))
