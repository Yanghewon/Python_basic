# Chapter04-1
# 파이썬 제어문
# If 실습

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1,2,3...], (1,2,3...) ...
print(type(False)) # 0, "", [], (), {} ...

# 예1 (참일 때 출력)
if True:
    print('Good')

# 예2 (거짓일 때 출력x)
if False:
    print('Bad')

# 예3
if False:
    print('Bad!')
else:
    print('Good')
print()

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양 변이 같은 경우 참
print(x == y)

# 양 변이 다를 때 참
print(x != y)

# 왼쪽이 크거나 같은 때 참
print(x >= y)

# 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

# 예4
city = ""
if city:
    print("You are in :", city)
else:
    print("Please enter your city")

# 예5
city2 = "Seoul"
if city2:
    print("You are in :", city2)
else:
    print("Please enter your city2")

# 논리 연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:', a > b and b > c) # a > b > c
print('or:', a > b or b > c)
print('not', not a > b)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 우선순위 : 산술 -> 관계 -> 논리
print('e1 :', 3+12 > 7+3)
print('e2 :', 5+10 * 3 > 7+3 * 20)
print('e3 :', 5+10 > 3 and 7+3 == 10)
print('e4 :', 5+10 > 0 and not 7+3 == 10)

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

# 예6
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 =='vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')
