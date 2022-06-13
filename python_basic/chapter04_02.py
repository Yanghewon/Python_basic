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

word = "Beautiful"

for s in word:
    print('word :', s)












































