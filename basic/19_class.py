# 객체지향프로그래밍(object oriented programming) : 자바, c++, 자바스크립트, 파이썬
# => 객체 개념이 도입된 프로그래밍
#     객체? 주체(자신)가 바라보는 사물을 의미
#         ex) 학생, 컴퓨터, 책상, ...
#     객체의 2가지 요소 ( 학생 객체 )
#         1) 속성 : 학번, 이름, 주소, 전화번호
#         2) 동작 : 공부하기, ...
#
#     프로그래밍화 하면?
#         학생객체 => 클래스
#         속성 => 변수
#         동작 => 함수
#
#     관계 : 객체들간의 관계 정의

# 1. 클래스 정의 (객체를 표현)
class Student:      # class 의 이름은 관습적으로 첫글자가 대문자이다.
    # name=""       # 초기값을 주지 않는 경우 "" 혹은 None 으로 값을 줘도 된다.
    name = None
    age = 10

# 2. 클래스 메모리에 올리는 작업: 객체 생성
# 변수명 = 클래스명()
s1 = Student()
print(s1)
s1.name = "이순신"
s1.age = 44
print(s1.name + " " + str(s1.age))

s2 = Student()
print(s2)
s2.name = "유관순"
s2.age = 18
print(s2.name + " " + str(s2.age))

print("#"+"-"*20+"#")

# 3.1 생성자
class Student:
    name = None
    age = 10

    def __init__(self):  # 생성자 , 'self' 는 클래스내에서 선언되는 모든 함수에 들어가야 함
        print("생성자")

s1 = Student()  # 객체생성 -> 생성자를 호출 init__
s1.__init__()   # 강제로 생성자를 명시적으로 실행하여도 동일한 결과

print("#"+"-"*20+"#")

# 3.2 생성자의 역할
# 인스턴스 변수를 초기화하는 역할을 할 수 있다.

class Student:
    name = None
    age = 10

    # 생성자 역할 : 인스턴스 변수를 초기화하는 역할
    def __init__(self, n1, n2):  # 생성자
        print("생성자", n1, n2)
        self.name = n1
        self.age = n2

# 객체 생성과 동시에 파라미터를 통해 변수 초기화
s1 = Student("홍길동", 29)
print(s1.name, s1.age)
s2 = Student("이순신", 44)
print(s2.name, s2.age)

print("#"+"-"*20+"#")

# 4. 클래스 변수의 외부 접근
# 클래스내의 변수는 '__' 를 사용하여 외부 접근을 막고 함수를 통해 변수의 값을 얻거나 설정할 수 있다.
class Student:
    __name = None
    __age = None

    def __init__(self, n, a):
        if a < 100:
            self.__age = a
        self.__name = n

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, a):
        self.__age = a

    def setName(self, n):
        self.__name = n

s = Student("홍길동", 99)
s.setAge(89)
print(s.getName())
print(s.getAge())

print("#"+"-"*20+"#")

# 5. 속성 추가 및 삭제 (동적)

class Student:
    name = "홍길동"

s = Student()
print(s.name)

# 동적으로 멤버 추가
s.age = 10
print(s.age)

# 동적으로 멤버 삭제
del s.age

print("#"+"-"*20+"#")

# 6.1 부모 클래스와 자식 클래스
class Pet:
    name = None
    age = None

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def cry(self, action):
        print(action)

    def eat(self, action):
        print(action)

class Dog(Pet):  # 상속을 표현, Pet 부모클래스, Dog 자식클래스
    def __init__(self, n, a):
        # 부모에서 선언된 변수는 부모에서 초기화 하는게 좀 더 자연스럽다.
        # self.name = n
        # self.age = a
        super().__init__(n, a)

    def run(self):
        print("후다닥~")

class Cat(Pet):
    color = None  # color 는 Cat 에게만 있는 속성으로 가정

    def __init__(self, n, a, c):
        # 부모에서 선언된 변수는 부모에서 초기화 하는게 좀 더 자연스럽다.
        # self.name = n
        # self.age = a
        super().__init__(n, a)
        self.color = c

d = Dog("바둑이", 2)
d.eat("쩝쩝")
d.cry("멍멍")
d.run()

c = Cat("야옹이", 3, "black")
c.eat("쩝쩝")
c.cry("야옹")

print("#"+"-"*20+"#")

# 6.2 부모 클래스와 자식 클래스 : 오버라이딩 함수
class Pet:

    def eat(self):
        print("Pet.eat")

class Dog(Pet):

    # 부모의 함수를 자식이 재정의 : 오버라이딩 함수 (overriding function)
    # 목적 : 재사용
    def eat(self):
        print("Dog.eat!!!!!")

d = Dog()
d.eat()

print("#"+"-"*20+"#")

# 6.3 부모 클래스와 자식 클래스 : 다중 상속 가능 (자바는 단일 상속)
class Animal:
    name="홍길동"

class Person:
    age=10

class Man(Animal, Person):  # 다중 상속
    pass

m=Man()
print("다중 상속: " + m.name+"\t"+str(m.age))

print("#"+"-"*20+"#")

# 6.3 부모 클래스와 자식 클래스 : 변수 표현
# 변수명
# self.변수명
# super().변수명

class Parent:
    name="parent"

class Child(Parent):
    name="child"

    def info(self):
        name="info"
        print("variable :", name)
        print("variable :", self.name)
        print("variable :", super().name)

c = Child()
c.info()

print("#"+"-"*20+"#")

# 6.4 부모 클래스와 자식 클래스 : 추상클래스
# 추상 클래스 (abstrac class)
# -> 강제할 함수(추상함수)를 정의
# -> 추상함수는 아직 구현되지 않은 함수
# -> 추상 클래스는 객체 생성 불가
# -> 추상 클래스를 상속받은 자식 클래스를 이용하여 추상 클래스에 있는 함수 이용 가능
#     (단, 추상클래스의 추상메소드를 반드시 재정의(오버라이딩) 해야한다.)
# 목적 : 여러 클래스들안의 메서드를 강제해서 통일성

from abc import *

class Flyer(metaclass=ABCMeta):

    @abstractmethod
    def takeoff(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass

# f = Flyer()    # 객체 생성 안됨

class Bird(Flyer):
    def takeoff(self):
        print("Bird.takeoff")

    def fly(self):
        print("Bird.fly")

    def land(self):
        print("Bird.land")

class Airplane(Flyer):
    def takeoff(self):
        print("Airplane.takeoff")

    def fly(self):
        print("Airplane.fly")

    def land(self):
        print("Airplane.land")

b = Bird()
b.takeoff()
b.fly()
b.land()

a = Airplane()
a.takeoff()
a.fly()
a.land()

print("#"+"-"*20+"#")
