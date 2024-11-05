def solution(numbers):
    result_list = []
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            k = i + j
            if k not in result_list:
                result_list.append(k)
    result_list.sort()
    return result_list