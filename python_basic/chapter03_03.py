# Chapter03_3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형( 순서o, 중복o, 수정o, 삭제o)

# 선언
a = [] # 빈 리스트는 대괄호로 선언
b = list()
c = [70, 75, 80, 85] # len
d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 리스트 안에 다른 자료형을 넣을 수 있음
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # 리스트 안에 리스트를 넣을 수 있다
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱(원화는 과정을 꺼내오는 것)
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1]) # d에 있는 10000을 가져올 때는 대괄호를 치고 그 자료형의 순서를 넣으면 됨
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1]) # 중첩된 리스트에서 가져올 때는 대괄호를 연달아서 쓴다(즉, e리스트 안에 있는 리스트 중 1번째)
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산(리스트 + 리스트 -> 리스트)
print('>>>>>')
print('c + d', c + d) # 순서대로 나열됨
print('c * 3', c * 3) # 곱한 순서만큼 반복
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3]+ c[3:])
print(c)
print(c[:3]+ c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정
print('>>>>>')
c[0] = 4 # 리스트 숫자 변경하는 법
print('c - ', c) 

print()
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']] -> 리스트 안에 대괄호를 넣는 법
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
print()
# 슬라이싱 범위를 지정했을 때는 하나의 원소로, 하나의 리스트 순서만 입력했을 경우 리스트 그대로 들어감

#리스트 삭제
del c[2] # 정석적인 방법
print('c - ', c)
c[1:3] = []
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 마지막 데이터 삽입 함수
print('a - ', a)

a.sort() # 오름차순으로 정렬(정렬)
print('a - ', a)

a.reverse() # 내립차순으로 정렬(역순)
print('a - ', a)
print('a - ', a.index(3)) # a[3]과 같음, a리스트에서 원소를 가져올 때 사용
a.insert(2, 7) # 원하는 위치에 원소 입력(a, b) a: 추가할 위치 번호, b: 넣을 원소
print('a - ', a)
a.reverse()
print('a - ', a)
# del a[6] -> 리스트 위치에 있는 원소를 지움
a.remove(10) # 특정 숫자를 지움
print('a - ', a)
print('a - ', a.pop()) # 리스트 마지막 원소를 빼는 것
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 내가 찾는 값이 리스트 안에 몇개 있는지 알려줌
ex = [8, 9]
a.extend(ex) # 연장하는 것(리스트 뒤에 가져다 붙임)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
