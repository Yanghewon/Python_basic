# Chapter03-6
# 집합(set) 특징
# 집합(set) 자료형(순서x, 중복x)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo','quz'} # 괄호가 '딕셔너리'같아 보이지만 key가 없이 value만 있기 때문에 '집합(set)'으로 처리함
f = {42, 'foo', (1, 2, 3), 3.141592} 

print('a - ', type(a), a, 2 in a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])
print()


#리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2) # s1, s2의 교집합을 출력
print('s1 & s2 : ', s1.intersection(s2)) # intersection(교차)


print('s1 | s2 :', s1 | s2)
print('s1 | s2 :', s1.union(s2))

print('s1 - s2 : ', s1.difference(s2)) # 차집합

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # False: 교집합o, True: 교집합x

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # s1이 s2의 부분집합인지 확인
print('superset : ', s1.issuperset(s2)) #s2가 s1의 집합인지 확인

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)

print('s1 - ', s1)

s1.remove(2) # s1.remove(7) 원소에 없는 값을 입력하면 에러가 생긴다
print('s1 - ', s1)

s1.discard(3) # 제거 함수 / s1.discard(7) 원소에 없는 값을 입력해도 에러 발생 안 한다
print('s1 - ', s1)

s1.clear()
print('s1 - ', s1) # 온전히 지움

a = [1, 2, 3]
a.clear()
print(a)

