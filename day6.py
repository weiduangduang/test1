# 小魏
# 2024/5/31  10:32

# import platform
# from  mymodule import person1

# # greeting("Bill")
# a = person1["country"]
# print(a)
# print(dir(person1))
# x = platform.system()
#
# print(x)
# print(dir(platform))
# print(platform)

# Python 日期
# import datetime
#
# x = datetime.datetime.now()
# print(datetime)
# print(datetime.datetime)
# print(datetime.datetime.now)
# print(x)
# print(x.year)
# print(x.strftime("%Z"))
# print(x.month)
# print(x.weekday())
#
# y = datetime.datetime(2024,6,1,13,20,55,999)
# print(y)

# import json
#
# x = '''{
#     "readme": {
#         "encryptMode": "加密模式",
#         "isencrypt": "是否加密",
#         "isAutoLogin": "登录模式 0账号密码登录 1授权登录失败账号密码登录 2授权登录失败不显示账号密码 3网关自动登录",
#         "isPlateform": "是否平台模式 1是 0否",
#         "loginurl": "系统登录地址",
#         "apiVersion": "网络请求基地址 默认空",
#         "appName": "系统名称",
#         "appHomeName": "系统登录名称",
#         "projectName": "项目名称",
#         "autoLoginName": "授权登录系统名称",
#         "copyright": "版权",
#         "technicalSupport": "技术支持",
#         "timeoutPeriod": "请求超时时间/秒",
#         "logo": "登录LOGO名称",
#         "fileBaseUrl": "附件请求基地址 默认空",
#         "fileDownload": "附件下载 most 0不下载 1下载",
#         "isca": "启用CA 0不启用 1北京CA 2医网信CA"
#     },
#     "encryptMode": "1",
#     "isencrypt": "1",
#     "isAutoLogin": 1,
#     "isPlateform": 0,
#     "loginurl": "http://enterprise.kaiserestful.cn:8080/CMSMobile1/#/",
#     "apiVersion": "/dev",
#     "appName": "智慧运营管理",
#     "appHomeName": "智慧运营管理信息平台",
#     "projectName": "合同系统",
#     "autoLoginName": "合同管理",
#     "copyright": "Copyright @2023 XXXX医院",
#     "technicalSupport": "技术支持:南京凯唱软件有限公司",
#     "timeoutPeriod": 30,
#     "logo": "kaiser-logo.png",
#     "fileBaseUrl": "",
#     "fileDownload": 0,
#     "isca": "2"
# }'''
#
# y = json.loads(x)

# print(y["readme"])
# print(y["readme"]["isca"])
# print(y["readme"]["encryptMode"])
# print(y["encryptMode"])

# for a,b in y["readme"].items():
#     print(a,b)

# for x in y.values():
#   print(x)

# print(len(y["readme"]))

# x = {
#   "name": "Bill",
#   "age": 63,
#   "city": "Seatle"
# }
#
# # 转换为 JSON：
#
# y = json.dumps(x)
#
# # 结果是 JSON 字符串：
# print(y)

# print(json.dumps({"name": "Bill", "age": 63}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json
#
# x = {
#   "name": "Bill",
#   "age": 63,
#   "married": True,
#   "divorced": False,
#   "children": ("Jennifer","Rory","Phoebe"),
#   "pets": None,
#   "cars": [
#     {"model": "Porsche", "mpg": 38.2},
#     {"model": "BMW M5", "mpg": 26.9}
#   ]
# }
#
# print(json.dumps(x,indent=4))
# print(json.dumps(x,indent=4,sort_keys=True))
# print(json.dumps(x,indent=4,separators=(";","=")))

# import re
# txt = "China is a great country,balabala"
# x = re.search("^China.*country$",txt)
# x1 = re.search("^China.*country,b",txt)
# print(x)
# print(x1)

# import re
#
# str = "China is a great country"
# x = re.findall("na", str)
# print(x)
# x1 = re.findall("USA", str)
# print(x1)

# import re
#
# str = "China is a great country"
# x = re.search("\s", str)
# x1=re.search("China", str)
# x2=re.search("china", str)
# x3=re.search("USA", str)
#
# print("The first white-space character is located in position:", x.start())
# print("x1",x1)
# print("x2",x2)
# print("x3",x3)

import re

str = "China is a great country"
x = re.split("\s", str,1)
y = re.sub("\s", "9", str,2)
print(x)
print(y)

z = re.search(r"\bC\w+", str)
print(z)
print(z.span())
print(z.group())
print(z.string)
print(z.string)