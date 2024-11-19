def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    result = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(r2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
        

    return result

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
