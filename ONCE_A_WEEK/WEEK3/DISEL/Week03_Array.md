3주차: 배열(Array)

  배열

‘인덱스ʼ와 ‘값ʼ의 일대일 대응 자료구조

배열 선언

배열과 리스트는 다른 개념이지만 파이썬에서는 (배열을 지원하는 문법이 없으므
로) 리스트 사용

데이터는 메모리 낮은 주소에서 높은 주소 방향으로 연이어 할당

# 기본 방법
arr = [0,0,0,0,0]
arr = [0] * 6

# list 생성자
arr = list(range(6))

# 리스트 컴프리헨션
arr = list(0 for _ in range(6))
arr = [0 for _ in range(6)]

2차원 배열

arr = [[1,2,3], [3,4,5], [2,3,3]]

print(arr[1][2])

arr[1][2] = 1000 #배열 값 덮어쓰기
print(arr[1][2])

arr = [[i]*4 for i in range(3)] #리스트 컴프리헨션으로 2차원 배
print(arr)

  배열 효율성

3주차: 배열(Array)1배열 연산의 시간복잡도: O1  ON

배열은 데이터를 어디에 저장하느냐에 따라 시간복잡도가 달라짐

데이터 삽입 (맨 뒤 삽입 vs 맨 앞 삽입 vs 중간 삽입) 비교

arr = [0,1,2]
#arr가 위와 같은 상황에 데이터를 맨 뒤에 추가하면, 시간복잡도는 O
#데이터를 맨 앞에 추가하면 기존 데이터를 한칸 씩 밀어야 하므로, 시간
#데이터를 중간에 삽입할 경우 미는 데이터 수 만큼 시간복잡도 발생. 시

배열은 메모리 공간을 충분히 확보해야 함(& 메모리 낭비 주의)

위의 예시에서 “데이터를 맨 뒤에 배치하는 경우ˮ 효율성은 좋지만, 메모리 낭
비 발생 가능성.

이 경우, 할당할 수 있는 메모리 크기 확인 필요

배열로 표현하는 데이터가 너무 많으면 ˮruntime error“발생(런타임에서 
배열 할당에 실패할 수 있음)

운영체제마다 배열 할당 가능 메모리 한계 다름

정수 1차원 배열은 1000만개가 보통 최대

정수 2차원 배열은 3000 * 3000개 (9천만개)가 보통 최대

중간이나 처음 위치에 데이터 삽입이 많은 지 확인 필수

이 경우 시간복잡도가 높아져 실제 시험에서 시간 초과 발생 가능성.

단, 배열을 리스트로 구현시에는 배열 크기 고민할 필요 없음

삭제 연산도 시간복잡도를 갖음 주의

  리스트로 데이터 삽입 / 삭제

(파이썬 과정에서는 배열을 리스트로 설명하기로 함)

데이터 삽입: append(), 연산자, insert()

append() 메서드 활용

맨 끝에 데이터 추가

3주차: 배열(Array)2arr = [1,2,3]
arr.append(4)
print('arr: ', arr)

연산자 활용

my_list = [4,5,6]

my_list.append(4)
print('my_list: ', my_list)

my_list = my_list + [9, 7]
print('my_list: ', my_list)

insert() 메서드 활용

특정 위치에 데이터 삽입

my_list.insert(2, 9999)
print('my_list: ', my_list)

데이터 삭제: pop(), remove()

pop() 메서드 활용

pop할 index를 인수로 받어 삭제하고, 삭제한 데이터 값을 반환

my_list = [1,2,3,4,5]
popped_element = my_list.pop(2) #index 2위치의 element는 

remove() 메서드 활용

특정 위치가 아닌 특정 데이터 자체를 삭제하는 메서드

인수로 받은 값이 처음 등장하는 위치의 데이터를 삭제

my_list = [1,2,4,4,5]
my_list.remove(4)

3주차: 배열(Array)3print('my_list: ', my_list)

리스트 컴프리헨션(list comprehension)으로 데이터 조종

기존 리스트 기반의 새 리스트 생성

반복문, 조건문 이용한 복잡한 리스트 생성

numbers = [1,2,3,4,5]

squares = [num**2 for num in numbers]
print('squares: ', squares)

리스트 연관 메서드

fruits = ['apple', 'banana', 'apple', 'cherry', 'orange', 
print('fruits: ', fruits)

print('no of fruits: ', len(fruits))

print('index: ', fruits.index('banana'))

print('sort: ', fruits.sort()) # sort()메서드는 반영만.

print('count: ', fruits.count('apple'))

print('fruits: ', fruits)
fruits.sort(reverse=True)

print('fruits: ', fruits)

  기본 예제

문제01 - 배열 정렬

'''
문제1. 정수 배열을 정렬해서 반환하는 solution()함수 완성하기
- 정수 배열 길이는 2 ~ 105.
- 정수 배열 각 데이터값은 -100,000 ~ 100,000.

3주차: 배열(Array)4(input)
[1,-5,2,4,3]
[2,1,1,3,2,5,4]
[6,1,7]

(output)
[-5,1,2,4,3]
[1,1,2,2,3,4,5]
[1,6,7]

'''

import sys

def solution_ex01():
    with open('/content/drive/MyDrive/Colab Notebooks/Algo

        results=[]
        for _ in range(3):

            result = list(map(int, f.readline().split()))
            result.sort()

            results.append(result)
        return results
print(solution_ex01())

문제02 - 배열 제어

'''
문제2. 정수 배열 받아, 배열의 중복값을 제거하고 내림차순으로 정렬해서 
배열 길이는 2 ~ 1,000.
각 배열의 데이터 값은 -100,000 ~ 100,000.

(input)

[4,2,2,1,3,4]

[2,1,1,3,2,5,4]

(output)

3주차: 배열(Array)5[4,3,2,1]

[5,4,3,2,1]
'''
def solution_ex02():
    with open('/content/drive/MyDrive/Colab Notebooks/Algo

        results=[]
        for _ in range(2):
            result = set(map(int, f.readline().split())) #
            result = list(result) #2.list()로 변환하고
            result.sort(reverse=True) #3. list를 sort()로 정
            results.append(result)
        return results
print(solution_ex02())

  모의 테스트

문제03 - 두 개 뽑아 더하기

'''
문제3. 두 개 뽑아서 더하기
정수 배열 numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만
배열에 오름차순으로 담아 반환하는 solution()함수 완성.
- numbers 길이는 2 ~ 100.
- numbers 모든 수는 0 ~ 100.

(input)
[2,1,3,4,1]

[5,0,2,7]

(output)

[2,3,4,5,6,7]

[2,5,7,9,12]
'''

def solution():
    with open('/content/drive/MyDrive/Colab Notebooks/Algo
        results = [] #위치 주의(for문 밖에서!)

3주차: 배열(Array)6        for _ in range(2): #test case = 2

            numbers = list(map(int, f.readline().split()))
            result = []
            # graph = [[0]*len(numbers) for _ in range(len
            # visited = [0] * len(numbers)

            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    result.append(numbers[i] + numbers[j])
            result = list(set(result))

            result.sort()
            results.append(result)
        return results

solution()

문제04 - 모의 고사

문제05 - 행렬의 곱셈

문제06 - 실패율

문제07 - 방문 길이

3주차: 배열(Array)7                    
