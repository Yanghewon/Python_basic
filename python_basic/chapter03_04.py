# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 선언
a = ()
b = (1,) # 원소가 하나일 때만 뒤에 ,로 마무리 지어야 튜플로 취급한다
         # b = (1) -> ,를 안 쓰면 int(정수)로 취급
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine')) # 튜플 안에 중첩으로 튜플을 넣을 수 있다

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1])) # 튜플이 리스트로 형변경 가능(리스트의 효과를 보고 싶을 때)

# 수정x (불가능 확인)
# d[0] = 1500

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 숫자가 어느 위치에 들어있는지 물어보는 함수
print('a - ', a.count(2)) # 2가 들어간 숫자가 몇개 들어있는지 물어보는 함수

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹(여러가지를 하나로 묶는 작업)
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])
print(type(t))
print()

# 언팩킹1(묶여 있던 것을 풀어서 하나의 객체로 만들어줌)
(x1, x2, x3, x4) = t
# x1, x2, x3, x4 = t -> 괄호를 안 묶더라도 '언팩킹' 가능(하지만 묶는것이 통념)

print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))

# 팩킹 연습
t2 = 1, 2, 3 # 괄호로 안 묶어도 튜플로 인정
t3 = 4, # 괄호는 생략 가능해도 튜플로 만들려면 ","를 넣어야 한다

# 언팩킹 연습
x1, x2, x3 = t2 # -> 언팩킹
x4, x5, x6 = 4, 5, 6 # 각 원소에 할당 가능

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
