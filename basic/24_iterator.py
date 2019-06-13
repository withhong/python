# 반복자 (iterator)
# 값을 차례대로 사용할 수 있는 객체

# 1. 반복 가능한 객체
# str, list, dict, set, ...
# __iter__ 함수가 있는지를 통해서 확인 가능
# dir : datatype 이 가지는 함수(메소드)나 변수를 반환
print("iter in int :", '__iter__' in dir(10))
print("iter in str :", '__iter__' in dir('10'))
print("iter in list :", '__iter__' in dir([10,20,30]))
print("iter in set :", '__iter__' in dir({10,20,30}))
print("iter in tuple :", '__iter__' in dir((10,20,30)))
print("iter in dict :", '__iter__' in dir({"A":10,"B":20,"C":30}))
print("iter in range :", '__iter__' in dir(range(10,40,10)))

print("dir int :", dir(10))
print("dir str :", dir('10'))
print("dir list :", dir([10,20,30]))
print("dir set :", dir({10,20,30}))
print("dir tuple :", dir((10,20,30)))
print("dir dict :", dir({"A":10,"B":20,"C":30}))
print("dir range :", dir(range(10,40,10)))

print("#"+"-"*20+"#")

# 2. 반복 가능한 객체를 저장했다가 나중에 반복하는 방법
# __next__
a = [10,20,30].__iter__()

print("list __next__", a.__next__())
print("list __next__", a.__next__())
print("list __next__", a.__next__())
#print("list __next__", a.__next__()) # 반복할 수 있는 숫자를 넘어가면 에러 발생 (StopIteration)

a = {10,20,30}.__iter__()

print("set __next__", a.__next__())
print("set __next__", a.__next__())
print("set __next__", a.__next__())

a = (10,20,30).__iter__()

print("tuple __next__", a.__next__())
print("tuple __next__", a.__next__())
print("tuple __next__", a.__next__())

a = {"A":10,"B":20,"C":30}.__iter__()

print("dict __next__", a.__next__())
print("dict __next__", a.__next__())
print("dict __next__", a.__next__())

a = range(10,40,10).__iter__()

print("range __next__", a.__next__())
print("range __next__", a.__next__())
print("range __next__", a.__next__())

print("#"+"-"*20+"#")

# 내장함수 이용 방법 : iter, next
a = iter([10,20,30])

print("list __next__", next(a))
print("list __next__", next(a))
print("list __next__", next(a))

a = iter({10,20,30})

print("set __next__", next(a))
print("set __next__", next(a))
print("set __next__", next(a))

a = iter((10,20,30))

print("tuple __next__", next(a))
print("tuple __next__", next(a))
print("tuple __next__", next(a))

a = iter({"A":10,"B":20,"C":30})

print("dict __next__", next(a))
print("dict __next__", next(a))
print("dict __next__", next(a))

a = iter(range(10,40,10))

print("range __next__", next(a))
print("range __next__", next(a))
print("range __next__", next(a))

a = iter(range(10,40,10))

print("range __next__", next(a,100))
print("range __next__", next(a,100))
print("range __next__", next(a,100))
print("range __next__", next(a,100)) # default 값으로 100 을 주면 반복 가능한 횟수가 지나면 100을 반환

print("#"+"-"*20+"#")

# 3. 반복자 (iterator) 만들기
# class my_iterator:
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         pass
#
#     def __getitem__(self, index):
#         pass

# range(num) 와 비슷한 형태의 iterator
# class my_iterator:
#     def __init__(self, end):
#         self.start = 0          # 0 에서 시작
#         self.end = end          # 끝나는 시점은 입력으로 받음 (end - 1 까지)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             output = self.start
#             self.start = self.start + 1
#             return output
#         else:
#             raise StopIteration
#
#     def __getitem__(self, index):
#         if index < self.end:
#         else:
#             raise IndexError

# range(start, end) 와 비슷한 형태의 iterator
class my_iterator:

    def __init__(self, start, end):
        self.start = start      # 시작 시점을 입력으로 받음
        self.end = end          # 끝나는 시점은 입력으로 받음 (end - 1 까지)
        self.num = self.end - self.start
        self.my_list = range(start, end)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.num:
            output = self.my_list[self.index]
            self.index = self.index + 1
            return output
        else:
            raise StopIteration

    def __getitem__(self, item):
        for i in range(item):
            self.__next__()
        return self.__next__()

for i in my_iterator(2, 5):
    print("my_iterator :", i)

print("#"+"-"*20+"#")

a = my_iterator(2, 5)
print("my_iterator :", next(a))
print("my_iterator :", next(a))
print("my_iterator :", next(a))

print("#"+"-"*20+"#")

print("my_iterator :", my_iterator(2, 5)[0])
print("my_iterator :", my_iterator(2, 5)[1])
print("my_iterator :", my_iterator(2, 5)[2])

print("#"+"-"*20+"#")

# 4. unpacking
a, b, c = iter([10,20,30])

print("list unpacking", a, b, c)

a, b, c = iter({10,20,30})

print("set unpacking", a, b, c)

a, b, c = iter((10,20,30))

print("tuple unpacking", a, b, c)

a, b, c = iter({"A":10,"B":20,"C":30})

print("dict unpacking", a, b, c)

a, b, c = iter(range(10,40,10))

print("range unpacking", a, b, c)

# * 사용
a, *b = iter([10,20,30])

print("list unpacking *", a, *b)

# _ 사용 : unpacking 할 때 특정 순서의 값을 무시하고 싶을 때 _ 로 반환
a, b, _ = iter([10,20,30])

print("list unpacking _", a, b, _)

print("#"+"-"*20+"#")
