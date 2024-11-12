def solution(decimal):
    result = ''
    while decimal > 0:
        result = str(decimal % 2) + result
        decimal //= 2
    return result

# 보다 스택을 활용하는 방법이 명시적이고 표기 편하다
def solution(decimal):
    result = ''
    stack = []
    while decimal > 0:
        stack.append(str(decimal % 2))
        decimal //= 2
    while stack:
        result += stack.pop()
    return result