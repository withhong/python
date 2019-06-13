# decorator
# '@' 를 붙이며 @abstractmethod, @staticmethod, @classmethod 등이 모두 decorator


# 1. decorator
# simple function call
def my_func_1():
    print("my_func_1")

def my_func_2():
    print("my_func_2")

my_func_1()
my_func_2()

print("#"+"-"*20+"#")

# 함수 이름, 정보 표시
def func_exec(function):
    def wrapper():
        print("*****", "function name :", function.__name__, "start", "*****")
        function()
        print("*****", "function name :", function.__name__, "end", "*****")
    return wrapper

def my_func_1():
    print("my_func_1")

def my_func_2():
    print("my_func_2")

a = func_exec(my_func_1)
b = func_exec(my_func_2)

a()
b()

print("#"+"-"*20+"#")

# '@' 사용
def func_exec(function):
    def wrapper():
        print("*****", "function name :", function.__name__, "start", "*****")
        function()
        print("*****", "function name :", function.__name__, "end", "*****")
    return wrapper

@func_exec
def my_func_1():
    print("my_func_1")

@func_exec
def my_func_2():
    print("my_func_2")

my_func_1()
my_func_2()

print("#"+"-"*20+"#")

# 2. 파라미터 있고 반환값 있는 decorator
def func_exec(function):
    def wrapper(a, b):
        print("*****", "function name :", function.__name__, "start", "*****")
        c = function(a, b)
        print("*****", "function name :", function.__name__, "end", "*****")
        return c
    return wrapper

@func_exec
def my_func_1(a, b):
    return a + b

@func_exec
def my_func_2(a, b):
    return a - b

print(my_func_1(2, 1))
print(my_func_2(2, 1))

print("#"+"-"*20+"#")

# 3. tag 붙이기
def html_tag(tag):              # decorator 자체가 tag 라는 파라미터를 받음
    def decorator(func):        # 실제 decorator 역할을 하며 function 을 입력으로 받음
        def wrapper():          # 실제 함수는 파라미터가 없음 (hello)
            a = func()
            b = r"<{0}>{1}</{0}>".format(tag, a)
            return b
        return wrapper
    return decorator

a, b = ["A", "B"]

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())

print("#"+"-"*20+"#")
