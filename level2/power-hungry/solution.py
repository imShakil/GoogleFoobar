def school_multiplication(a, b):
    # multiply a with b
    # convert to list of digit
    num1 = [int(digit) for digit in a][::-1]
    num2 = [int(digit) for digit in b][::-1]
    
    # result with list of zeros
    result = [0] * (len(num1) + len(num2))
    
    # multiply each digit of num2 with num1
    for idx, d2 in enumerate(num2):
        carry = 0
        for jdx, d1 in enumerate(num1):
            product = d1 * d2 + carry + result[idx + jdx]
            carry = product // 10
            result[idx + jdx] = product % 10
        result[idx + len(num1)] = carry
        
    # print(result)
    # remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    result = result[::-1]
    return ''.join(str(digit) for digit in result)


def solution(xs):
    positive_array = []
    negative_array = []
        
    for num in xs:
        if num > 0:
            positive_array.append(num)
        if num < 0 :
            negative_array.append(num)            
    
    negative_array.sort()
    if len(negative_array) % 2:
        negative_array = negative_array[:len(negative_array)-1]
    negative_array = [num * (-1) for num in negative_array]
    positive_array.extend(negative_array)
    positive_array.sort(reverse=True)
    
    #print(positive_array)
    
    if len(xs) == 1:
        return str(xs[0])
    
    if len(positive_array) == 0:
        # print("0")
        return "0"
    
    result = str(positive_array[0])
    print(positive_array)
    for idx in range(1, len(positive_array)):
        if positive_array[idx] == 1:
            continue
        result = school_multiplication(str(positive_array[idx]), result)
    
    print(result)
    return result

input_array = [-1, -5, -6, -9, -14]
#print(input_array)
solution(input_array)

