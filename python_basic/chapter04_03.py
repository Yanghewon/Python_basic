# Chapter04-3
# 파이썬 반복문
# While 실습

# while <expr>:
#   <statement(s)>

# 예제1

n = 5
while n > 0:
    n = n - 1
    print(n)


# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop()) # pop 함수는 뒤에서부터 꺼내오는 것이기 때문에 pop(-1)과 같다


# 예제3
#break, continue

n = 5
while n > 0:
    n -=1
    if n == 2:
        break
    print(n)
print('Loop Ended.')


# 예제4
m = 5
while m > 0:
    m -=1
    if m == 2:
        continue # 해당 값을 건너뛴다
    print(m)
print('Loop Ended.')


# if 중첩
# 예제5

i = 1
while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1


# While - else 구문
# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')


# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s =  'qux'
i = 0

while i < len(a): # a의 길이는 4 즉, i < 4 의 식과 같다
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')


# 무한반복(무한반복은 프로그램이 계속 돌아가서 망가질수도 있음)
# while True:
#   print('foo)

# 예제8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())
