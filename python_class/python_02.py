# name = input("请输入姓名")
# age = input("请输入年龄")
# sex = input("请输入性别")
#
# print('''************
#         姓名：{}
#         年龄：{}
#         性别：{}
#         ************
# '''.format(name,age,sex))


str = " python hello  aaa 123123aabb"


print(str[0:7])
print('o a' in str)
print('he' in str)
print('ab' in str)

str = str.replace("python","lemon")
print(str)
print(str.find("aaa"))
