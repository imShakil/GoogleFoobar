def solution(i):
    primes = "2"
    n = 21000
    for num in range(3, n, 2):
        itr = 2
        add = True
        while itr * itr <= num:
            if num % itr == 0:
                add = False
                break
            itr += 1
        if add:
            primes += str(num)
        
        if len(primes) >= i+5:
            print(num)
            break
    return primes[i:i+5]

print(solution(3))
