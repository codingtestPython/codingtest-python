def solution(arr):
    return sorted(set(arr), reverse = True)

print(solution([4, 2, 2, 1, 3, 4]))
print(solution([2, 1, 1, 3, 2, 5, 4]))