# Chapter03_01
# 숫자형

# 파이썬 지원 자료형(알아만 두기)
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dixt : 사전
"""
# int(정수) + float(실수) : 사용가능(프로그램에서 알아서 형 변환이 이루어짐)

# 데이터 타입
str1 = "Pyhton"
bool = True
str2 = "Anaconda"
float = 10.0 # 10(정수), 10.0(실수) -> 같은 수 없다.
int = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}

tuple = (7, 8, 9) #tuple은 {}, () 두 괄호 다 씀, 괄호 없어도 되지만 비선호(괄호에 따라 타입이 달라짐)
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abd(x) :  절대값
pow(x, y) : x ** y -> 2 ** 3 #제곱을 한다
"""

# 정수 선언
i = 77
i2 = -14
big_int = 87777777999999999999999999999 # 큰 수도 할당 가능

# 정수 출력
print(i)
print(12)
print(big_int)
print()

# 실수 출력
f = 0.999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 9999999999999
big_int2 = 234324234223423
f1 = 1.234
f2 = 3.939

# +
print(">>>>>+")
print("i1 + i2 : ", i1 + i2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# *
print(">>>>>*")
print("i1 * i2 : ", i1 * i2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)


