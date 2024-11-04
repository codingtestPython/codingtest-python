# Python cheatsheet

## Useful grammar

### List (append, pop)

- list는 배열처럼 사용할 수 있으며, stack과 queue 구현에 적합
- DFS에서 stack을 이용한 경로 탐색
- 'pop'은 list요소에서 데이터를 꺼내는 것으로, stack이므로 list 요소 끝에서 부터 제거
  - Stack -> LIFO(Last In First Out)
  - Queue -> FIFO(First In First Out)

```python
stack = []
stack.append(1)  # push
stack.append(2)
stack.pop()      # pop ('2' 제거)
print(stack)
```

    [1]

### Set

- 중복 허용하지 않는 데이터 구조
- 방문한 노드 체크할 때 유용
- DFS, BFS에서 중복된 노드 탐색하지 않기 위해 사용

```python
visited = set()
visited.add(1) #1 방문
if 2 not in visited:
    visited.add(2)
visited.add(1)
print(visited)

visited_test=list()
visited_test.append(1)
if 2 not in visited_test:
    visited_test.append(2)
visited_test.append(1)
print(visited_test)
```

    {1, 2}
    [1, 2, 1]

### Dictionary

- 특정 노드에 대한 데이터 조회할 때 사용
- dictionary의 index번호는 key값이다
- 해시맵과 같은 자료구조

```python
graph = {1:[2,3], 2:[4], 3:[3], 4:[]}
print(graph[1])
print(graph[3])
```

    [2, 3]
    [3]

### 기본 반복문

- for문
- while문

```python
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4

### List Comprehension

- 효율적으로 리스트 초기화 또는 변환
- 인접 리스트나 행렬 초기화에 활용

```python
squares = [x*x for x in range(5)]
print(squares)
```

    [0, 1, 4, 9, 16]

### Lambda

- 짧은 함수
- 정렬, 필터링에 유용

```python
points= [(1,2),(3,4),(5,1)]
points.sort(key=lambda x:x[1])
print(points)
```

    [(5, 1), (1, 2), (3, 4)]

### Map

- 여러 데이터에 동일한 함수 적용

```python
numbers = list(map(int, input().split()))
print(numbers)
```

### filters

- 조건에 맞는 요소만 필터링

```python
even_numbers = list(filter(lambda x:
                           x % 2 == 0,
                           range(10)))
even_numbers
```

### any/all 함수

- any()는 하나라도 True면 True 반환
- all()은 모두 True이어야 True 반환

```python
nums = [1,2,3,4]
print(any(x>2 for x in nums)) #True or False
print(all(x>2 for x in nums)) #True or False
```

    True
    False

### Zip

- 여러 리스트의 원소를 동시 순회

```python
a = [1,2,3]
b = [4,5,6]
for x, y in zip(a, b):
    print(x,y) #열 별로 정렬
```

    1 4
    2 5
    3 6

### collections.defaultdict

- 값이 없을 때 기본값을 자동으로 생성

```python
from collections import defaultdict
graph = defaultdict(list)
graph['A'].append('B')
print(graph)
```

    defaultdict(<class 'list'>, {'A': ['B']})

### collections.Counter

- 빈도수 계산

```python
from collections import Counter
count = Counter([1,2,3,3,3])
print(count)
```

    Counter({3: 3, 1: 1, 2: 1})

### break와 continue

- loop에서 조건에 맞는 경우 빠르게 탈출하거나 건너뜀

```python
for num in range(10):
    if num == 5:
        break #루프 중단
    elif num%2 == 0:
        continue #짝수 건너뛰기
print(num)
```

    5

### for break else

```
# try catch finally 구문처럼 for문에 break와 else로 비슷한 동작이 가능합니다.
for [반복 조건]:
    if:
        print('조건에 해당합니다.')
        break
else:
    print('조건에 해당하지 않습니다.')
```

### try-except

- 예외처리

```python
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot devide by zero")
```

    Cannot devide by zero

### 대소문자 변환

```
import string

lower = string.ascii_lowercase # 소문자(a-z)
upper = string.ascii_uppercase # 대문자(A-Z)
letters = string.ascii_letters # 영문자(a-Z)
digits = string.digits # 숫자(0-9)

"문자열".isupper() # 대문자인지 확인
"문자열".islower() # 소문자인지 확인

"문자열".upper() # 대문자로 변환
"문자열".lower() # 소문자로 변환
```

### 문자열 정렬

```
"문자열".ljust(n) # 좌측 정렬
"문자열".center(n) # 가운데 정렬
"문자열".rjust(n) # 우측 정렬
```

### 변수값 SWAP

```
a = 1
b = 2

a, b = b, a # a = 2, b = 1이 됨
```

### 진법 변환

```
a = bin(42) # 2진수로 변환
b = oct(42) # 8진수로 변환
c = hex(42) # 16진수로 변환

# 다시 10진수로 변환하는 방법
int(a, 2)
int(b, 8)
int(c, 16)
```

## Algorithm implementation grammar

### Recursion

- DFS나 백트래킹문제에서 많이 활용
- 깊이 우선탐색에 유용[링크 텍스트](https://)

```python
def dfs(graph, node, visited):
    visited.add(node)
    print(visited.type())
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

### heapq

- heap(우선순위 큐)을 구현할 때 사용
- 최단 경로 탐색에 유용
- 다익스트라 알고리즘에 쓰임

```python
import heapq
heap=[]
heapq.heappush(heap, (1,'A'))
heapq.heappop(heap)
print(heap)
```

    []

### itertools - Permutations

- 순열을 구하는 백트래킹 문제에 유용

```python
from itertools import permutations #순열
perm = list(permutations([1,2,3]))
for p in perm:
    print(p)
```

    (1, 2, 3)
    (1, 3, 2)
    (2, 1, 3)
    (2, 3, 1)
    (3, 1, 2)
    (3, 2, 1)

### itertools - combinations

- 조합을 구하는 문제에 유용

```python
from itertools import combinations
comb = combinations([1,2,3],2)
for c in comb:
    print(c)
```

    (1, 2)
    (1, 3)
    (2, 3)

### sorted

- 탐색 알고리즘에서 정렬이 필요할 때 유용

```python
arr = [3,1,4,1,5]
sorted_arr = sorted(arr)
print(sorted_arr)
```

    [1, 1, 3, 4, 5]

### collection - deque

- deque는 양방향 queue로, queue와 stack을 효율적으로 구현할 수 있음
- BFS에서 queue를 사용한 탐색
- deque(리스트): dequeue안에는 list형태를 넣어야 함

```python
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)   # 오른쪽에 추가
queue.popleft()   # 왼쪽에서 pop (1 제거)
print(queue)
```

    deque([2, 3, 4])

## Performance improvement grammar

### 데이터 입력

- list, map을 활용하는 경우

```
# 공백을 구분값으로 데이터를 리스트로 입력 받을 경우
arr = list(map(int, input().split()))

# 공백을 구분값으로 정해진 개수의 데이터를 입력 받는 경우
a, b, c = map(int, input().split())
```

- sys 라이브러리를 활용하는 경우(속도가 빠름)

```
import sys

# 공백을 구분값으로 정해진 개수의 데이터를 입력 받는 경우
a, b = map(int,sys.stdin.readline().split())

# 문자열을 입력 받는 경우(sys.stdin.readline()은 문자열 끝의 개행 문자를 자동 제거해주지 않으므로 직접 제거해줘야 함 => rstrip())
str = sys.stdin.readline().rstrip()

# 공백을 구분값으로 데이터를 리스트로 입력 받을 경우
arr = list(map(int,sys.stdin.readline().split()))

# 2차원 리스트로 입력 받을 경우
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
```
