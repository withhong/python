# 1. set 생성 (순서 없기때문에 중복 안됨, 수정 가능, 혼합 데이터 가능)
m = {10,7,1,2,3}
m = {}              # 빈 set 생성 가능

# 2. 함수
# 추가
m = {10,7,1,2,3}
m.add(8)
print("add 함수: ", m)
m.add((77,66))  # add tuple
print("add 함수: ", m)

print("#"+"-"*20+"#")

# 삭제
# discard 는 데이터 없어도 에러안남, remove 는 에러
m = {10,7,1,2,3}
m.discard(3)
print("discard 함수: ", m)
m.discard(5) # 없는 값을 해도 에러안남
print("discard 함수: ", m)

m = {10,7,1,2,3}
m.remove(3)
print("remove 함수: ", m)
#m.remove(5) # 없는 값을 하면 에러
print("remove 함수: ", m)

print("#"+"-"*20+"#")

# 3. 기타 함수
m = {10,7,1,2,3}
print("길이: ", len(m))
print("포함여부: ", 1 in m)
print("포함여부: ", 5 in m)
m.clear()
print("clear: ", m)

print("#"+"-"*20+"#")

#help(set)
