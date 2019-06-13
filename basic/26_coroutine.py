# cooperative routine
# 함수를 호출할때 함수내의 함수에 값을 전달하고 반환받는 방법


# 1. routine 에 값 보내기
def my_coroutine():
    while True:
        a = (yield)       # routine 밖에서 값을 받아옴
        print(a)

b = my_coroutine()
next(b)     # routine 의 yield 직전까지 실행

b.send(0)   # send 를 통해 routine 에 값을 보냄
b.send(1)   # send 를 통해 routine 에 값을 보냄
b.send(2)   # send 를 통해 routine 에 값을 보냄

print("#"+"-"*20+"#")

# 2. routine 값 받아오기
def my_coroutine():
    c = 0
    while True:
        a = (yield c)       # routine 밖에서 값을 받아옴
        c = a+1

b = my_coroutine()
next(b)            # routine 의 yield 직전까지 실향

print(b.send(0))   # send 를 통해 routine 에 값을 보냄
print(b.send(1))   # send 를 통해 routine 에 값을 보냄
print(b.send(2))   # send 를 통해 routine 에 값을 보냄

print("#"+"-"*20+"#")

