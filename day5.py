# 小魏
# 2024/5/30  17:19

#迭代器
# mytuple = ("apple","banana","cherry")
# myiter = iter(mytuple)
# 
# print(myiter)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# myit = iter("banana")
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# myit1 = "banana"
# for x in myit1:
#     print(x)

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# for x in myiter:
#   print(x)


# 作用域
# def myfunc():
#   x = 100
#   print(x)
#
# myfunc()
# print(x)

# def myfunc():
#     x=100
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
#
# myfunc()

# x = 100
#
# def myfunc():
#     x = 200
#     print(x)
#
# myfunc()
#
# print(x)


x = 100

def myfunc():
    x = 200
    print(x)


myfunc()

print(x)