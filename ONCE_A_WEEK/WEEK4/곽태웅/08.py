def solution(s):
    open_count = s.count('(')
    close_count = s.count(')')
    if open_count == close_count:
        return True
    else:
        return False
    
def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return not stack