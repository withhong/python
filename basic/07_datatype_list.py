#1. list 생성 (순서 있고 중복 가능, 수정 가능, 혼합 데이터 가능)
m1 = [10,20,30]
m2 = []             # 비어있는 list 생성 가능

#2. 함수
# append
m = [10,20,30]
m.append(40)
print("append: ", m)
m.append([50,60]) # list
print("append: ", m)
m.append((70,80)) # tuple
print("append: ", m)

print("#"+"-"*20+"#")

# extend : 추가할 때 추가하는 값을 개별값으로 추가 가능
m = [10,20,30]
m.extend([900,300])
print("extend: ", m)
m.extend([700])
print("extend: ", m)

print("#"+"-"*20+"#")

# insert : 특정 위치에 추가 가능
m = [10,20,30]
m.insert(0, 100)
print("insert: ", m)
m.insert(1, [7,8,9])
print("insert: ", m)

print("#"+"-"*20+"#")

# + 사용
m1 = [10,20,30]
m2 = [7,8,9]
m2 += m1
print("+로 리스트 생성", m1)
print("+로 리스트 생성", m2)

print("#"+"-"*20+"#")

# slice
m = [10,20,30]
print("특정값: ", m[0])
print("특정값: ", m[0:3])
print("특정값: ", m[:3])
print("특정값: ", m[:])

print("#"+"-"*20+"#")

# 기타 함수
print("길이: ", len(m))
print("포함갯수: ", [1,2,2,3,4].count(2))
print("특정위치: ", [1,2,2,3,4].index(2))
print("특정위치: ", [1,2,2,3,4].index(2,2,3))
print("포함여부: ", 1 in [1,2,2,3,4])
print("포함여부: ", 5 in [1,2,2,3,4])

print("#"+"-"*20+"#")

# modify
m = [10,20,30,40]
m[0] = 100
print("값변경:", m)

print("#"+"-"*20+"#")

# pop
m = [10,20,30,40]
m.pop() # 맨 끝값 삭제
print("pop: ", m)

m = [10,20,30,40]
m.pop(-1) # 맨 끝값 삭제
print("pop: ", m)

m = [10,20,30,40]
m.pop(0) # 맨 처음값 삭제
print("pop: ", m)

print("#"+"-"*20+"#")

# del
m = [10,20,30,40]
del m[-1] # 맨 끝값 삭제
print("del: ", m)

m = [10,20,30,40]
del m[0] # 맨 처음값 삭제
print("del: ", m)

print("#"+"-"*20+"#")

# remove : 값에 의한 삭제
m = [10,20,30,40,100]
m.remove(100)
print("값에 의한 삭제:", m)

print("#"+"-"*20+"#")

# 중첩 접근
m = [10,20,30,[7,8,9]]
print("리스트 중첩 접근: ", m[3][0:3])

print("#"+"-"*20+"#")

# 정렬
m = [9,5,2,4,1,7]
m.sort()
print("오름차순: ", m)
m.sort(reverse=True)
print("내림차순: ", m)

print("#"+"-"*20+"#")

# 숫자 표현 문자열 정렬 : 한자리는 정렬됨, 한자리만 비교
m = ['9', '5', '2']
m.sort()
print("오름차순: ", m)
m.sort(reverse=True)
print("내림차순: ", m)

m = ['90', '500', '20']
m.sort()
print("오름차순: ", m)
m.sort(reverse=True)
print("내림차순: ", m)

print("#"+"-"*20+"#")

# 숫자 표현 문자열 정렬 : 정수로 변경 후 정렬
m = ['90', '500', '20']
m.sort(key=int) # 원래는 ascii 로 비교
print("오름차순: ", m)
m.sort(key=int, reverse=True)
print("내림차순: ", m)

print("#"+"-"*20+"#")

# 리스트 삭제
m.clear()
print(m)

print("#"+"-"*20+"#")

#help(list)