# 요세푸스 문제
from collections import deque

# 첫번째 구현
def solution(n, k):
    q = deque([i for i in range(1, n+1)])
    l = []
    i = 0
    while len(q) != 0:
        i += 1
        e = q.popleft()
        if i % k == 0:
            l.append(e)
        else:
            q.append(e)
    return l

# deque의 rotate 메소드를 사용하면 훨씬 간단하다.
# 파이썬에서는 리스트가 비면 falsy로 처리하기 때문에 len()을 통해 q의 길이를 구할 필요가 없다.
def solution(n, k):
    q = deque([i for i in range(1, n+1)])
    l = []
    
    while q:
        q.rotate(-(k - 1))
        l.append(q.popleft())
    
    return l