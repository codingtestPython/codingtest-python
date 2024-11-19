def solution(arr):
    sum_arr = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum_arr.append(arr[i] + arr[j])

    return sorted(set(sum_arr))

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))