# Chapter08-1
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple()의 형변환은 이미 학습

# 절대값
# abs()

print(abs(-3))

# all, any : iterable 요소 검사(참, 거짓)
print(all([1, 2, 3])) # and조건, 값이 모두 참일 때: 참, 하나라도 거짓일 때: 거짓
print(any([1, 2, 0])) # or조건, 값이 모두 거짓이여야만: 거짓, 하나라도 참일 때: 참

# chr: 아스키코드 -> 문자, ord: 문자 -> 아스키코드
print(chr(67))
print(ord('C'))

# enumerate: 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']): 
    # enumerate를 사용하면 i에는 인덱스(0, 1, 2...처럼 for구문에서 반복되는 숫자를 나타냄), name에는 실제 리스트의 값을 넣어줌
    print(i, name)


# filter 함수: 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2 # 절대값이 2보다 클 경우

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6]))) # list를 사용하지 않으면 filter object값으로 나옴
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))
print()

# id: 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))


# Len: 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))


# max, min: 최대값, 최소값
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))
print()


# map: 반복가능한 객체 요소를 지정하 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-3,2,0,-5,6]))) # 함수를 통해 조건에 맞게 색을 입힌 후 모두다 출력
print(list(map(lambda x :abs(x), [1,-3,2,0,-5,6])))

# pow: 제곱값 반환
print(pow(2,10)) # 2의 10승


# range: 반복가능한 객체(Iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))


# round: 반올림
print(round(6.5781, 2)) # 소수자리 2번째까지 반올림하여라
print(round(5.6)) # 바로 소수점 첫번째자리가 반올림 됨


# sorted: 반복가능한 객체(Iterable) 정렬 후 반환
print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))


# sum: 반복가능한 객체(Interable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))


# type: 자료형 확인
print(type(3))
print(type({3,4}))
print(type(()))
print(type([]))

# zip: 반복가능한 객체(Interable)의 요소를 묶어서  튜플로 반환

print(list(zip([10,20,30], [40,50,60]))) # list를 안 쓰면 object로 반환됨(알아서 형변환 해야함)
print(list(zip([10,20,30], [40,50]))) # 짝이 안 맞으면 반환 x



















