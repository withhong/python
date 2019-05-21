# 프로그램 특징
# 정적 : 변수
# 동적 : 데이터 조작처리 등 ... -> 함수(메소드)
#
# 함수의 종류
# 사용자 정의 함수
# 시스템 정의 함수 : 시스템이 미리 만든 함수 (range, str, int, ...)
#
# 함수의 특징
# 함수는 반드시 호출해야 실행된다. 함수명()
# 함수영역의 작업이 끝나면 반드시 돌아온다. (return) return 은 일반적으로 생략을 많이 함
# 함수 기능 정의가 아직 안되어 있는 경우에는 pass 를 이용한다.
# def my_func():
#     pass
#
# 함수의 형태
# 1. 파라미터(혹은 argument) 없고, 리턴값 없는 형태
# 2. 파라미터(혹은 argument) 있고, 리턴값 없는 형태
# 3. 파라미터(혹은 argument) 없고, 리턴값 있는 형태
# 4. 파라미터(혹은 argument) 있고, 리턴값 있는 형태

# 1. 파라미터 없고, 리턴값 없는 형태

def my_func():
    print("hello")
    #return  # 생략 가능

print("함수 호출 전")
my_func()   # 함수 호출
print("함수 호출 후")

print("#"+"-"*20+"#")

# 2. 파라미터 있고, 리턴값 없는 형태
# 함수 호출시 파라미터 갯수와 파라미터 변수 갯수가 반드시 일치해야 한다.

def my_func(n): # worker 함수 : 실제 일을 하는 함수
    print("hello", n)
    #return

print("함수 호출 전")
my_func(10)     # caller 함수
print("함수 호출 후")

print("#"+"-"*20+"#")

# 3. 파라미터 없고, 리턴값 있는 형태
# return 값이 없을 때는 return 생략가능

def my_func():
    print("hello")
    return 100

print("함수 호출 전")
b = my_func()
print(b)
print("함수 호출 후")

print("#"+"-"*20+"#")

# 일반적인 프로그램 언어에서 리턴값은 하나이지만 파이썬에서는 여러개도 가능

def my_func():
    print("hello")
    return 100,200

print("함수 호출 전")
a, b = my_func()
print(a,b)
print("함수 호출 후")

print("#"+"-"*20+"#")

# 4. 파라미터 있고, 리턴값 있는 형태

def my_func(n1,n2):
    print("hello")
    return n1+n2

print("함수 호출 전")
a = my_func(10,20)
print(a)
print("함수 호출 후")

print("#"+"-"*20+"#")

# 5. return : 돌아올때 사용, 일반적인 결과값 return
def my_func(n):
    mesg = "홀수" # 초기값을 주는 형태
    if n%2 == 0:
        mesg = "짝수"
    return mesg

print("함수 호출 전")
a = my_func(7)
print(a)
print("함수 호출 후")

print("#"+"-"*20+"#")

# 6. return : 함수 실행시 중간에 돌아올때도 사용 가능
def my_func(n):
    print("hello1")
    if n==10 : return
    print("hello2")

print("함수 호출 전")
my_func(10)
print("함수 호출 후")

print("함수 호출 전")
my_func(100)
print("함수 호출 후")

print("#"+"-"*20+"#")

# 7. 일급객체 (first-class) - 함수는 데이터로 인식, 즉 데이터가 위치할 수 있는 곳에 사용될 수 있음
# (1) 함수를 변수에 저장가능
# (2) 함수호출시 파라미터값으로 함수 사용 가능
# (3) 함수호출시 함수의 리턴값으로 함수 사용 가능

# 7.1 함수를 변수에 저장가능
def my_func():
    print("my_func")

print(my_func)
n = my_func     # 함수를 변수에 지정
print(n)

my_func()       # 함수 호출
n()             # 함수 호출

print("#"+"-"*20+"#")

# 7.2 일급객체 : 함수호출시 파라미터값으로 함수 사용 가능
# call back 함수 : 이벤트 처리시 주로 사용
# call back : 사용자가 호출한 함수가 아니고 시스템이 호출한 함수
def my_func_a():
    print("my_func_a")

def my_func_b():
    print("my_func_b")

def my_func_c(n):
    n()  # 시스템 호출

my_func_c(my_func_a)  # 사용자 호출
my_func_c(my_func_b)  # 사용자 호출

print("#"+"-"*20+"#")

# 7.3 일급객체 : 함수호출시 함수의 리턴값으로 함수 사용 가능
def my_func_a():
    print("my_func_a")

def my_func_b():
    return my_func_a

m = my_func_b()
m()

print("#"+"-"*20+"#")

# 8. 함수와 변수
m = 10  # 전역 변수 (함수안과밖에서 사용 가능)

def my_func():
    n = 100  # 지역 변수 (함수안에서만 사용 가능)
    print("전역변수 m 함수안:"+ str(m))
    print("지역변수 n 함수안:"+ str(n))

my_func()
print("전역변수 m 함수밖:"+ str(m))
#print("지역변수 n 함수밖:"+ str(n))   # 지역 변수는 함수밖에서 사용 안됨

print("#"+"-"*20+"#")

# 9. 함수와 파라미터

# 9.1 함수 호출시 반드시 갯수가 일치
def my_func(n):
    print(n)

my_func(10)

print("#"+"-"*20+"#")

# 9.2 함수 호출시 파라미터값에 디폴트값을 줄 수 있다.
def my_func(n1, n2=200):
    print(n1, n2)

my_func(100)

print("#"+"-"*20+"#")

# 9.3 함수 호출시 파라미터값 맵핑 방법
def my_func(n1, n2):
    print(n1, n2)

my_func(200, 100)           # 순서로 맵핑
my_func(n2=100, n1=200)     # 이름으로 맵핑

print("#"+"-"*20+"#")

# 9.4 파라미터 갯수가 일치하지 않는 경우 : 가변인자
# 파라미터 갯수를 정확히 모를때 유용
def my_func(*n):
    print(n)  # tuple 로 처리 (packing)
    for i in n:
        print("값:" + i)

my_func("A", "B")
my_func("A", "B", "C")
my_func("A")

print("#"+"-"*20+"#")

# 9.5 packing
def my_func(x, *n):
    print(x, n)  # tuple 로 처리 (packing)
    for i in n:
        print("값>>>:" + i)

my_func("A1", "B1")
my_func("A2", "B2", "C2")
my_func("A3")

print("#"+"-"*20+"#")

# 9.6 * 이용한 집합자료를 unpacking 해서 따로따로 변수 저장 가능
def my_func(n, m, p):
    print(n, m, p)

my_func(*[9, 8, 7])  # list
my_func(*{9, 8, 7})  # set
my_func(*(9, 8, 7))  # tuple

def my_func(n, m, *p):
    print(n, m, p)

my_func(*[9, 8, 7])             # list
my_func(*{9, 8, 7, 6, 5})       # set
my_func(*(9, 8, 7, 10, 20, 30)) # tuple

print("#"+"-"*20+"#")

# 9.7 dict 의 packing : **

def my_func(**n):
    print(n)

my_func(name="홍길동", age="20")  # key:value 쌍으로 dict 로 packing

def my_func(x, y, **n):
    print(x, y, n)

my_func(10, 20, name="홍길동", age="20")  # key:value 쌍으로 dict 로 packing

print("#"+"-"*20+"#")