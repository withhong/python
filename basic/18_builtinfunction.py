# built in function (시스템 정의 함수)

# 1. abs
# 2. all
# 3. any
# 4. chr
# 5. dir
# 6. divmod
# 7. enumerate
# 8. eval
# 9. filter
# 10. hex
# 11. id
# 12. input
# 13. int
# 14. isinstance
# 15. len
# 16. list
# 17. map
# 18. max
# 19. min
# 20. oct
# 21. open
# 22. ord
# 23. pow
# 24. range
# 25. round
# 26. sorted
# 27. str
# 28. sum
# 29. tuple
# 30. type
# 31. zip

# help(__builtins__)

# 1. abs
# 절대값 계산
print("abs : ", abs(1))
print("abs : ", abs(-1))
print("abs : ", abs(1.5))
print("abs : ", abs(-1.5))

print("#"+"-"*20+"#")

# 2. all
# 반복가능한 datatype 을 입력으로 받아서 모두 참이면 True, 하나라도 거짓이 있으면 False 를 리턴한다.
print("all : ", all([0]))
print("all : ", all([1]))
print("all : ", all([10, 20, 30]))
print("all : ", all({10, 20, 30}))
print("all : ", all((10, 20, 30)))
print("all : ", all([0, 20, 30]))
print("all : ", all({0, 20, 30}))
print("all : ", all((0, 20, 30)))
print("all : ", all([(3>2), (5>1), (10>7)]))
print("all : ", all([(3>2), (5>1), (10<7)]))

print("#"+"-"*20+"#")

# 3. any
# 반복가능한 datatype 을 입력으로 받아서 하나라도 참이면 True, 모두 거짓이면 False 를 리턴한다.
print("any : ", any([0]))
print("any : ", any([1]))
print("any : ", any([0, 20, 30]))
print("any : ", any({0, 20, 30}))
print("any : ", any((0, 20, 30)))
print("any : ", any([0, 0, 0]))
print("any : ", any({0, 0, 0}))
print("any : ", any((0, 0, 0)))
print("any : ", any([(3>2), (5>1), (10>7)]))
print("any : ", any([(3>2), (5>1), (10<7)]))
print("any : ", any([(3<2), (5<1), (10<7)]))

print("#"+"-"*20+"#")

# 4. chr
# 아스키 값(0~127)을 해당하는 문자로 반환
print("ASCII(48)", chr(48))
print("ASCII(97)", chr(97))

print("#"+"-"*20+"#")

# 5. dir
# datatype 이 가지는 함수(메소드)나 변수를 반환
print("dir int :", dir(10))
print("dir str :", dir('10'))
print("dir list :", dir([10,20,30]))
print("dir set :", dir({10,20,30}))
print("dir tuple :", dir((10,20,30)))

print("#"+"-"*20+"#")

# 6. divmod
# 몫과 나머지를 함께 반환 (tuple)
print("몫과 나머지 :", divmod(10, 3))

print("#"+"-"*20+"#")

# 7. enumerate
# 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
m = enumerate([10,20,30])
print("enumerate :", dict(m))

# for 문
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):  # 두번째 파라미터는 세기 시작하는 첫번째 숫자, 기본값은 0
    print("enumerate :", c, value)

print("#"+"-"*20+"#")

# 8. eval
# 실행 가능한 문자열을 입력으로 받아서 결과값을 반환
print("eval :", "1+2")
print("eval :", "1<2")
print("eval :", eval("1+2"))
print("eval :", eval("1<2"))

print("#"+"-"*20+"#")

# 9. filter
# filter 함수는 첫번째 파라미터로 함수 이름, 두번째 파라미터로 반복 가능한 자료형
# 반복하여 함수를 실행하여 참인 것만 반화

def check(a):
    return a > 0

print("filter :", list(filter(check, [0, 1, 2, -1, -2])))

print("#"+"-"*20+"#")

# 10. hex
# 정수값을 16진수로 변한
print("hex :", hex(8))
print("hex :", hex(16))

print("#"+"-"*20+"#")

# 11. id
# id(object)는 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴
a = b = 7
print("id :", id(a))
print("id :", id(b))
print("id :", id(7))

print("#"+"-"*20+"#")

# 12. input
# 사용자의 입력 처리 가능
# m = input("이름 입력: ")
# print("input :", m)

# 13. int
# 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴
print("int :", int('7'))
print("int :", int(7.0))
# print("int :", int('7.0')) # 소수점 있는 형태의 문자열은 안됨
print(int("10") + 10)

print("#"+"-"*20+"#")

# 14. isinstance
# 인스턴스와 클래스 이름을 받아 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴
class my_class:
    pass
a = my_class()
b = 7

print("isinstance :", isinstance(a, my_class))
print("isinstance :", isinstance(b, my_class))

print("#"+"-"*20+"#")

# 15. len
# 입력값의 길이를 반환
# 한글의 경우 파이썬2에서는 바이트, 파이썬3에서는 글자수를 반환
print("len :", len("ABC"))
print("len :", len([10,20,30]))
print("len :", len({"A":10,"B":20,"C":30}))
print("len :", len("홍길동"))

print("#"+"-"*20+"#")

# 16. list
# list 로 변환
print("list :", list({10,20,30}))

print("#"+"-"*20+"#")

# 17. map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받아 결과 반환
def my_func(a):
    return a+1

a1, a2, a3 = map(my_func, [10,20,30])
print("map :", list([a1, a2, a3]))
print("map :", list(map(my_func, [10,20,30])))

print("#"+"-"*20+"#")

# 18. max
# 최대값 반환
print("max :", max([10,20,30]))
print("max :", max({10,20,30}))
print("max :", max((10,20,30)))

print("#"+"-"*20+"#")

# 19. min
print("min :", min([10,20,30]))
print("min :", min({10,20,30}))
print("min :", min((10,20,30)))

print("#"+"-"*20+"#")

# 20. oct
# 정수값을 8진수로 변한
print("oct :", oct(8))
print("oct :", oct(16))

print("#"+"-"*20+"#")

# 21. open
# 파일 입출력
# open(filename, [mode])
# mode : w, r, a, b
#fread = open("read_mode.txt", 'r')

print("#"+"-"*20+"#")

# 22. ord
# 아스키 값 반환
print("ord :", ord('a'))
print("ord :", ord('b'))

print("#"+"-"*20+"#")

# 23. pow
# pow(x, y)는 x의 y 제곱한 결과값
print("pow :", pow(2, 3))
print("pow :", pow(3, 2))

print("#"+"-"*20+"#")

# 24. range
# range([start,] stop [,step])
print("range :", list(range(10)))
print("range :", list(range(1,5)))
print("range :", list(range(1,10,2)))
print("range :", list(range(10,1,-1)))

print("#"+"-"*20+"#")

# 25. round
# round(number[, ndigits])
print("round :", round(1.3))
print("round :", round(1.5))
print("round :", round(1.378, 2))

print("#"+"-"*20+"#")

# 26. sorted
# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 반환
print("sorted : ", sorted("hello"))
print("sorted : ", sorted(["h","e","l","l","o"]))
print("sorted : ", sorted([30, 20, 10]))
print("sorted : ", sorted((30, 20, 10)))

print("#"+"-"*20+"#")

# 27. str
# 문자열 형태로 객체를 변환
print("str :", str(7))
print("str :", str("Hello").upper())
print(str(10) + "값")

print("#"+"-"*20+"#")

# 28. sum
print("sum :", sum([10, 20, 30]))
print("sum :", sum({10, 20, 30}))
print("sum :", sum((10, 20, 30)))

print("#"+"-"*20+"#")

# 29. tuple
print("tuple :", tuple([10,20,30]))

print("#"+"-"*20+"#")

# 30. type
# datatype 반환
print("type :", type("A"))
print("type :", type(7))

print("#"+"-"*20+"#")

# 31. zip
# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할
print("zip :", list(zip([1, 2, 3], [4, 5, 6])))
print("zip :", list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print("zip :", list(zip("abc", "def")))
print("zip :", dict(zip([1, 2, 3], [4, 5, 6])))

print("#"+"-"*20+"#")

# 추가 1. 정수를 실수로 (float)
print("float :", float(10))

print("#"+"-"*20+"#")

# 추가 2. 랜덤값 얻기
import random

n1 = random.random()  # 0이상 1미만의 실수값(float)
print("random :", n1)

n2 = random.randrange(1, 6)  # 1~5까지 정수값
print("random :", n2)

n3 = random.randint(1, 6)  # 1~6까지 정수값
print("random :", n3)

a = ['a', 'b', 'c', 'd']
b = random.choice(a)  # 사용자 값에서 랜덤하게 값 얻기
print("random :", b)

random.shuffle(a)  # shuffle
print("random :", a)

print("#"+"-"*20+"#")
