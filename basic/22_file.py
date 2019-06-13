# IO
# 입력(input) -> 파이썬 -> 출력(output)
# 키보드                   모니터
# 파일                     파일
# 네트워크

# (1) 표준 입출력
# 표준 입력: 키보드로 입력 -> input())
# 표준 출력: 모니터에 출력 -> print(값)

# (2) 파일 입출력 (open)
# 파일출력 -> mode 는 w, 파일이 없으면 자동생성, 기본적으로 덮어쓰기
# 파일출력 -> mode 는 a, 파일이 없으면 자동생성, 추가됨

# 1. 파일 출력
# 현재 작업 디렉토리
import os
print(os.getcwd())  # 현재 작업 디렉토리

try:
    # f = open("C:\\sample.txt", "a")
    # f = open(os.getcwd() + r"\sample_num.txt", "a")
    f_num = open(os.getcwd() + r"\sample_num.txt", "w")
    f_kor = open(os.getcwd() + r"\sample_kor.txt", "w")
    f_eng = open(os.getcwd() + r"\sample_eng.txt", "w")

    for i in range(10):
        data = str(i)+"\n"
        f_num.write(data)

    for i in ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]:
        data = i+"\n"
        f_kor.write(data)

    for i in ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        data = i+"\n"
        f_eng.write(data)

except Exception as e:
    print("파일쓰기 예외 메시지", e)

finally:
    f_num.close()
    f_kor.close()
    f_eng.close()

print("종료")

#help(open)

print("#"+"-"*20+"#")

# 2.1 파일읽기 : readline()
# 한줄만 읽음
# import os
f_num = open(os.getcwd() + r"\sample_num.txt", "r")
line = f_num.readline()
print("readline :", line)
f_num.close()

print("#"+"-"*20+"#")

# 파일 전체를 읽기 위해서는 반복문 필요
f_num = open(os.getcwd() + r"\sample_num.txt", "r")
while True:
    line = f_num.readline()
    # 파일 끝 break
    if not line : break # 마지막줄은 "", False 로 처리
    print("readline 반복 :", line)
f_num.close()

print("#"+"-"*20+"#")

# 파일의 끝 (논리값 인식)
# 논리값 : True False
# True 로 처리
#   10
#   "AA"
# False로 처리
#   0
#   "" # 빈문자열
#   None

if 0:
    print("0 -> True")
else:
    print("0 -> False")

if None:
    print("None -> True")
else:
    print("None -> False")

if "":
    print("\"\" -> True")
else:
    print("\"\" -> False")

if 1:
    print("1 -> True")
else:
    print("1 -> False")

if "AA":
    print("\"AA\" -> True")
else:
    print("\"AA\" -> False")

print("#"+"-"*20+"#")

# 2.2 파일읽기 : readlines()
# list 로 반환
f_num = open(os.getcwd() + r"\sample_num.txt", "r")
lines = f_num.readlines()
print("readlines :", lines)
f_num.close()

print("#"+"-"*20+"#")

# list 로 반환
f_num = open(os.getcwd() + r"\sample_num.txt", "r")
lines = f_num.readlines()
for line in lines:
    print("readlines :", line)
f_num.close()

print("#"+"-"*20+"#")

# 2.3 파일읽기 : read()
# 한꺼번에 모두 읽어서 전체를 문자열로 반환, 반복문 필요없음
f_num = open(os.getcwd() + r"\sample_num.txt", "r")
data = f_num.read()
print("read :", data)
f_num.close()

print("#"+"-"*20+"#")

f_kor = open(os.getcwd() + r"\sample_kor.txt", "r")
#f_kor = open(os.getcwd() + r"\sample_kor.txt", 'r', encoding='utf-8')   # 한글 encoding 때문에 문제가 생기는 경우 명시적으로 encoding 을 적어주어야 한다.
data = f_kor.read()
print("read :", data)
f_kor.close()

print("#"+"-"*20+"#")

f_eng = open(os.getcwd() + r"\sample_eng.txt", "r")
data = f_eng.read()
print("read :", data)
f_eng.close()

print("#"+"-"*20+"#")

# 3. with 문
# 자동으로 close() 처리
# with open("파일명", 'r') as f:
# import os

try:
    with open(os.getcwd() + r"\sample_num.txt", 'r', encoding='utf-8') as f_num:
        print("with :", f_num.read())
except Exception as e:
    print("with : error", e)

print("#"+"-"*20+"#")

# 4. 라인 수 세기
with open(os.getcwd() + r"\sample_kor.txt", "r") as f:
    lines = f.readlines()
    for cnt, lines in enumerate(lines, 1):
        # print(cnt, lines)
        pass
    print("line number :", cnt)

print("#"+"-"*20+"#")
