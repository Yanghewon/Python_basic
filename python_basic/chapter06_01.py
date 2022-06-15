# Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수
# 메소드(method)는 객체(object)와 연관되어 사용 -> 사용하고자 하는 대상이 .으로 연결되어 있어야 함
# str, float, list와 같은 자료형은 모두 객체이므로 이러한 자료형과 연관되어 사용되는 것은 메소드로 볼 수 있다

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유(species = firstdog를  모두가 공유하는 것 처름)
# 인스턴스 변수 : 객체마다 별도 존재(self, name, age를 사용하여 나만의 변수를 가지는 것)

# 예제1

from unicodedata import name


class Dog(object): # object 상속 받음
    # 클래스 속성
    species = 'firstdog'

    # 초기화/ 인스턴스 속성
    # __init__은 인스턴스화 실시할 때 반드시 처음에 호출되는 특수 함수
    # __init__은 오브젝트(인스턴스 생성)과 관련하여 데이터 초기를 실시하는 함수
    # __init__()은 반드시 첫 번째 인수로 self를 지정
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("mikky", 2) # a와 c의 값은 같아보여도 프로그램에서는 전혀 다른 객체로 간주

# 비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스
print('dog3', a.__dict__)
print('dog4', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예제2
#self의 이해
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print('Func2 called')


f = SelfTest()

# print(dir(f)) 우리가 지정할 수 있는 함수가 나옴, 그 중 class에서 지정한 'func1', 'func2'가 들어있는 것을 확인할 수 있음

print(id(f))

# f.func1()
f.func2()

SelfTest.func1()
SelfTest.func2(f) # func2에서는 self가 있기 때문에 인스턴스를 요구 -> 인스턴스 f를 넣어줘야 예외가 발생하지 않음
# f.func1()을 출력하면 에러가 나온다. 왜냐 'self'를 지정하지 않았기 때문(self는 인스턴스를 요구)
# 'self'에 f가 넘어간 것이기 때문에 func1()에는 self
# func1을 실행시키려면 바로 class에 접근하면 됨 -> SelfTest.func1()
# 인스턴스를 실행시키기 위해서는 self가 필수

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # stock_num을 재고로 생각하자

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num +=1

    def __del(self): # 객체가 소멸할때 자동으로 소환되는 함수
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse라는 Class에 'Lee'와 'Cho'가 생성되었기 때문에 stock_num = 2가 된 것
# 'Lee', 'Cho'는 self에 할당되는 인스턴스가 되는 것

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__) # stock_num은 공유되는 변수인데, user1, user2(인스턴스 네임스페이스)에 없는 것은 class에 들어가 stock_num을 찾고 인스턴스 네임스페이스에 할당한다.
print('before', Warehouse.__dict__) # Warehouse에 stock_num이 들어있는 것을 확인 가능

del user1
print('after', Warehouse.__dict__) # del은 지우는 함수이기 때문에 Warehouse.__dict__을 보면 stock_num을 보면 1로 수정된 것을 알 수 있다
print()

# 예제4
class Dog2: # object 상속 받음
    # 클래스 속성
    species = 'firstdog'

    # 초기화/ 인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return'{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog2('july', 4)
d = Dog2('Marry', 10)

# 메소드 호출
print(c.info())
print(d.info())

# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))














