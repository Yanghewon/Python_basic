# Chapter08-2
# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제1
import sys
print(sys.argv)

# 예제2(강제 종료)
# sys.exit() -> 매우 위험한 함수(실행시켰을 때 만나면 바로 종료시켜버리기 때문)


# 예제3(파이썬 패키지 위치)
print(sys.path)


# pickle : 객체 파일 쓰기
import pickle
print()

# 예제4(쓰기)
f = open("test.obj", 'wb') # 열고나서 23줄처럼 닫아줘야함
obj = {1: 'python', 2: 'syudy', 3: 'basic'}
pickle.dump(obj, f) # 쓰는 것을 할 때는 'dump'
f.close() # 닫아줘야 함
print()

# 예제5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f) # 읽는 것을 하는 것은 'load'
print(data, type(data))
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(파일이 비어 있으면 삭제), rename

# 예제6
import os
print(os.environ)
print(os.environ["USERNAME"])

# 예제7
print(os.getcwd()) # route 경로 표시
print()

# time : 시간 관련 처리
import time

# 예제8
print(time.time())

# 예제9(형태 변환)
print(time.localtime(time.time()))

# 예제10(간단한 표현)
print(time.ctime())

# 예제11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) # 내가 원하는 방식으로 표현 가능

# 예제12(시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1) # 1초 간격으로 출력

# random : 난수 리턴
import random  # 외부함수는 직접 가져와야 함

# 예제13
print(random.random())

# 예제14
print(random.randint(1,45))
print(random.randrange(1,45))

# 예제15(섞기)
d = [1,2,3,4,5,]
random.shuffle(d) # 랜덤으로 섞기
print(d)

# 예제16(무작위 선택)
c = random.choice(d)
print(c)

# webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser

webbrowser.open("http://google.com")

webbrowser.open_new("http://google.com") # 새 창으로 연다










