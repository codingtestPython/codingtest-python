def solution(progresses, speeds):
    days = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]
    
    answer = []
    current_release = days[0]
    count = 0
    
    for day in days:
        if day <= current_release:
            count += 1
        else:
            answer.append(count)
            current_release = day
            count = 1
    
    answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))