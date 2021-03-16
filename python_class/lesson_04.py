# 函数
'''
def good_jod(a,b,c,*args):
    sum1 = a+b+c
    for i in args:
     sum1 +=i
     return sum1
result = good_jod(1,2,3,3,1,2)

'''
str = "abcdef"

def add_fun():
    sum = 0
    num = int(input("请输入任意整数："))
    for i in range(10):
        sum += i
    print("结果是"+sum)
    add_fun()