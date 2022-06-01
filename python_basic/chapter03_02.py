# Chapter03_02
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Pyhton"
str2 = 'Pyhton'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 문자열의 길이를 구해줌

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 넣을 문자
...
"""

print("I'm Boy") # 작은 따움표를 넣기 위해서는 큰 따움표로 묶어줘야 함
print('I\'m Boy') # \(역슬러쉬) 뒤에 ', "를 붙이면 그대로 출력

print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on Tv?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

# Raw String : \(역슬러쉬)를 사용해야 할 때 써야함
raw_s1 = r'D:\python\test'
print(raw_s1)
print()








