# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다
# 4. 예외 무시

    # SyntaxError : 문법 오류
# print('error) -> '을 하나만 붙일 경우
# print('error')) -> ()가 짝이 안 맞을 경우
# if True       -> :을 안 붙였을 경우
#     pass

    # NameError : 참조 없음
# a = 10
# b = 1
# print(c) -> 없는 변수를 호출할 때

    # ZeroDivisionError : 수학적으로 불가능한 것
# print(100 / 0)

    # IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[5]) -> 리스트에 없는 것을 호출할 때
# 또는
# print(x.pop()) -> 리스트의 개수보다 많은 pop을 사용할 때
# print(x.pop()) -> pop은 리스트에서 꺼낸 후 삭제하기 때문
# print(x.pop())
# print(x.pop())

    # KeyError
# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby']) -> dic에 없는 것을 호출했기 때문
# print(dic.get('hobby')) -> dic에 없어도 get함수를 사용하면 None으로 출력되면서 오류발생 x

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

    # AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time

    # ValuError : 참조 값이 없을 때
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200) -> 자료구조 안에 데이터가 존재하지 않을때

    # FileNotFoundError : 없는 파일을 찾을 때
# f = open('test.txt')

    # TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'

# print(x + y) -> list는 가변형, tuple은 불변형 이기 때문에 내부적 구조로 인해 데이터를 하나로 합칠 수 없다
# print(x + z)
# print(y + z)

# print(x + list(y)) -> 맞지 않은 자료형을 합칠 땐 형변환 필수
# print(x + list(z))

# 예외 처리 기본
# try : 예외가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명 2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
# try: # 외부에 있는 프로그램과 커넥션을 연결할 때 에러가 발생할 수 있기 때문에 사용
#     z = 'Kim'
#     x = name.index(z) # 리스트의 위치 번호를 알려줌
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError: -> 정확한 에러명을 남기는 것도 알아보기 편함
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print()

# 예제2

# try: # 외부에 있는 프로그램과 커넥션을 연결할 때 에러가 발생할 수 있기 때문에 사용
#     z = 'Cho'
#     x = name.index(z) # 리스트의 위치 번호를 알려줌
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception: # 모든 예외격의 부모(이 안에서 예외를 잡음, 모든 예외를 처리할 수 있음)
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# 예제3

# try: # 외부에 있는 프로그램과 커넥션을 연결할 때 에러가 발생할 수 있기 때문에 사용
#     z = 'Cho'
#     x = name.index(z) # 리스트의 위치 번호를 알려줌
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception as e: # 모든 예외격의 부모(이 안에서 예외를 잡음)
#     print(e) # Exception as e을 했기 때문에 어디서 에러가 났는지 알 수 있음
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')
# finally:
#     print('ok! finally!') # 에러가 발생하든 안 하든 꼭 실행시켜야 하는 구문을 쓸 때 사용(finally)

print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'park'
    if a == 'kim':
        print('Ok! Pass!')
    else:
        raise ValueError # 직접 예외를 만든 것
except ValueError: # 직접 에러 처리
    print('Occurred! Exception!')
else:
    print('Ok! else!')












