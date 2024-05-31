# # 小魏
# # 2024/5/24  14:55
#
# x = "awesome"
#
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)

# x = "awesome"
#
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)

# x = 6666666666666666666666666666666666666666666666666666666666666666666666666
# print(x)
# print(type(x))

#
# x = 27e4
# y = 15E2
# z = -49.8e100
#
#
# x = 2+3j
# y = 7j
# z = -7j
#
# print(x)
# print(type(x))
# print(y)
# print(type(y))
# print(z)
# print(type(z))
#
# x = 10 # int
# y = 6.3 # float
# z = 1j # complex
#
# # 把整数转换为浮点数
#
# a = float(x)
#
# # 把浮点数转换为整数
#
# b = int(y)
#
# # 把整数转换为复数：
#
# c = complex(x)
#
# print(a)
# print(b)
# print(c)
#
# print(type(a))
# print(type(b))
# print(type(c))

#
# import random
#
# print(random.randrange(1,100,5))
#
# a = """Python is a widely used general-purpose, high level programming language.
# It was initially designed by Guido van Rossum in 1991
# and developed by Python Software Foundation.
# It was mainly developed for emphasis on code readability,
# and its syntax allows programmers to express concepts in fewer lines of code."""
# print(a)
#
# b = "Hello, World!"
# print(b[2:5])
#
# b = "Hello, World!"
# print(b[-5:-2])
# print(b[2:5:-1])

# a = " Hel lo, Wo rld!  "
# print(a.strip())
# print(a.strip().lower())
# print(a.strip().lower().upper())
# print(a.replace("World", "高宇大傻子哦"))
# print(a.split())
# print(a.split(" "))
#
# txt = "China is a great country"
# x = " ina " in txt
# print(x)

# a = "Hello"
# b = "World"
# c = a + b
# print(c)
#
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# age = 63
# txt = "My name is Bill, I am " + str(age)
# print(txt)

# age = 63
# txt = "My name is Bill, and I am {}"
# print(txt.format(age))
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {2} pieces of item {1} for {3} dollars."
#
# myorder1=myorder.format(quantity, itemno, price,"1")
# print(myorder1.center(100))
# print(myorder1.encode(encoding="utf-8", errors="replace"))
#
# txt = "My name is Ståle"
#
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# print(txt.encode(encoding="ascii",errors="strict"))
txt = "     banana     "

# x = txt.rstrip()
#
# print("of all fruits", x, "is my favorite")

# txt = "banana,,,,,ssaaww....."
#
# x = txt.rstrip(",.asw")
#
# print(x)
# print(bool("Hello"))
# print(bool(10))

# class myclass():
#   def __len__(self):
#     return 0
#
# myobj = myclass()
# print(bool(myobj))
#
# x = 200
# print(isinstance(isinstance(x, bool),bool))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#
# print(thislist)
# print(thislist[1])
# print(thislist[-1])
# print(thislist[2:5])
# print(thislist[-4:])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "mango"
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# if "apple"  not in thislist:
#   print("Yes, 'apple' is in the fruits list")
#   print(len(thislist))
# thislist.insert(1,'aaaa')
# thislist.append('bbb')
# thislist.remove('apple')
# print(thislist)
# thislist.pop(1)
# print(thislist)
# del thislist[1]
# print(thislist)
# thislist.clear()
# print(thislist)
# print(len(thislist))

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# thislist.insert(1,'aaaa')
# print(thislist)
# print(mylist)
#
# thislist = ["apple", "banana", "cherry"]
# mylist2 = list(thislist)
# thislist.insert(1,'bbb')
# print(thislist)
# print(mylist2)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# list3 = list1 + list2
# print(list3)
#
# for x in list2:
#     list1.append(x)
# print("list1为", list1)

# list1=["a","b","c"]
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)
thislist = list({"apple", "banana", "cherry", 1}) # 请注意双括号
print(thislist)
thislist1 = list({"apple", "banana", "cherry", 1}) # 请注意双括号
print(thislist1)
thislist2 = list({"apple", "banana", "cherry", 1}) # 请注意双括号
print(thislist2)