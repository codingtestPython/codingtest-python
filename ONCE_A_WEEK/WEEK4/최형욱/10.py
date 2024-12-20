def solution(value):
  answer = 0
  n = len(value)
  for i in range(n):
    stack = []

    for j in range(n):
      c = value[(i + j) % n]
      if c == "(" or c == "[" or c == "{":
        stack.append(c)
      else:
        if not stack:
          break
      
        if c == ")" and stack[-1] == "(":
          stack.pop( ) 
        elif c == "]" and stack[-1] == "[":
          stack.pop( ) 
        elif c == "}" and stack[-1] == "{":
          stack.pop( ) 
        else:
          break
    else:
      if not stack:
        answer += 1

  return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))