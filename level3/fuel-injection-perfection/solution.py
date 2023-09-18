def opt_solution(n):
    steps = 0
    while n > 1:
        steps += 1
        # edge case
        if n == 3:
            n -= 1
        elif n%2 == 0:
            n //= 2
        elif n%4 == 3:
            n += 1
        else:
            n -= 1
    return steps

def solution(n):
    n = int(n)
    return opt_solution(n)
    # Your code here
