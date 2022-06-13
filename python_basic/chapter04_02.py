# Chapter04-2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#   <Loop body>

for v1 in range(10): # 0~9까지의 수
    print('v1 is :', v1)
print()

for v2 in range(1, 11): # 1~10까지의 수
    print('v2 is :', v2)
print()

for v3 in range(1, 11, 2): # 1~10까지 2칸씩 띄워서 출력
    print('v3 is :', v3)
print()

# 1~1000 합

sum1 = 0

for v in range(1, 1001):
    sum1 += v # a += b -> a = a + b (a에 새로운 값인 b를 더하고 그 값을 다시 a로 저장함)

print('1 ~ 1000 Sum :', sum1)

print('1 ~ 1000 Sum :', sum(range(1, 1001))) 
# sum(range(1, 1001))을 해도 1부터 1001을 더한 값이 나오는 이유는 range의 값을 리스트로 만들어 sum 하기 때문

print('1 ~ 1001 4의 배수의 합 : ', sum(range(4, 1001, 4)))
# for s in range(4, 1001, 4): , print(s)를 하게 되면 결과값이 4의 배수로 정확하게 더해진 것 알 수 있다(디버깅)

# Iterables(문자열) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are :', n)

# 예제2
lotto_number = [11, 19, 21, 28, 36, 37]

for n in lotto_number:
    print("Currnet number :", n)

# 예제3
word = "Beautiful" # 문자열도 리스트돼서 하나씩 출력

for s in word:
    print('word :', s)

print()

# 예제4

my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for k in my_info:
    print('key :', k) # k를 넣으면 key를

for k in my_info:
    print('key :', my_info[k]) # my_info[k] my_info에 k를 넣어주면 밸류
print()

for v in my_info.values():
    print('value :', v) # 이렇게로도 밸류 출력 가능

# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper(): # 대문자라면(islower=소문자)
            print(n)
    else:
        print(n.upper()) # 대문자로 출력
print()

# break (break문을 만나면 실행 종료)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break # 34를 찾으면 멈춤
    else:
        print('Not found :', num)


# countinue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue # 내가 설정한 값을 만나면 스킵시킬 수 있다
    print("current type :", v, type(v))
    print("multiply by 2 :", v * 3)
print

# for - else (결과값만 찾아서 알려줌)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else:
    print('Not found : 24') 

# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()


# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 집합은 순서 x































