# 예외 (exception) -> 통상적으로 에러
#     예외 발생 -> 프로그램이 비정상적으로 처리됨
#     예외 처리 -> 발생된 예외를 처리하는 것이 아니고 정상종료 하도록 유도
#     예외 처리 방법
#                예외클래스(계층구조)를 제공해서 처리, (파이썬 문서(python.org) 에서 hierarchy 볼 수 있음 (library reference))
#                try ~ except 문장
#                finally 문

# 1. 예외 발생
n1 = 10
n2 = n1/5
#n2 = n1/0    # 실행시키면 에러 발생 (ZeroDivisionError: division by zero)
print("실행결과:", n2)
print("정상종료")

print("#"+"-"*20+"#")

# 2. 예외 처리 (try ~ except)
try:
    n1 = 10
    #n2 = n1/2
    n2 = n1/0
    print("실행결과:", n2)

# ZeroDivisionError 의 hierarchy
# Exception > ArithmeticError > ZeroDivisionError
except ZeroDivisionError as e:    # 해당하는 에러종류를 써줘야 함. (정확하게 종류를 써주는 것이 좋음)
# except ArithmeticError as e:      # hierarchy 에서 상위는 사용가능 (다형성)
# except Exception as e:            # hierarchy 에서 상위는 사용가능 (다형성)
# except TabError as e:             # hierarchy 가 완전 다르기 때문에 동작안됨
    print("예외처리 코드", e)
# except:
#     print("예외처리 코드")
print("정상종료")

print("#"+"-"*20+"#")

# 3. 예외 처리 (try ~ except, finally)
try:
    n1 = 10
    #n2 = n1/2
    n2 = n1/0
    print("실행결과:", n2)

# ZeroDivisionError 의 hierarchy
# Exception > ArithmeticError > ZeroDivisionError
except ZeroDivisionError as e:    # 해당하는 에러종류를 써줘야 함. (정확하게 종류를 써주는 것이 좋음)
    print("예외처리 코드", e)
finally:
    print("finally : 반드시 수행")
    print("finally : 파일, DB 입출력(외부자원)의 close 작업") # 예외동작을 하든 안하든 동작되는 코드에는 외부자원을 사용하는 부분의 close 작업을 넣어준다.
print("정상종료")

print("#"+"-"*20+"#")

# 4. 예외 처리 (try ~ except, finally, 서로 다른 exception 이 있는 경우)
# 명시적으로 각각 예외처리를 하고 마지막에는 전체 예외에 대한 처리를 넣어준다.

try:
    n1 = 10
    #n2 = n1/2
    n2 = n1/0
    print("실행결과:", n2)

except ZeroDivisionError as e:    # 해당하는 에러종류를 써줘야 함. (정확하게 종류를 써주는 것이 좋음)
    print("예외처리 코드", e)
except IndexError as e:
    print("예외처리 코드", e)
except Exception as e:
    print("예외처리 코드", e)
finally:
    print("finally : 반드시 수행")
    print("finally : 파일, DB 입출력(외부자원)의 close 작업") # 예외동작을 하든 안하든 동작되는 코드에는 외부자원을 사용하는 부분의 close 작업을 넣어준다.
print("정상종료")

print("#"+"-"*20+"#")

# 5. finally 문 사용 (except 없이)
# except 없이 try finally 만 사용할 수 있음
# 반드시 수행해야 하는 작업만 수행하겠다는 의미

print("프로그램 시작")
try:
    n = 10 / 2
    print("결과값", n)
finally:
    print("finally : 반드시 수행")
print("정상종료")

print("#"+"-"*20+"#")

# 6. 사용자 정의 예외
# 지금까지는 예외를 시스템이 발생시킴
# 사용자가 명시적으로 예외 발생시키고 처리 가능
# 사용자가 명시적으로 예외 발생시칸다는 것은 시스템이 발생시킨다는 의미. 즉, 문법적으로는 문제가 없음
# 개발자가 만든 프로그램에서 개발자가 지정한 특정 조건에 위배되었을 경우 강제적으로 예외 발생함
# raise 예외클래스명(mesg) -> 자바는 throw 예외클래스명(mesg)

# 사용자 정의 예외클래스
class UserException(Exception):  # 반드시 Exception 클래스를 상속받아야 함

    def __init__(self, mesg):
        self.mesg = mesg

#
import random

def randomValue():
    n = random.randrange(0, 2)
    print("6. 랜덤값 :", n)
    if n == 0:
        # 사용자 정의 예외클래스 이용
        raise UserException("랜덤값이 0: 예외발생")  # 클래스이름(값). 즉, 객체 생성과 동일
        # 기존 예외 이용 가능
        # raise ZeroDivisionError("랜덤값이 2: 예외발생")     # 클래스이름(값). 즉, 객체 생성과 동일

print("6. 프로그램 시작")
try:
    randomValue()
except ZeroDivisionError as e:
    print("6. 예외처리 코드", e)
except UserException as e:
    print("6. 예외처리 코드", e)
else:                           # 예외가 발생하지 않았을때를 위해서 'else'를 사용할 수 있다.
    print("6. 예외발생 안함")
print("6. 정상종료")

print("#"+"-"*20+"#")

# 7. 시스템이 발생시킨 예외를 사용자 정의 예외로 처리하는 방법
# 시스템이 발생한 에러 -> 영문자 에러 메시지가 출력됨
# 시스템이 발생한 에러 -> 사용자 정의 예외로 하여 한글로 된 에러 메시지 출력

# 사용자 정의 예외클래스
class UserException(Exception):  # 반드시 Exception 클래스를 상속받아야 함

    def __init__(self, mesg):
        self.mesg = mesg

#
def calc():
    try:
        n1 = 10
        n2 = n1 / 0
        print("7. 실행결과:", n2)
    except ZeroDivisionError as e:
        raise UserException("0으로 나눔: 예외발생")


print("7. 프로그램 시작")
try:
    calc()
except UserException as e:
    print("7. 예외처리 코드", e)
print("7. 정상종료")

print("#"+"-"*20+"#")

# 8. 사용자 정의 예외의 예제
# 랜덤값 생성하여 생성된 값이 특정값이면 예외 발생

# 사용자 정의 예외클래스
class UserException(Exception):  # 반드시 Exception 클래스를 상속받아야 함

    # def __init__(self, mesg):
    #     self.mesg = mesg

    def __init__(self):
        super().__init__("Check User Exception")

#
import random

def randomValue():
    n = random.randrange(0, 2)
    print("8. 랜덤값 :", n)
    if n == 1:
        # 사용자 정의 예외클래스 이용
        raise UserException  # 클래스이름(값). 즉, 객체 생성과 동일

print("8. 프로그램 시작")
try:
    randomValue()
except UserException as e:
    print("8. 예외처리 코드", e)
else:                           # 예외가 발생하지 않았을때를 위해서 'else'를 사용할 수 있다.
    print("8. 예외발생 안함")
print("8. 정상종료")

print("#"+"-"*20+"#")
