# 모듈 : 함수나 변수 또는 클래스 들을 모아 놓은 파일로 다른 파이썬 프로그램에서 불러와 사용할수 있게끔 만들어짐

# 1. main 프로그램 알기

# __name__ 이 __main__ 인 경우, 시작하는 모듈 (main module)
print(__name__)

if __name__ == '__main__':
    print("main module : 시작점")
else:
    print("외부에 있는 파일을 import 된 모듈")

print("#"+"-"*20+"#")

# 2. main 에서 외부 파일 찾을 때의 경로 확인하는 방법
import sys

#print(sys.path)
for i in range(len(sys.path)):
    print("path 확인 :", sys.path[i])

print("#"+"-"*20+"#")

# 파이썬 프로그램내에서 경로 추가 하는 방법
# sys.path.append("C:/경로")
# for i in range(len(sys.path)):
#     print("path 확인 :", sys.path[i])
#
# print("#"+"-"*20+"#")

# 3. 다른 모듈을 불러서 사용하는 방법

# 1) import 패키지명.모듈명(파일명)

import basic.submodule_0
import basic.submodule_1  # 파일이 2개면 둘다 import 해야함

if __name__ == "__main__":
    print("멤버 확인(submodule_0) :", dir(basic.submodule_0))  # import 한 모듈의 멤버
    print("모듈명 확인(submodule_0) :", basic.submodule_0.__name__)  # import 한 모듈의 이름
    print("모듈명 확인(submodule_0) :", basic.submodule_0.__file__)  # import 한 모듈의 경로
    print("접근(submodule_0) :", basic.submodule_0.a)  # import 한 모듈의 변수 접근
    basic.submodule_0.info()  # import 한 모듈의 함수 호출
    stu = basic.submodule_0.Student()  # import 한 모듈의 클래스 이용

    print("접근(submodule_1) :", basic.submodule_1.b)  # import 한 모듈의 변수 접근

print("#"+"-"*20+"#")

# 2) from 패키지명 import 모듈명(파일명)

# from basic import submodule_0, submodule_1
from basic import (submodule_0, submodule_1)

if __name__ == "__main__":
    # 사용할 때 패키지 이름을 따로 쓰지 않아도 된다.
    print("멤버 확인(submodule_0) :", dir(submodule_0))  # import 한 모듈의 멤버
    print("모듈명 확인(submodule_0) :", submodule_0.__name__)  # import 한 모듈의 이름
    print("모듈명 확인(submodule_0) :", submodule_0.__file__)  # import 한 모듈의 경로
    print("접근(submodule_0) :", submodule_0.a)  # import 한 모듈의 변수 접근
    submodule_0.info()  # import 한 모듈의 함수 호출
    stu = submodule_0.Student()  # import 한 모듈의 클래스 이용

    print("접근(submodule_1) :", submodule_1.b)  # import 한 모듈의 변수 접근

print("#" + "-" * 20 + "#")

# 3) from 패키지명.모듈명(파일명) import 멤버

# from basic.submodule_0 import a, info, Student
from basic.submodule_0 import *

if __name__ == "__main__":
    # 사용할 때 패키지 이름, 모듈이름을 따로 쓰지 않아도 된다.
    print("접근(submodule_0) :", a)  # import 한 모듈의 변수 접근
    info()  # import 한 모듈의 함수 호출

    stu = Student()  # import 한 모듈의 클래스 이용

# from 에서 어디까지 기술했느냐에 따라 사용할때 패키지 이름, 모듈이름을 사용하는지가 달라진다.

print("#" + "-" * 20 + "#")

# 3. pip
# pip search package_name : package 검색
# pip install package_name : 설치
# pip install package_name=version : 설치
# pip list : 설치된 package list 추력
# pip uninstall package_name : 삭제

# 4. 패키지
# 모듈 : 변수, 함수, 클래스 등을 모아 놓은 파일
# 패키지 : 여러 모듈을 묶어 놓은 것

# 1. 패키지 생성
# 패키지는 폴더로 구성
# (1) 만들고 싶은 패키지의 이름으로 폴더 생성
# (2) __init__.py 파일 생성
#     이 파일은 내용을 비워도 된다.
#     폴더(디렉토리) 가 패키지로 인식되도록하는 역할
#     패키지를 초기화 하는 역할
# (3) 패키지내에 모듈 생성

# 2. 패키지 사용
# (1) import 패키지.모듈
#     패키지.모듈.함수()
#     패키지.모듈.변수
# (2) import 패키지
#       이렇게 사용하기 위해서는 __inin__.py 파일 수정 필요
#       from . import 모듈 이름     # 현재 패키지에서 모듈을 가져온다는 의미
#       from . import *            # 현재 패키지에서 모듈, 클래스, 변수 등 모든 것을 가져온다는 의미

#       __all__ 명령을 __init__.py 에 사용하면 * 로 가져오는 것들을 조정할 수 있다. * 로 가져오더라도 일부는 비공개 될 수 있다.
#       __all__ = ['AAA', 'BBB']   # 함수 AAA 와 BBB 만 공개하겠다는 의미


