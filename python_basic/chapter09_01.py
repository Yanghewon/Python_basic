# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 : W, 추가 모드 : a(append), 텍스트 모드(기본값이기 때문에 생략 o) : t, 바이너리 모드 : b
# 상대 경로('../, ./'), 절대 경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제1

# f = open('C:\\PythonPartice\\python_basic\\resource\\it_news.txt') # resource에 있는 it_news.tst를 읽기 위해서 open함
# 10번줄은 절대 경로로 불러온 것
f = open('./resource/it_news.txt', 'rt', encoding='UTF-8') # 'rt'는 우리가 읽을 파일이 텍스트이므로 텍스트를 읽는다는 뜻(텍스트는 기본값이기 때문에 t는 생략 o)
#12번줄은 상대 경로로 불러온 것
# 인코딩을 알아야 파일이 안 깨짐(ex.UTF-8)

# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
print()
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close(open을 했으면 꼭 close)
f.close()

# 예제2
# with문은 open을 사용해도 close를 안 써도 됨
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read() : 전체 읽기, read(10) : 10byte

with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read(20) # read(x) -> x만큼의 글자를 가져옴
    print(c)
    c = f.read(20) # 마지막에 읽은 곳을 기억하고 그 뒤부터 출력
    print(c)
    f.seek(0,0) # 처음으로 돌아감
    c = f.read(20)
    print(c)

print()

# 예제4
# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    # line = f.readline()
    print(f.readline()) # 라인을 통으로 출력

print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts) # /n -> 줄바꿈
    print()
    for c in cts:
        print(c, end='')

print()

# 파일 쓰기(write)
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'wt') as f:
    f.write('I love python2\n') # 기존 내용이 지워지고 새로운 내용이 생김

# 예제3
with open('./resource/contents1.txt', 'a') as f: # a를 쓰면 새롭게 생성이 아닌 기존 파일에 추가가 됨
    f.write('I love python3\n') 

# 예제4
# writelines : 리스트 -> 파일
with open('./resource/contente2txt', 'w') as f:
    list = ['Orange\n', 'Apple/n', 'Banana\n', 'Melon\n'] # \n 줄바꿈
    f.writelines(list)


# 예제5
with open('./resource/contents3.txt', 'w') as f:
    print('Test text Write!', file=f) # file=f는 터미널이 아니라 파일에 직접 출력이 됨
