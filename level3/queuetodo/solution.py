
def calXOR(n):
    mod = [n, 1, n+1, 0]
    if n < 0:
        return 0
    return mod[n%4]

def solution(start, length):
    xor_sum = 0
    for id in range(length):
        nw = start + (length * id)
        xor_sum ^= (calXOR(nw-1)^calXOR(nw+length-id-1))
    return xor_sum

print(solution(0, 3))
