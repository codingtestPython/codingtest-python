import math

def solution(progresses, speeds):
  answer = [ ]
  n = len(progresses)
  days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

  count = 0
  max_day = days_left[0] 

  for i in range(n):
    if days_left[i] <= max_day:
      count += 1
    else:
      answer.append(count)
      count = 1
      max_day = days_left[i]

  answer.append(count)

  return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))