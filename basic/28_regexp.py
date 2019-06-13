# 정규 표현식 (regexp)

import re   # 파이썬에서 정규 표현식 사용을 도와주는 모듈, 기본 라이브러리

# 1. 문자열 검색
# (1) match() : 문자열의 처음부터 정규식과 매치
# (2) search() : 문자열 전체를 검색하여 정규식과 매치
# (3) findall() : 정규식과 매치되는 모든 문자열을 리스트로 반환
# (4) finditer() : 정규식과 매치되는 모든 문자열을 iterator 로 반환

# 매치된 결과는 객체로 반환하기에 문자열을 반환하기 위한 별도의 함수가 필요
# group() : 매치된 문자열 반환
# start() : 매치된 문자열의 시작 위치
# end() : 매치된 문자열의 끝 위치
# span() : 매치된 문자열을 튜플로 반환 (시작, 끝)

# match 와 search 의 차이는 match 는 문자열의 처음부터 매치시키기 때문에 패턴이 문자열의 처음부터 매치되어야 한다.

# 1.1 match()
# 찾으면 객체가 반환되고 못찾으면 None 이 반환
print("문자열 검색 (match) :", re.match("H",     "Hello World!"))
print("문자열 검색 (match) :", re.match("Hello", "Hello World!"))
print("문자열 검색 (match) :", re.match("Hi",    "Hello World!"))
print("문자열 검색 (match) :", re.match("World",  "Hello World!"))  # match 는 문자열의 처음부터 검색하기에 패턴이 처음부터 매치되어야 한다.

# 문자열을 compile 해두고 이를 사용해서 할 수도 있다.
pat1 = re.compile("H")
pat2 = re.compile("Hello")
pat3 = re.compile("Hi")
pat4 = re.compile("World")

# print("문자열 검색 (match) :", pat1.match("Hello World!"))
# print("문자열 검색 (match) :", pat2.match("Hello World!"))
# print("문자열 검색 (match) :", pat3.match("Hello World!"))
# print("문자열 검색 (match) :", pat4.match("Hello World!"))

print("문자열 검색 (match) : True") if pat1.match("Hello World!") else print("문자열 검색 (match) : None")
print("문자열 검색 (match) : True") if pat2.match("Hello World!") else print("문자열 검색 (match) : None")
print("문자열 검색 (match) : True") if pat3.match("Hello World!") else print("문자열 검색 (match) : None")
print("문자열 검색 (match) : True") if pat4.match("Hello World!") else print("문자열 검색 (match) : None")

print("#"+"-"*20+"#")

# 1.2 search()
# 찾으면 객체가 반환되고 못찾으면 None 이 반환
print("문자열 검색 (search) :", re.search("H",     "Hello World!"))
print("문자열 검색 (search) :", re.search("Hello", "Hello World!"))
print("문자열 검색 (search) :", re.search("Hi",    "Hello World!"))
print("문자열 검색 (search) :", re.search("World", "Hello World!"))

# 문자열을 compile 해두고 이를 사용해서 할 수도 있다.
pat1 = re.compile("H")
pat2 = re.compile("Hello")
pat3 = re.compile("Hi")
pat4 = re.compile("World")

# print("문자열 검색 (search) :", pat1.search("Hello World!"))
# print("문자열 검색 (search) :", pat2.search("Hello World!"))
# print("문자열 검색 (search) :", pat3.search("Hello World!"))
# print("문자열 검색 (search) :", pat4.search("Hello World!"))

print("문자열 검색 (search) : True") if pat1.search("Hello World!") else print("문자열 검색 (search) : None")
print("문자열 검색 (search) : True") if pat2.search("Hello World!") else print("문자열 검색 (search) : None")
print("문자열 검색 (search) : True") if pat3.search("Hello World!") else print("문자열 검색 (search) : None")
print("문자열 검색 (search) : True") if pat4.search("Hello World!") else print("문자열 검색 (search) : None")

print("#"+"-"*20+"#")

# 1.3 findall()
pat1 = re.compile("H")
pat2 = re.compile("Hello")
pat3 = re.compile("Hi")
pat4 = re.compile("World")

print("문자열 검색 (findall) :", pat1.findall("Hello World!"*2))
print("문자열 검색 (findall) :", pat2.findall("Hello World!"*2))
print("문자열 검색 (findall) :", pat3.findall("Hello World!"*2))
print("문자열 검색 (findall) :", pat4.findall("Hello World!"*2))

print("#"+"-"*20+"#")

# 1.4 finditer()
pat1 = re.compile("H")
pat2 = re.compile("Hello")
pat3 = re.compile("Hi")
pat4 = re.compile("World")

for i in pat1.finditer("Hello World!"*2):
    print("문자열 검색 (finditer) :", i, i.group())
for i in pat2.finditer("Hello World!"*2):
    print("문자열 검색 (finditer) :", i, i.group())
for i in pat3.finditer("Hello World!"*2):
    print("문자열 검색 (finditer) :", i, i.group())
for i in pat4.finditer("Hello World!"*2):
    print("문자열 검색 (finditer) :", i, i.group())

print("#"+"-"*20+"#")

# 1.5 group(), start(), end(), span()
# match 된게 없으면 에러 발생
# match, search 와 함께 사용가능
pat2 = re.compile("Hello")

print("문자열 검색 (match group) :", pat2.match("Hello World!").group())
print("문자열 검색 (match start) :", pat2.match("Hello World!").start())
print("문자열 검색 (match end) :",   pat2.match("Hello World!").end())
print("문자열 검색 (match span) :",  pat2.match("Hello World!").span())

pat2 = re.compile("Hello")

print("문자열 검색 (search group) :", pat2.search("Hello World!"*2).group(0))
print("문자열 검색 (search start) :", pat2.search("Hello World!"*2).start(0))
print("문자열 검색 (search end) :",   pat2.search("Hello World!"*2).end(0))
print("문자열 검색 (search span) :",  pat2.search("Hello World!"*2).span(0))

print("#"+"-"*20+"#")

# 2. 메타 문자
# . ^ $ * + ? { } [ ] \ | ( )

# .     : \n 제외한 모든 문자
# ^     : 패턴으로 시작
# $     : 패턴으로 끝
# *     : 바로 앞의 패턴이 0개 이상
# +     : 바로 앞의 패턴이 1개 이상
# ?     : 바로 앞의 패턴이 없거나 1개 이상
# { }   : 패턴{숫자} 숫자만큼 패턴이 반복. 패턴{숫자1, 숫자2}
# [ ]   : [문자] 가능한 문자들의 집합. [^문자] 없어야하는 문자들의 집합
# \     :
#           \A  : 문자열의 처음. ^ 는 라인의 처음. \A 는 전체 문자열의 처음
#           \Z  : 문자열의 끝. $ 는 라인의 끝. \Z 는 전체 문자열의 끝
#           \b  : 공백에 의해서 구분되는 단어 구분자
#           \B  : 단어 구분자 제외
# |     : or, 여러개 중에 하나
# ( )   : 패턴을 묶어줄때 사용. 그룹핑

# 2.1 .
# \n 제외한 모든 문자
pat1 = re.compile("a.b")

print("메타 . :", pat1.search("abc"))  # a 와 b 사이에 문자가 있어야 함
print("메타 . :", pat1.search("a b"))
print("메타 . :", pat1.search("a7b"))

print("#"+"-"*20+"#")

# 2.2 ^
# 문자열의 시작이 패턴과 동일해야 함
pat1 = re.compile("^a")

print("메타 ^ :", pat1.search("abc"))
print("메타 ^ :", pat1.search("a b"))
print("메타 ^ :", pat1.search("7ab"))  # a 로 시작해야 함

print("#"+"-"*20+"#")

# 2.3 $
# 문자열의 끝이 패턴과 동일해야 함
pat1 = re.compile("b$")

print("메타 $ :", pat1.search("abc"))  # b 로 끝나야 함
print("메타 $ :", pat1.search("a b"))
print("메타 $ :", pat1.search("a7b"))

print("#"+"-"*20+"#")

# 2.4 *
# 바로 앞의 패턴이 0개 이상 반복
pat1 = re.compile("ab*c")

print("메타 * :", pat1.search("ac"))
print("메타 * :", pat1.search("abc"))
print("메타 * :", pat1.search("abbc"))
print("메타 * :", pat1.search("a7c")) # b 가 나오거나 안나오거 해야 함. 다른 문자에 대한 언급은 없음

print("#"+"-"*20+"#")

# 2.5 +
# 바로 앞의 패턴이 1개 이상 반복
pat1 = re.compile("ab+c")

print("메타 + :", pat1.search("ac"))  # b 가 1개 이상 있어야 함
print("메타 + :", pat1.search("abc"))
print("메타 + :", pat1.search("abbc"))
print("메타 + :", pat1.search("a7c")) # b 가 1개 이상 있어야 함

print("#"+"-"*20+"#")

# 2.6 ?
# 바로 앞의 패턴이 없거나 1개 이상
pat1 = re.compile("ab?c")

print("메타 ? :", pat1.search("ac"))
print("메타 ? :", pat1.search("abc"))
print("메타 ? :", pat1.search("abbc"))# b 가 없거나 1개여야 함
print("메타 ? :", pat1.search("a7c")) # b 가 없거나 1개여야 함

print("#"+"-"*20+"#")

# 2.7 { }
# 패턴{숫자} 숫자만큼 패턴이 반복. 패턴{숫자1, 숫자2}
pat1 = re.compile("ab{1}c")

print("메타 { } :", pat1.search("ac"))    # b 가 1개여야 함
print("메타 { } :", pat1.search("abc"))   # b 가 1개여야 함
print("메타 { } :", pat1.search("abbc"))  # b 가 1개여야 함
print("메타 { } :", pat1.search("a7c"))   # b 가 1개여야 함

print("#"+"-"*20+"#")

# 2.8 [ ]
# 문자 클래스
# [ ] 사이에 들어가는 문자들과 매치
# - 을 사용하면 시작과 끝을 나타내기에 [a-c] 는 [abc], [0-2] 는 [012] 를 나타낸다.
# [a-zA-Z] : 모든 영문자, [0-9] : 모든 숫자
# [가-힣] : 모든 한글
# [ ] 내에 ^ 는 반대라는 의미. 즉, [^0-9] 는 숫자를 제외한 모든 문자를 의미한다.
# 자주 사용되는 문자 클래스
# [\d] : [0-9] 숫자
# [\D] : [^0-9] 숫자가 아닌 것
# [\s] : [ \t\n\r\f\v] 공백
# [\S] : [^ \t\n\r\f\v] 공백이 아닌 것
# [\w] : [a-zA-Z0-9] 문자, 숫자
# [\W] : [^a-zA-Z0-9] 문자, 숫자가 아닌것

pat1 = re.compile("[abc]")
pat2 = re.compile("[a-c]")
pat3 = re.compile("[a-z]")
pat4 = re.compile("[^0-9]")

print("메타 [] :", pat1.search("before").group())
print("메타 [] :", pat1.search("after").group())
print("메타 [] :", pat1.search("abc").group())

print("메타 [] :", pat2.search("before").group())
print("메타 [] :", pat2.search("after").group())
print("메타 [] :", pat2.search("abc").group())

print("메타 [] :", pat3.search("before").group())
print("메타 [] :", pat3.search("after").group())
print("메타 [] :", pat3.search("abc").group())

print("메타 [] :", pat4.search("before").group())
print("메타 [] :", pat4.search("after").group())
print("메타 [] :", pat4.search("abc").group())

print("#"+"-"*20+"#")

# 2.9 \
# \A : 문자열의 처음. ^ 는 라인의 처음. \A 는 전체 문자열의 처음
# \Z : 문자열의 끝. $ 는 라인의 끝. \Z 는 전체 문자열의 끝
# \b : 공백에 의해서 구분되는 단어 구분자
# \B : 단어 구분자 제외
pat1 = re.compile("\Aa")

print("메타 \A :", pat1.search("abc"))
print("메타 \A :", pat1.search("a b"))
print("메타 \A :", pat1.search("7ab"))  # a 로 시작해야 함

print("#"+"-"*20+"#")

pat1 = re.compile("b\Z")

print("메타 \Z :", pat1.search("abc"))  # b 로 끝나야 함
print("메타 \Z :", pat1.search("a b"))
print("메타 \Z :", pat1.search("a7b"))

print("#"+"-"*20+"#")

pat1 = re.compile(r"\bWorld\b")

print(r"메타 \b :", pat1.search("Hello World !!!"))
print(r"메타 \b :", pat1.search("Hello World!!!")) # World! 에서도 검색해냄. 즉, ! 도 단어 구분자로 인식
print(r"메타 \b :", pat1.search("HelloWorld !!!")) # 앞에 공백이 없어 검색못함

print("#"+"-"*20+"#")

pat1 = re.compile(r"\WWorld\W")

print("메타 \W :", pat1.search("Hello World !!!"))
print("메타 \W :", pat1.search("Hello World!!!")) # World! 에서도 검색해냄. 즉, ! 도 단어 구분자로 인식
print("메타 \W :", pat1.search("HelloWorld !!!")) # 앞에 공백이 없어 검색못함

print("#"+"-"*20+"#")

pat1 = re.compile(r"\BWorld\B")

print("메타 \B :", pat1.search("Hello World !!!"))    # World 의 앞뒤 모두 단어구분자가 없어야 함
print("메타 \B :", pat1.search("Hello World!!!"))     # World 의 앞뒤 모두 단어구분자가 없어야 함
print("메타 \B :", pat1.search("HelloWorld!!!"))      # World 의 앞뒤 모두 단어구분자가 없어야 함
print("메타 \B :", pat1.search("HelloWorldHello!!!")) # World 의 앞뒤 모두 단어구분자가 없어서 검색해냄

print("#"+"-"*20+"#")

# 2.10 |
# or, 여러개 중에 하나
pat1 = re.compile("ab|abc")

print("메타 | :", pat1.search("abc"))
print("메타 | :", pat1.search("a b")) # ab 혹은 abc 여야 함
print("메타 | :", pat1.search("7ab"))

print("#"+"-"*20+"#")

# 2.11 ( )
# 패턴을 묶어줄때 사용. 그룹핑
pat1 = re.compile("(ab)+")

print("메타 ( ) group :", pat1.search("abc"))
print("메타 ( ) group :", pat1.search("a b")) # ab 가 1번 이상 반복되어야 함
print("메타 ( ) group :", pat1.search("7ab"))

#pat1 = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
pat1 = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")

print("메타 ( ) group :", pat1.search("AAA 010-1234-5678").group(0))  # 매치된 전체 문자열
print("메타 ( ) group :", pat1.search("AAA 010-1234-5678").group(1))  # 매치된 첫번째 그룹
print("메타 ( ) group :", pat1.search("AAA 010-1234-5678").group(2))  # 매치된 두번째 그룹

pat1 = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")   # 중첩도 가능하며 이경우 바깥쪽부터 안쪽으로 인덱스를 증가시킨다.

print("메타 ( ) group :", pat1.search("AAA 010-1234-5678").group(0))  # 매치된 전체 문자열
print("메타 ( ) group :", pat1.search("AAA 010-1234-5678").group(1))  # 매치된 첫번째 그룹
print("메타 ( ) group :", pat1.search("AAA 010-1234-5678").group(2))  # 매치된 두번째 그룹
print("메타 ( ) group :", pat1.search("AAA 010-1234-5678").group(3))  # 매치된 세번째 그룹

# 그룹에 이름을 부여할 수 있음
# (\w+) -> (?P<group_name>\w+)
pat1 = re.compile(r"(?P<name>\w+)\s+(?P<number>\d+[-]\d+[-]\d+)")

print("메타 ( ) group name :", pat1.search("AAA 010-1234-5678").group("name"))
print("메타 ( ) group number :", pat1.search("AAA 010-1234-5678").group("number"))

print("#"+"-"*20+"#")

# 3. 전방 탐색
pat1 = re.compile(".*[.].*$")
a = ["aaa.bat", "bbb.exe", "ccc.txt", "ddd", "eee.py"]

for i in a:
    if pat1.search(i):
        print("검색 :", pat1.search(i).group())

print("#"+"-"*20+"#")

# 긍정형 전방 탐색
# (?=) 를 사용
pat1 = re.compile(".*[.](?=bat$).*$")
a = ["aaa.bat", "bbb.exe", "ccc.txt", "ddd", "eee.py"]

for i in a:
    if pat1.search(i):
        print("검색 :", pat1.search(i).group())

print("#"+"-"*20+"#")

# 부정형 전방 탐색
# (?!) 를 사용
pat1 = re.compile(".*[.](?!bat$).*$")
a = ["aaa.bat", "bbb.exe", "ccc.txt", "ddd", "eee.py"]

for i in a:
    if pat1.search(i):
        print("검색 :", pat1.search(i).group())

print("#"+"-"*20+"#")

# 4.1 문자열 바꾸기
# sub 함수 사용 : sub(바뀌고 나서의 문자열, 검색할 문자열)
# subn 은 tuple 로 처리 (바뀐 문자열, 바꾼 횟수)
pat1 = re.compile("(AAA|BBB|CCC)")
print("문자열 바꾸기 :", pat1.sub("abc", "AAA BBB CCC aaa bbb ccc"))
print("문자열 바꾸기 :", pat1.subn("abc", "AAA BBB CCC aaa bbb ccc"))

print("#"+"-"*20+"#")

# 4.2 문자열 바꾸기 : 참조 구문 이용하기
pat1 = re.compile(r"(?P<name>\w+)\s+(?P<number>\d+[-]\d+[-]\d+)")
print("문자열 바꾸기 :", pat1.sub("\g<number> \g<name>", "AAA 010-1234-5678"))

print("#"+"-"*20+"#")

# 5. 컴파일 옵션
# 찾으려고 하는 정규 표현식을 're.compile' 을 통해 컴파일할때 옵션을 줄 수 있다.
# DOTALL(S)
# IGNORE(I)
# MULTILINE(M)
# VERBOSE(X)

# 5.1 DOTALL, S
# . 검색하면 \n 외에 모든 문자를 검색하지만 DOTALL 옵션으로 컴파일하면 \n 도 포함
pat1 = re.compile("a.b")
pat2 = re.compile("a.b", re.DOTALL)
pat3 = re.compile("a.b", re.S)

print("compile :", pat1.search("a\nb"))
print("compile DOTALL (DOTALL) :", pat2.search("a\nb"))
print("compile DOTALL (S):", pat3.search("a\nb"))

print("#"+"-"*20+"#")

# 5.2 IGNORECASE, I
# 대소문자 구별없이 검색
pat1 = re.compile("[a-z]+")
pat2 = re.compile("[a-z]+", re.IGNORECASE)
pat3 = re.compile("[a-z]+", re.I)

print("compile :", pat1.search("ABC"))
print("compile IGNORECASE (IGNORECASE) :", pat2.search("ABC"))
print("compile IGNORECASE (I):", pat3.search("ABC"))

print("#"+"-"*20+"#")

# 5.3 MULTILINE, M
# 여러라인에서 라인마다 검색
mesg = """AAA
BBB CCC
AAA BBB
CCC AAA
BBB"""

pat1 = re.compile("AAA")
pat2 = re.compile("AAA", re.MULTILINE)
pat3 = re.compile("AAA", re.M)

print("compile :", pat1.findall(mesg))
print("compile MULTILINE (MULTILINE) :", pat2.findall(mesg))
print("compile MULTILINE (M):", pat3.findall(mesg))

print("#"+"-"*20+"#")

# 5.4 VERBOSE, X
pat1 = re.compile(r"(?P<name>\w+)\s+(?P<number>\d+[-]\d+[-]\d+)")
pat2 = re.compile(r"""
                    (?P<name>\w+)   # name
                    \s+
                    (?P<number>\d+[-]\d+[-]\d+) # number
                    """, re.VERBOSE)

print("compile :", pat1.search("AAA 010-1234-5678").group())
print("compile VERBOSE :", pat2.search("AAA 010-1234-5678").group())

print("#"+"-"*20+"#")

# 6. \
# 문자열에 \ 가 있는 경우
pat1 = re.compile("\\\Two")
pat2 = re.compile(r"\\Two")

print("\ :", pat1.search("C:\One\Two\Three").group())
print("\ :", pat2.search("C:\One\Two\Three").group())

print("#"+"-"*20+"#")

#
pat1 = re.compile('{(\s*)"(\w+)":\s*"(\w+)"(\s*)}')
print("\ :", pat1.sub(r'<\2>\3</\2>', '{ "name": "aaa" }'))

print("#"+"-"*20+"#")


