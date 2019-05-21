# while

n = 1
while n < 6 :
    print("hello")
    n += 1
print("end")

print("#"+"-"*20+"#")

# while 중첩

n = 1
while n < 4 :
    m = 1
    while m < 3:
        print(str(n) + " " + str(m))
        m += 1
    n += 1
print("end")

print("#"+"-"*20+"#")