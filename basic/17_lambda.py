# 특별한 함수
#
# 람다 함수 (lambda) -> 함수의 다른 표현식
#                   -> 함수가 실행해야 하는 문장이 단일 문장일때만 가능

# 1. 파라미터 없고 리턴값 없는 형태
def my_func_1():
    print("hello my_func_1")
my_func_1()

my_func_2=lambda : print("hello my_func_2")
my_func_2()

print("#"+"-"*20+"#")

# 2. 파라미터 있고 리턴값 없는 형태
def my_func_1(n1,n2=100):
    print("hello my_func_1",n1,n2)
my_func_1(10,20)

my_func_2=lambda n1,n2=100: print("hello my_func_2",n1,n2)
my_func_2(10,20)

print("#"+"-"*20+"#")

# 3. 파라미터 없고 리턴값 있는 형태
def my_func_1():
    return 100
m1 = my_func_1()
print(m1)

my_func_2=lambda : 100 # return 은 생략
m2 = my_func_2()
print(m2)

print("#"+"-"*20+"#")

# 4. 파라미터 있고 리턴값 있는 형태
def my_func_1(n1,n2):
    return n1+n2
m1 = my_func_1(1,2)
print(m1)

my_func_2=lambda n1,n2 : n1+n2 # return 은 생략
m2 = my_func_2(1,2)
print(m2)

print("#"+"-"*20+"#")

# 5. 가변인자
def my_func_1(n1, *n2, **n3):
    print(n1,n2,n3)
my_func_1(10,"홍",20, name="홍길동", age=20)

my_func_2 = lambda n1, *n2, **n3: print(n1,n2,n3)
my_func_2(10,"홍",20, name="홍길동", age=20)

print("#"+"-"*20+"#")
