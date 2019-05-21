# break : 반복문을 빠져나올때
# continue : 반복할 문장이 여러개인 경우에 특정 문장들을 skip 할 때

for n in range(1,6):
    if n==3: continue
    print(str(n), "hello")
print("end")

print("#"+"-"*20+"#")

for n in range(1,6):
    if n==3: break
    print(str(n), "hello")
print("end")

print("#"+"-"*20+"#")
