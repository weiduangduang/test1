# 小魏
# 2024/5/28  10:18

# def mul(x):

#     return x * 5
#
#
# y = mul(5)
# print(mul(10))
#
#
# def my_function(child3, child2, child1):
#     return "The youngest child is" + child3
#
#
# print(my_function(child1="111", child2="2qwer", child3='2222'))
#
#
# def printtulpe(*t):
#     for x in t:
#         print(x)
#
# printtulpe("1","a","aaa","asdfasdf")
# printtulpe(1,2,"a")

# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print("\n\nRecursion Example Results")
# tri_recursion(996)


# x = lambda a : a + 10
# print(x(5))
#
# x = lambda a, b : a * b
# print(x(5, 6))
#
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))
#
# class Myclass:
#     x=5
#
# p1=Myclass()
# print(p1.x)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#
# p1=Person("Bill",28)
# p1.myfunc()
# p1.age=39
# print(p1)
# del p1
# print(p1.age)