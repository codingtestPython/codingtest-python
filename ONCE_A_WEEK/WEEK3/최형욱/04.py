def solution(arr):
    math_poors = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0]*3

    for i, a in enumerate(arr):
        for j, math_poor in enumerate(math_poors):
            if a == math_poor[i % len(math_poor)]:
                scores[j] += 1

    max_score = max(scores)

    high_scores = []

    for i, score in enumerate(scores):
        if score == max_score:
            high_scores.append(i+1)
    
    return high_scores

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))