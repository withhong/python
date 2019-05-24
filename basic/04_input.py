# keyboard 입력
m = input("이름 입력: ")
print(m)

# 여러 입력 한번에 받는 방법
#a, b, c, d = map(int, input("4개 입력(예: 1 2 3 4): ").split(" "))
a, b, c, d = map(int, input("4개 입력(예: 1 2 3 4): ").split())
print(a, b, c, d, sum([a, b, c, d]))
