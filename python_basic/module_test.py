# 모듈 사용 실습
# 현재 c드라이브에 math파일 삭제함

import sys

# print(sys) # 이미 만들어진 것이기 때문에 (built-in)이라고 출력됨
print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
sys.path.append('C:/math/') # 경로 뒤에 append로 'C:/math/'가 삽입됨

print(sys.path)

# import test_module
import chapter06_02

# 모듈 사용
print(chapter06_02.power(10, 3))



