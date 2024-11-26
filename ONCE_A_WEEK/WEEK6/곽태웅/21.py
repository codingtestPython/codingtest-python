from collections import Counter

def solution(want, number, discount):
    answer = 0
    counter = Counter(dict(zip(want, number)))

    for i in range(0, len(discount) - 9):
        sliced_counter = Counter(discount[i:i+10])
        if all(sliced_counter[j] >= counter[j] for j in counter):
            answer += 1
    return answer

# 접근한 방식
# Counter를 이용해 비교하면 원하는 만큼의 상품을 살 수 있는지 개수를 비교할 수 있다

# 시행착오, 10일이라는 조건을 포함하지 않았었다
# 회원권의 기한은 10일임으로 리스트를 슬라이스해서 사용해야 함