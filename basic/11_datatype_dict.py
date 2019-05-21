# 1. dict 생성
m1 = dict()
m2 = dict({"name":"홍길동", "age":20})
m3 = {"name":"홍길동", "age":20}

print(m1)
print(m2)
print(m3)

print("#"+"-"*20+"#")

# 2. dict 추가, 수정, 삭제
# 추가
m = {"name":"홍길동", "age":20}
m['address'] = "서울"
print("address 추가: ", m)

# 수정
m["age"] = 40
print("age 수정: ", m)

# 삭제
del m["address"]
print("address 삭제: ", m)

# dict 전체 삭제
m.clear()
print("dict 삭제 (clear): ", m)

print("#"+"-"*20+"#")

# 3. dict 기타 함수
m1 = {"name":"홍길동", "age":20}
print("길이: ", len(m1))
print("접근: ", m1["name"], m1["age"]) # m1['name'] 연관배열
print("접근: ", m1.get("name"))

print("#"+"-"*20+"#")

print("key값만 얻기: ", m1.keys())
m2 = list(m1.keys())
print("list 변환 후 key값만 얻기: ", m2)

print("value값만 얻기: ", m1.values())
m3 = list(m1.values())
print("list 변환 후 value값만 얻기: ", m3)

print("key, value 얻기: ", m1.items())
m4 = list(m1.items())
print("list 변환 후 key, value 얻기: ", m4)

print("#"+"-"*20+"#")

print("key 존재여부: ", "name" in m1)
print("key 존재여부: ", "name" in m1.keys())
print("value 존재여부: ", "홍길동" in m1.values())

print("#"+"-"*20+"#")

#help(dict)
