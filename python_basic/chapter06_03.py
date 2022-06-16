# Chapter06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천(패키지파일에 있음)
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용 가능

# 예제1
import sub.sub1.module1 # 해석: sub패키지 안에 sub1 패키지 안의 많은 모듈들 중에 module1을 가져오는 것
import sub.sub2.module2 # 해석: sub패키지 안에 sub2 패키지 안의 많은 모듈들 중에 module2을 가져오는 것

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module1 # 경로를 다 작성해야하는 불편함을 줄이고자 from을 사용함
from sub.sub2 import module2 as m2 # alias

# sub.sub1.module1.mod1_test1()
module1.mod1_test1() # 23줄에 나온 것처럼 from을 사용했기 때문에 26번줄보다 간략하게 호출할 수 있음
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
# from sub.sub1 import * -> *로 가져오게 되면 전체를 가져오는 것으로 훨씬 간략함(그러나 너무 많은 정보를 가져기 때문에 비추)
# from sub.sub2 import *

# module1.mod1_test1()
# module1.mod1_test2()

# module2.mod2_test1()
# module2.mod2_test2()