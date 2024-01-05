# def somefuncg():#generator
#     count = 1
#     for i in range(1, 10):
#         yield count
#         count *= i

# a = somefuncg()

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# for i in somefuncg():
#     print(i)
# def somefuncn():#normal function
#     return 1
    # return 2

# print(somefuncn())
# a = somefuncg()

# print(a)

# for i in somefuncg():
#     print(i)

# for j in somefunc():
#     print(j)
# print(somefunc())
# print(somefunc())
# print(somefunc())

# for j in a:
#     print(j)

# print(a)
# 1
# 3
# 9
# 27
# 81
# .
# .
# .

class Odam:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.age == __value.age

ali = Odam("Ali", 20)
ali2 = Odam("Ali", 20)

print(id(ali), id(ali2))

if ali == ali2:
    print("ikkisi ham bir odam")
else:
    print("bir odam emas bular")