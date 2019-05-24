# 1. 일반적인 print 사용
print(100)
print("hello world")
# default sep=" ", default end="\n"
print(100,200)
print(300,400)
print(100,200,sep=",", end="\t")
print(300,400,sep=",")

print("#"+"-"*20+"#")

# 2. format 출력
# format_spec :: = [[ fill] align] [ sign] [#] [0] [ width] [ grouping_option] [. precision] [ type]
# fill :: = <모든 문자>
# align :: = "<"| ">"| "="| "^"
# sign :: = "+"| "-"| ""
# width :: = digit+ grouping_option :: = "_"| ","
# precision :: = digit+
# type :: = "b"| "c"| "d"| "e"| "E"| "f"| "F"| "g"| "G"| "n"| "o"| "s"| "x"| "X"

n = "홍길동"
a = 20
print("이름은 "+n+"이고 나이는 "+str(a))

print("#"+"-"*20+"#")

# 3. 다양한 format 출력
# 문법 :
# '{}'.format(값)
# '{}{}'.format(값1, 값2)

print("이름은 {0}이고 나이는 {1}".format(n, str(a)))

mesg = "이름은 {0}이고 나이는 {1}".format(n, str(a))
print(mesg)

mesg = "이름은 {0}이고 나이는 {1}".format("이순신", 20)
print(mesg)

print("#"+"-"*20+"#")

# unpacking
mesg = "{0}::::::{1}".format(*"hello")
print(mesg)
mesg = "{1}::::::{2}{0}".format(*"hello")
print(mesg)

print("#"+"-"*20+"#")

# list
mesg = "{0[0]}::::::{0[1]}".format([10,20])
print(mesg)
mesg = "{0}::::::{1}".format(*[10,20])
print(mesg)

print("#"+"-"*20+"#")

# set : set 은 불가, 순서가 없기 때문에
# mesg =  "{0[0]}::::::{0[1]}".format({10,20})
# print(mesg)

# tuple
mesg =  "{0[0]}::::::{0[1]}".format((10,20))
print(mesg)

print("#"+"-"*20+"#")

# 3자리마다 ','
price = '{:,}'.format(123456789)
print(price)

# 정수, 실수
price = '{0:f},{0:.3f},{0:d},{0:11d}'.format(1234)
print(price)
print('{0:f},{0:.3f},{0:d},{0:11d}'.format(1234))

print("#"+"-"*20+"#")

# 16진수
print("%#0.3x"%255, "%0.3x"%255, "%0.3X"%255)
# print('{0:#{width}{base}}'.format(16, base='x', width=4))
print('{0:08x}'.format(16))
print('{0:#010x}'.format(16))
print('{0:#011_x}'.format(16))

print("#"+"-"*20+"#")

# 정렬
print('{:<5}'.format("ABC"))
print('{:>5}'.format("ABC"))
print('{:^5}'.format("ABC"))

print('{:<5}'.format(-10))
print('{:>5}'.format(-10))
print('{:^5}'.format(-10))
print('{:=5}'.format(-10))

print('{:}'.format(100))
print('{:}'.format(-100))
print('{:+}'.format(100))    # 양수, 음수 모두 부호 표시
print('{:+}'.format(-100))   # 양수, 음수 모두 부호 표시
print('{: }'.format(100))    # 양수의 경우 부호 없이 한칸 띄우고, 음수는 부호 표시
print('{: }'.format(-100))   # 양수의 경우 부호 없이 한칸 띄우고, 음수는 부호 표시

print("#"+"-"*20+"#")

# dict 출력
person = {"A":"123", "B":"456", "C":"789"}
print('{p[A]} {p[B]}'.format(p=person))

print("#"+"-"*20+"#")

# 4. print 사용법
# help(print)

# print("#"+"-"*20+"#")

# 5. formatting 사용법
# help('FORMATTING')

# print("#"+"-"*20+"#")