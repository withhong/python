# 1. 조건문 (단일 if, if~else, 다중 if, 중첩 if, 3항 연산자)
# 조건문 수행시 코드는 ':'와 indent 를 통해 구분

# 단일 if 문

print("A")
if 1:
    print("B")
print("C")

print("#"+"-"*20+"#")

# if~else 문

print("A")
if 1:
    print("B")
else:
    print("C")

print("#"+"-"*20+"#")

# 다중 if 문

# 입력을 받으면 문자열이다.
# 문자열 -> 정수 : int
# 정수 -> 문자열 : str
#n = int(input("점수입력:"))
n = 100
if (n>90):
    print("A")
elif (n>80):
    print("B")
else:
    print("C")

print("#"+"-"*20+"#")

# 중첩 if 문
n = 99

if (n>90):
    print("A")
else:
    if (n>80):
        print("B")
    else:
        print("C")

print("#"+"-"*20+"#")

# 3항 연산자
# 보통은 (조건식)? 참일때 : 거짓일때
# python 은 참일때 if (조건식) else 거짓일때

a = 6
result = 100 if a==61 else 200
print(result)

print("#"+"-"*20+"#")
