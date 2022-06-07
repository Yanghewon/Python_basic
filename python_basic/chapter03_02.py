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

print("sorted: ", sorted(str_o1)) # 정렬해서 나온다
print("split: ", str_o4.split(' ')) # ''에 들어오는 것을 기준으로 분리한다

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ (iter이 들어있으면 반복할 수 있다는 의미)

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_sl = "Nice Python" # 글자수를 샐 때 0부터 시작한다

print(len(str_sl)) # 글자수를 알려줌
# 슬라이싱 연습
print(str_sl[0:3]) # 0 1 2에 위치한 글자만 나온다(3뒤에 -1이 생략되어 있는 것으로 2째자리 숫자만 나옴)
print(str_sl[5:11]) # = print(str_sl[5:]) -> :만 쓰게 되면 문자열의 끝까지 나오게 됨
print(str_sl[:]) # 다 비워두면 처음부터 끝까지 나옴
print(str_sl[:len(str_sl)]) # len을 사용해서 글자수를 넣은 경우 -1은 처리하지 않는다(본래 글자수 만큼 처리)
print(str_sl[1:12:2]) # [1:12:2씩 띄워서 출력]
print(str_sl[-5:]) # 숫자에 -가 붙으면 뒤에서부터 시작(-는 -1부터 시작)
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

# 아스키 코드(또는 유니코드)
a= 'z' # 파이썬에는 알파벳에 맞는 번호가 있다

print(ord(a)) # 알파벳 a에 맞는 아스키 코드를 알려줌
print(chr(122))



