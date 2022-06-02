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

# 멀티라인 입력
# 역슬래쉬 사용
multi_str = "blalblalblalblalblalblal" # 많은 텍스트를 입력할때
# multi_str2 = 
# '''
# String
# multi line
# Test
#'''        -> 이렇게 하는 것은 오류가 난다.
multi_str2 = '''
String
multi line
Test
'''        # -> 이렇게 해주거나

multi_str3 = \
'''
String
Multi line
Test
'''         # -> 깔끔하게 해줄때는 '\'를 사용하면 됨

print(multi_str2)
print(multi_str3)

# 문자열 연산
str_o1 = "pyhon"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3) # 문자열을 곱하면 그 수 만큼 반복됨
print(str_o1 + str_o2) # 문자열을 더하면 더한 문자열을 나열해줌
print('y' in str_o1) # ''안에 들어가는 문자가 문자열에 있는지 물어보는 구문
print('n' in str_o1)
print('P' not in str_o2) # "not in"은 ''이 문자열에 들어가 있지 않나요?라고 물어보는 구문, 그렇기에 없으면 True가 나옴

# 문자열 형 변환
print(str(66), type(str(66))) # 숫자를 str에 넣어 문자열로 치환
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 첫번째 글자를 대문자로 바꿔주는 역할
print("endswith?: ", str_o2.endswith("e")) # 끝 글자가 뭐로 끝나는지 확인할때
print("replace", str_o1.replace("thon", 'Good')) # 문자열 중 ""에 들어있는 문자를 ''의 문자로 바꿈








