# 小魏
# 2024/5/27  10:17

# thistuple=('apple','banana','cherry')
# print(thistuple[1])
# x=list(thistuple)
# x[1]='1'
# thistuple=tuple(x)
# print(thistuple)
# if "apple1" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
# else:
#     print('111')
#
# thistuple = ("apple",)
# print(type(thistuple))
#
# #不是元组
# thistuple = ("apple")
# print(type(thistuple))
#
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
#
# tuple3 = tuple1 + tuple2
# print(tuple3,type(tuple3))


# thisset = {"apple", "apple", "banana", "cherry"}
# print(thisset)
thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
#
# # thisset.add("123")
# thisset.update({"123", "456"})
# print(thisset)
# print(len(thisset))

# thisset.discard('1')
#
# print(thisset)
# thisset.clear()
# thisset.add(1)
# del thisset
# print(thisset)
# set1={"a","b","c",1,2}
# set2={1,2,3}
# set3=set2.copy()
# # set3 = set1.union(set2)
# # set1.update(set2)
# set2.difference(set1)
# print(set1)

thisdict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}


# print(thisdict)
# x=thisdict["year"]
# print(x)
# y=thisdict.get("year")
# print(y)
#
# for a in thisdict:
#     print(thisdict[a])
#
# for a in thisdict.values():
#     print(a)
#
# for x, y in thisdict.items():
#     print(x, y)
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# print(len(thisdict))
#
# thisdict["color"]="red"
# print(thisdict)
#
# thisdict.popitem()
# print(thisdict)
# mydict=thisdict.copy()
# mydict2=dict(thisdict)
# print(mydict)
# print("mydict2",mydict2)

# myfamily = {
#   "child1" : {
#     "name" : "Phoebe Adele",
#     "year" : 2002
#   },
#   "child2" : {
#     "name" : "Jennifer Katharine",
#     "year" : 1996
#   },
#   "child3" : {
#     "name" : "Rory John",
#     "year" : 1999
#   }
# }
# print(myfamily)

#
# child1 = {
#   "name" : "Phoebe Adele",
#   "year" : 2002
# }
# child2 = {
#   "name" : "Jennifer Katharine",
#   "year" : 1996
# }
# child3 = {
#   "name" : "Rory John",
#   "year" : 1999
# }
# myfamily={
#     "child1":child1,
#     "child2":child2,
#     "child3":child3,
# }
# for x,y in  myfamily.items():
#     print(x,y)
# # print(myfamily)

# thisdict = dict(brand="Porsche", model="911", year=1963)
# # 请注意，关键字不是字符串字面量
# # 请注意，使用了等号而不是冒号来赋值
# print(thisdict)


# a = 66
# b = 200
# if b > a:
#     print("b is greater than a") # 会报错

# i = 1
# while i < 7:
#   print(i)
#   i += 1

# i = 1
# while i < 7:
#   print(i)
#   if i == 3:
#     continue
#   i += 1
#
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# for x in "banana":
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# for x in range(3,10,2):
#   print(x)
# else:
#   print("Finally finished!")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x,"   ",y)

# def myfunction():
#   print("Hello from function")
#
# myfunction()
#
# def name(fname):
#   print(fname + "Gates")
#
# name("Bill  ")

def my_function(country="China"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)
