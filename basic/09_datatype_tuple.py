# 1. tuple 생성 : 순서 있고 중복가능하고 수정안됨, 혼합데이터 가능
m = (10, 1, 3, 7, 2)
m = ()

# 2. 함수
m = (10, 1, 3, 7, 2)
print("길이: ", len(m))
print("포함갯수: ", (10, 1, 3, 7, 2).count(1))
print("특정위치: ", (10, 1, 3, 7, 2).index(10))
print("특정값 포함여부: ", 10 in (10, 1, 3, 7, 2))

print("#"+"-"*20+"#")

print("slice: ", m[0])
print("slice: ", m[0:2])
print("slice: ", m[0:])
print("slice: ", m[:3])
print("slice: ", m[:-1])
print("slice: ", m[:])

print("#"+"-"*20+"#")