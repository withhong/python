# data type
# python 은 다른 언어의 int, float, bool, str 처럼 특별히 지정해서 data type 을 정의하지 않아도 된다. 실행하면서 data type 을 인식한다.
#
# 종류
# 기본형 - 문자(string), 수치(정수(int), 실수(float), 8진수, 16진수), 논리(bool)
# 집합형 - list, set, tuple, dict

# 1. 문자열
print("문자열 타입")
print("hello")
print('hello')
print('''hello''')
print("""hello""")

print("#"+"-"*20+"#")

# 2. escape 문자
print('\'')
print('\"')
print("hello\tworld")
print("hello\nworld")
print("c:\\temp")

print("#"+"-"*20+"#")

# 3. raw string : escape 문자 비활성화
print(r'\'')
print(r'\"')
print(r"hello\tworld")
print(r"hello\nworld")
print(r"c:\\temp")

print("#"+"-"*20+"#")

# 4. 문자열 연결
print("A"+"B")
str_A = "A"
str_B = "B"
print(str_A + str_B)
#print("A"+10)      # 문자와 숫자가 바로 연결될 수는 없음
print("A"+str(10))  # 숫자를 문자로 바꾼 후 에 연결 가능
print("A",10)
print("A",10,sep="")

print("#"+"-"*20+"#")

# 5. 수치 데이터
print(1324349833493434394830) # 메모리가 허락하는 한 길이 제한이 없음
print(100_000_000)            # 가독성을 위해 '_' 사용가능
print(3.24)                   # 실수형
bin_value = 0b1000            # 2진수
print(bin(bin_value), bin_value, int(bin_value))
oct_value = 0o10              # 8진수
print(oct(oct_value), oct_value, int(oct_value))
hex_value = 0x10              # 16진수
print(hex(hex_value), hex_value, int(hex_value))

print("#"+"-"*20+"#")

# 6. 논리 데이터
print(True)
print(False)

print("#"+"-"*20+"#")

# 7. list : 순서 있고 중복 허용, 수정 가능, 혼합 데이터 가능
print([10,20,30])
print([10,20,3.0])
print([10,20,"A"])

print("#"+"-"*20+"#")

# 8. set : 순서 없기 때문에 중복 안됨, 수정 가능, 혼합 데이터 가능
print({10,20,30})
print({10,20,30,10})
print({10,20,3.0, 'A'}) # 순서가 없어서 랜덤하게 출력 (실행할때마다)

print("#"+"-"*20+"#")

# 9. tuple : 순서 있고 수정 안됨, 중복 가능, 혼합 데이터 가능
print((10,20,30))
print((10,20,30,10))
print((10,20,3.0, 'A'))

print("#"+"-"*20+"#")

# 10. dict : 'key', 'value' 쌍으로 - map 계열 (search 가 빠름) - JSON 형태
# 순서 없음, 중복되면 뒤에 있는 것이 출력
# {"key":"value"}
print({"name":"AAA", "age":20, "address":"서울"})
print({"name":"AAA", "age":20, "address":"서울", "name":"BBB"})

print("#"+"-"*20+"#")

# 11. 데이터 타입 정리

n1 = 10
n2 = "홍길동"
n3 = 3.14
n4 = True
n5 = [10,20,30]
n6 = {10,20,30}
n7 = (10,20,30)
n8 = {"key":"value"}

print (n1, type(n1))
print (n2, type(n2))
print (n3, type(n3))
print (n4, type(n4))
print (n5, type(n5))
print (n6, type(n6))
print (n7, type(n7))
print (n8, type(n8))

print("#"+"-"*20+"#")

#help(list)
#help(set)
#help(tuple)
