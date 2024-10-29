# input: 1 2 3
# output: [1, 2, 3]
arr = list(map(int, input().split()))
print(arr)

# input: 1 2 3
# output: 1 2 3
a, b, c = map(int, input().split())
print(a, end=" ")
print(b, end=" ")
print(c)



import sys

# input: 1 2
# output: 1 2
a, b = map(int,sys.stdin.readline().split())
print(a, end=" ")
print(b)

# input: 안녕하세요
# output: 안녕하세요
str = sys.stdin.readline().rstrip()
print(str)

# input: 1 2 3
# output: [1, 2, 3]
arr = list(map(int, sys.stdin.readline().split()))
print(arr)

# input: 1 2 3 [ENTER] 4 5 6
# output: [[1, 2, 3], [4, 5, 6]]
board = [list(map(int,sys.stdin.readline().split())) for _ in range(2)]
print(board)



import sys
input = sys.stdin.readline
print = sys.stdout.write

print("%s\n" % "123")
print("%s\n" % ("12" + "3"))
print("%d + %d = %d\n" % (1, 2, 1 + 2))


import string

lower = string.ascii_lowercase
print(f'lower: {lower}')

upper = string.ascii_uppercase
print(f'upper: {upper}')

letters = string.ascii_letters
print(f'letters: {letters}')

digits = string.digits
print(f'digits: {digits}')

print("abc".upper())
print("ABC".lower())

print("abc".isupper())
print("abc".islower())



print("abc".ljust(5))
print("abc".center(5))
print("abc".rjust(5))


a = [1, 2, 3]
b = ['one', 'two', 'three']

print(dict(zip(a, b)))
print(list(zip(a, b)))

c, d = zip(*zip(a, b))
print(list(c))
print(list(d))



import collections

collector = collections.Counter([1, 1, 1, 2, 3, 4, 4])

print(collector[1])
print(collector[4])
print(collector[5])



for i in range(10):
    if i == 11:
        print('조건에 해당합니다.')
        break
else:
    print('조건에 해당하지 않습니다.')



a = 1
b = 2

a, b = b, a

print(a, end=" ")
print(b)



a = bin(42)
print(a)
print(int(a, 2))

b = oct(42)
print(b)
print(int(b, 8))

c = hex(42)
print(c)
print(int(c, 16))