# built in function (시스템 정의 함수)

# 1. 합계 (sum)
print(sum([10, 20, 30]))
print(sum({10, 20, 30}))
print(sum((10, 20, 30)))

print("#"+"-"*20+"#")

# 2. 문자를 정수로 (int), 정수를 문자로 (str)
print(int("10") + 10)
print(str(10) + "값")

print("#"+"-"*20+"#")

# 3. 정수를 실수로 (float)
print(float(10))

print("#"+"-"*20+"#")

# 4. 문자로 표현된 수식을 실행하는 함수 (eval)
print('4+3')
print('4>3')
print(eval('4+3'))
print(eval('4>3'))

print("#"+"-"*20+"#")

# 5. 랜덤값 얻기
import random

n1 = random.random()  # 0이상 1미만의 실수값(float)
print(n1)

n2 = random.randrange(1, 6)  # 1~5까지 정수값
print(n2)

n3 = random.randint(1, 6)  # 1~6까지 정수값
print(n3)

a = ['a', 'b', 'c', 'd']
b = random.choice(a)  # 사용자 값에서 랜덤하게 값 얻기
print(b)

random.shuffle(a)  # shuffle
print(a)

print("#"+"-"*20+"#")