# chapter02-1
# 파이썬 완전 기초
# print 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""") # 3개씩 쓰기도 함

print() # 띄어쓰기 역할을 함

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='') # sep 옵션은 공백말고 다른 문자를 넣을 수 있도록 한다
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션

print('Welcome to', end=' ')
 # 일반적인 print문은 자동 줄바꿈, end옵션을 사용하게 된면 마지막 부분에 어떤 것을 넣을지 설정 가능
print('IT News', end=' ')
print('Web Site')
print()
# file 옵션
import sys
print('Learn Python', file=sys.stdout) # 현재 내용을 외부, 즉 하드디스크에 있는 파일옵셥에 저장
print()


# format 사용(d(정수), s(문자열), f(실수)) 중요
# =(d : 3, s : 'python', f : 3.14454)
print('%s %s' % ('one', 'two')) # %s를 넣으면 그 뒤에 오는 문자열을 넣을 수 있다?
print('{} {}' .format('one', 'two')) # format은 s,d,f를 유연하게 처리해준다
print('{} {}' .format('one', '2'))
print('{1} {0}' .format('one', 'two'))
 # {}공백이 오면 0부터 시작한다. 여기에 {1}{0}순서를 넣어주면 1>0 이기 때문에 {1}에 보다 더 큰 숫자가 오게 되는 것이다.


# %s
print('%10s' % ('nice')) #10은 10개의 자릿수를 의미, nice는 4자리이기 때문에 나머지 6자리는 공백으로 표시해준다
print('{:>10}' .format('nice'))

print('%-10s' % ('nice')) # 양수 : 왼쪽부터 공백, 음수 : 오른쪽부터 공백
print('{:10}' .format('nice')) # 부등호 방향으로 공백,^ : 중앙정열, 없으면 오른쪽부터 공백

print('{:_>10}' .format('nice'))
print('{:_<10}' .format('nice'))
print('{:^10}' .format('nice'))




