# 1. 산술 연산자
print(3+2)
print(3-2)
print(3*2)
print(3/2)  # 결과가 실수형
print(3//2) # 몫
print(3%2)  # 나머지
print(3**2) # 지수

print("#"+"-"*20+"#")

# 2. 몫과 나머지를 함께 얻고 싶을 때 : divmod 함수 이용, tuple 형태로 결과 출력
print(divmod(3,2))

print("#"+"-"*20+"#")

# 3. 비교 연산자 : 결과값이 True, False 로 출력
print(3 > 2)
m = 3 > 2
print(m)
print(3 >= 2)
print(3 < 2)
print(3 <= 2)
print(3 != 2)
print(3 == 2)

print("#"+"-"*20+"#")

# 4. 대입 연산자
n1=n2=n3=n4=n5=n6=n7=3
m=2

n1 += m     # n1 = n1 + m
print(n1)
n2 -= m     # n2 = n2 - m
print(n2)
n3 *= m     # n3 = n3 * m
print(n3)
n4 /= m     # n4 = n4 / m
print(n4)
n5 //= m    # n5 = n5 // m
print(n5)
n6 %= m     # n6 = n6 % m
print(n6)
n7 **= m    # n7 = n7 ** m
print(n7)

print("#"+"-"*20+"#")

# 5. unpacking 1
k1,k2='he'       #unpacking
print(k1,k2)

k1,k2=[10,20]    #unpacking
print(k1,k2)

k1,k2={10,20}    #unpacking
print(k1,k2)

k1,k2=(10,20)    #unpacking
print(k1,k2)

k1,k2={"x":77,"y":88}   #unpacking
print(k1,k2)            # key 출력

# to get values in dict
m = {"x":77,"y":88}     #unpacking
k1,k2 = m
print(m[k1],m[k2])

print("#"+"-"*20+"#")

# 6. unpacking 2
# 갯수가 일치하지 않을때
# *는 반드시 한번만 사용해야 함

#k1,k2=[10,20,30] #unpacking
k1,*k2=[10,20,30] #unpacking
print(k1,k2)    # 10 [20, 30]

*k1,k2=[10,20,30] #unpacking
print(k1,k2)    # [10 20] 30

*k1,k2=(10,20,30) #unpacking
print(k1,k2)    # [10 20] 30

print("#"+"-"*20+"#")

# 7. 논리 연산자 and or not
print(3>4 and 4==4)
print(3>4 or 4==4)
print(not (3>4))

print("#"+"-"*20+"#")
