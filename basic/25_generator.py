# generator
# iterator 를 생성해주는 함수
# 함수내에서 yield 명령으로 표현되며, 별도로 __iter__, __next__, __getitem__ 등의 함수를 만들 필요가 없다.

# 1. generator
def my_generator():
    yield 0
    yield 1
    yield 2

for i in my_generator():
    print("my_generator :", i)

# generator 가 __iter__ 있는지 확인
print("my_generator :", dir(my_generator()))

print("#"+"-"*20+"#")

# next 함수 사용
def my_generator():
    yield 0
    yield 1
    yield 2

a = my_generator()

print("my_generator next :", next(a))
print("my_generator next :", next(a))
print("my_generator next :", next(a))

print("#"+"-"*20+"#")

# 2. generator 의 예외 그리고 return
def my_generator():
    yield 0
    yield 1
    yield 2

a = my_generator()

print("my_generator next :", next(a))
print("my_generator next :", next(a))
print("my_generator next :", next(a))
#print("my_generator next :", next(a))   # 횟수를 넘어가면 동일하게 StopIteration 발생

print("#"+"-"*20+"#")

# return 명령을 통해 원하는 메시지 출력 가능
def my_generator():
    yield 0
    yield 1
    yield 2
    return "횟수 초과"  # StopIteration 과 함께 메시지 출력

a = my_generator()

print("my_generator next :", next(a))
print("my_generator next :", next(a))
print("my_generator next :", next(a))
# print("my_generator next :", next(a))   # 횟수를 넘어가면 동일하게 StopIteration 발생

print("#"+"-"*20+"#")

# 3. yield 와 함수
def my_generator(a):
    for i in a:
        yield i.upper()

a = ["a", "b", "c"]
for i in my_generator(a):
    print("my_generator :", i)

print("#"+"-"*20+"#")

# 4. yield, from
def my_generator():
    a = [10,20,30]
    for i in a:
        yield i

a = my_generator()

print("my_generator from :", next(a))
print("my_generator from :", next(a))
print("my_generator from :", next(a))

print("#"+"-"*20+"#")






