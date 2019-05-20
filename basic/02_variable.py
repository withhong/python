# variable (변수)

# 1. 일반적인 변수의 사용
name = "홍길동"
age = 20
address = "서울"
isMarrired = True
height = 180
weight = 68
phone = ["01011112222", "01111112222"]

print("이름은"+name)
print("나이는"+str(age))
print("전화는", phone[0], phone[1])

print("#"+"-"*20+"#")

# 2. 동시에 여러 변수 선언 가능
n1=n2=n3=10
print(n1, n2, n3)

print("#"+"-"*20+"#")

# 3. 동시에 여러 변수에 저장하는데 값이 다른 경우
x, y, z = "홍길동", 20, "서울"
print(x,y,z)

x, y, z = "홍길동", 30, "서울"
print(x,y,z)

print("#"+"-"*20+"#")

# 4. 대량 문자열 사용시 : ''' '''(triple)
mesg = "안녕하세요. 저는 홍길동입니다."
print(mesg)
mesg = '''\
이름 : 홍길동
나이 : 30\
'''
print(mesg)

print("#"+"-"*20+"#")

# 5. 여러 정수값 연산시 : '\' 사용
result = 10 + 20 + 30
print(result)

result = 10 + 20 + \
30
print(result)

print("#"+"-"*20+"#")

# 6. keyword 확인
# variable 사용시 사용되는 이름이 keyword 에 해당될 수 있는데
# 이를 방지하기 위해 다음과 같이 미리 정의된 keyword 를 확인 가능하다.
import keyword
print("키워드 목록", keyword.kwlist)

print("#"+"-"*20+"#")
