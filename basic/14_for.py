# 1. 일반적인 for 문의 형태
for n in [1,2,3,4]:
    print("hello")
print("end")

print("#"+"-"*20+"#")

# 2. range 이용 : range(start:end) -> start ~ end-1
# range(n) : 0부터 n-1까지 반환
# range(m,n) : m 부터 n-1까지 반환
# range(m,n,s) : m 부터 n-1까지 반환, 증가는 s

for n in range(3):
    print(n)
print("end")

for n in range(1,3):
    print(n)
print("end")

for n in range(1,10,2):
    print(n)
print("end")

print("#"+"-"*20+"#")

#help(range)

# 3. 집합데이터의 반복문
# list
for n in [100,200,300]:
    print("list", n)
print("end")

# set
for n in {10,20,30}:
    print("set", n)
print("end")

# tuple
for n in (1,2,3):
    print("tuple", n)
print("end")

# dict 는 key 값이 기본으로 출력됨
for n in {'java':"웹", 'python':"분석"}: # dict
    print("dict", n)
print("end")

# 명시적으로 key 값 얻기
dict2 = {'java':"웹", 'python':"분석"}
for n in dict2.keys(): # dict
    print("dict key:", n)
print("end")

# 명시적으로 value 값 얻기
dict2 = {'java':"웹", 'python':"분석"}
for n in dict2.values(): # dict
    print("dict value:", n)
print("end")

# 명시적으로 key, value 한번에 tuple 형태로 얻기
dict2 = {'java':"웹", 'python':"분석"}
for n in dict2.items(): # dict
    print("dict item:", n)
print("end")

print("#"+"-"*20+"#")

# 3. 다른 형태의 반복문
# 일반적인 for 문
# for 변수1 in [데이터]:
#    문장

# 다른 형태의 반복문
# 변수2 = [문장 for 변수1 in 데이터]

for n in [10, 20, 30]:
    print(n)

n2=[]
for n1 in [10, 20, 30]:
    n2.append(n1+1)
print(n2)

n2 = [n1+1 for n1 in [10,20,30]]
print(n2)

print("#"+"-"*20+"#")
