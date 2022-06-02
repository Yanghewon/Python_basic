# Chapter02_02
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) # n에 대한 타입을 알려줌

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = "Change Value" # 앞에 선언한 값을 덮어 씀

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

#id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n)) # '=='는 서로 같냐는 것을 물어보는 것
print()

#같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
# 800에 대해 여러 변수를 선언해도 프로그램에서는 하나의 변수를 선언한 것으로 판단(생산성때문)
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method선언할 때 사용
# Pascal Case : NumberOfCollegeGraduates -> Class선언할 때 사용
# Snake Case(추천)  : number_of_college_graduates -> Python에서 변수 선언할 때 사용

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 예 : 1age = 9 처럼 숫자가 먼저 오면 선언 불가

# 예약어는 변수명으로 불가능
# 예 : for, class, else, end, or ...
