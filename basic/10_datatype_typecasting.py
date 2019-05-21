# 1. list -> set, tuple
p1 = [10,20,30] # list

# list -> tuple
p2 = set(p1)
print(p1,p2)

# list -> list
p2 = tuple(p1)
print(p1,p2)

print("#"+"-"*20+"#")

# 2. set -> tuple, list
p1 = {10,20,30} # set

# set -> tuple
p2 = tuple(p1)
print(p1,p2)

# set -> list
p2 = list(p1)
print(p1,p2)

print("#"+"-"*20+"#")

# 3. tuple -> list, set
p1 = (10,20,30) # tuple

# tuple -> list
p2 = list(p1)
print(p1,p2)

# tuple -> set
p2 = set(p1)
print(p1,p2)

print("#"+"-"*20+"#")

#help(list)
#help(tuple)
#help(set)

# 2. set 에서는 합집합, 교집합, 차집합이 사용 가능
a = {1,2,3,4}
b = {3,4}
print("합집합: ", a.union(b))
print("교집합: ", a.intersection(b))
print("차집합: ", a.difference(b))

print("#"+"-"*20+"#")