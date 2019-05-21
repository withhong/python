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
print("공백제거:", "           Hello         ".strip())
print("공백제거:", "           Hello         ".lstrip())
print("공백제거:", "           Hello         ".rstrip())
print("문자변경:", "Hello".replace("H", "A"))
print("문자변경:", "Hello".replace("l", "o",1))
print("구분자:", "aaa/bbb/ccc".split("/"))   # 반환값은 list

print("#"+"-"*20+"#")

#help(str)
