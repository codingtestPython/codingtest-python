def solution(number):
    stack = []

    while number > 0:
        remainder = number % 2
        stack.append(str(remainder))
        number //= 2

    stack.reverse()

    return ''.join(stack)
    
    
print(solution(10))
print(solution(27))
print(solution(12345))