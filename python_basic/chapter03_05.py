# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (json형태)
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 복습
"""
[] : 리스트
() : 튜플
{} : 딕셔너리
"""

# 선언
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '870514'} # {'a': 'b'}, a를 '키', b를 '값'이라고 부른다
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]} # 리스트를 넣어도 됨
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}

e = dict([                  # 너무 교과적
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(                   # 보다 많이 사용하는 방식
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # 키가 존재x ->에러발생
print('a - ', a.get('name')) # 키가 존재x ->None처리 (키가 없어도 프로그램이 돌아감으로 많이 사용)
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가(기존에 있는 키면 수정, 없는 키면 추가)
a['address'] = 'seoul' # 맨 뒤에 추가
print('a - ', a)
# a['name'] = 'seoul' -> 같은 키를 가지고 있으면 수정함
a['rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a)) # 이때 'len'은 키의 개수를 셈
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print()

# dict_ket, dict_valuse, dict_items : 반복문(__iter__)에서 사용 가능 

print('a - ', a.keys()) # 딕셔너리의 키만 가져옴
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys())) # 리스트로 형변환
print('b - ', list(b.keys()))

print()

print('a - ', a.values()) # 딕셔너리의 값만 가져옴
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print('a - ', a.items()) # 딕셔너리의 키와 값을 하나의 튜플 형태로 출력
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name')) # 'name'을 꺼내옴(그 후 딕셔너리 값에서 사라짐)
print('a - ', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem()) # 'popitem'은 임의로 키와 값을 하나 꺼내옴
print('f - ', f)

print()

# 딕셔너리 조회
print('a - ', 'birth' in a) # 딕셔너리에 해당하는 키 값이 있는지 알려줌
print('d - ', 'city' in d)

# 추가 & 수정
a['test'] = 'test_dict' # 추가
print('a - ', a)

a['address'] = 'dj' # 수정
print('a - ', a)

a.update(birth='910904') # 수정(문법적으로 확실하게 설명하는 법)
print('a - ', a)

temp = {'address': 'Busan'} # 수정
a.update(temp)
print('a - ', a)








