# 문자열 (str)

# 1. slice
m = "대한민국"
print(m[0],m[1],m[2],m[3])
print(m[0:3])
print(m[0:4])
print(m[0:])
print(m[:4])
print(m[:])
print(m[:-1])   # 뒤에서부터 count
print(m[::-1])  # 문자열 전체에서 '1'씩 감소시키면서 가져옴. 즉, 문자열을 뒤집은 것과 같은 효과
print(''.join(reversed(m))) # reversed 와 join 을 이용하여 문자열 뒤집는 방법
print(m*2)

print("#"+"-"*20+"#")

# 2. 함수
print("문자열길이", len("Hello"))
print("특정문자포함갯수", "Hello".count('e'))
print("특정문자위치", "Hello".find('e'))
print("대문자", "Hello".upper())
print("소문자", "Hello".lower())
print("대소문자 swap", "Hello".swapcase())
print("특정문자로 시작하는지", "Hello".startswith("H"), "Hello".startswith("x"))
print("문자변경:", "Hello".replace("H", "A"))
print("문자변경:", "Hello".replace("l", "o",1))
print("구분자:", "aaa/bbb/ccc".split("/"))   # 반환값은 list
print("공백제거:", "           Hello         ".strip())
print("공백제거:", "           Hello         ".lstrip())
print("공백제거:", "           Hello         ".rstrip())
print("특정문자제거:", "           ,Hello.         ".strip(',.'))   # , .

import string
print("구두점제거     :", "           ,Hello.         ".strip(string.punctuation))            # 구두점
print("구두점제거     :", ",Hello.".strip(string.punctuation))            # 구두점 (공백이 없어야 제거됨)
print("구두점및공백제거:", "           ,Hello.         ".strip(string.punctuation + ' '))      # 구두점 + 공백
print("구두점및공백제거:", "           ,Hello.         ".strip().strip(string.punctuation))    # 구두점 + 공백
print(string.punctuation)

print("정렬:", "Hello".ljust(10))
print("정렬:", "Hello".rjust(10))
print("정렬:", "Hello".center(10))

print("#"+"-"*20+"#")

#help(str)
