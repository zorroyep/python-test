# -*- coding:utf-8 -*-

#1，冒泡排序

lis = [56,12,1,8,254,10,100,34,56,7,23,456,234,-58]
def sortport():
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j+1],lis[j] = lis[j],lis[j+1]
    return lis

#t = sortport()
#print(t)



#2，计算X的n次方的方法
def power(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s*x
    return s

#t = power(5,2)
#print(t)


#3，计算a*a+b*b+c*c+...
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum



#4,计算阶乘n!





#5,列出当前目录下的所有文件和目录名
import os
t = [d for d in os.listdir('.')]
#print(t)



#6,把一个list中所有的字符串变成小写
L = ['Hello','World','IBM','Apple']
[s.lower() for s in L]



#7,输出某个路径下的所有文件和文件夹的路径
def print_dir():
    filepath = input('请输入一个路径：')
    if filepath=="":
        print("请输入正确的路径！")
    else:
        for i in os.listdir(filepath):  #获取目录中的文件及子目录列表
            print(os.path.join(filepath,i))  #把路径组合起来
#print(print_dir())



#8,输出某个路径及其子目录下的所有文件路径
def show_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath,i))
        print(path)
        if os.path.isdir(path): #isdir()判断是否是目录
            show_dir(path)      #如果是目录，使用递归方法
filepath = "d:\mib"
#show_dir(filepath)



#9,输出某个路径及其子目录下所有以.html为后缀的文件
def print_html(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath,i)
        if os.path.isdir(path):
            print_html(path)
        if path.endswith(".html"):
            print(path)
filepath = "D:\MyDocuments\python\pratise"
#print_html(filepath)



#10,把原字典的键值对颠倒并生产新的字典
dict1 = {"A":"a","B":"b","C":"c"}
dict2 = {y:x for x,y in dict1.items()}
#print(dict2)



#11,打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        pass
        #print('{}x{}={}\t'.format(i,j,i*j),end='')
    #print()



#12,替换列表中所有的3为3a
num = ['harden','lampard',3,34,45,39,29,40,3241,10001]
for i in range(num.count(3)):#获取3出现的次数
    #print(i)
    ele_index = num.index(3)    #获取首次3出现的坐标
    num[ele_index]="3a"         #修改3为3a
#print(num)


#13,打印列表中的每一项
namelist = ["James","Meng","Xin"]
for i in range(len(namelist)):
    pass
    #print('hello,{}'.format(namelist[i]))




#14,合并去重
list1 = [2,3,8,4,9,5,6]
lsit2 = [5,6,10,17,11,2]
list3 = list1 + lsit2
#print(list3) #不去重只进行两个列表的组合
#打印结果：[2, 3, 8, 4, 9, 5, 6, 5, 6, 10, 17, 11, 2]
#print(set(list3))   #去重，类型为set需要转换成list，集合中不存在相同的元素
#打印结果：{2, 3, 4, 5, 6, 8, 9, 10, 11, 17}    注意集合是大括号，已经去重
#print(list(set(list3)))
#打印结果：[2, 3, 4, 5, 6, 8, 9, 10, 11, 17]    注意列表是中括号



#15,随机生成验证码的两种方式
import random
list1 = []
for i in range(65,91):
    list1.append(chr(i)) #通过for循环遍历ascii码并追加到空列表中
for j in range(97,123):
    list1.append(chr(j))
for k in range(48,58):
    list1.append(chr(k))
ma = random.sample(list1,6)
#print(ma)
ma = ''.join(ma)
#print(ma)

import string
str1 = '0123456789'
str2 = string.ascii_letters #string.ascii_letters包含所有字母（大写或小写）的字符串
str3 = str1 + str2
ma1 = random.sample(str3,6)
ma1 = ''.join(ma1)
#print(ma1)


#16,计算平方根
'''
num = float(input('请输入一个数字：'))
num_sqrt = num**0.5
print('{:.2f}的平方根为{:.2f}'.format(num,num_sqrt))
'''




#17,判断字符串是否只由数字组成
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass 
    return False



#18,判断奇偶数
'''
num = int(input("输入一个数字："))
if (num % 2)==0:
    print("{0}是偶数".format(num))
else:
    print("{0}是奇数".format(num))
'''



#
'''
     _____________
    /_________   /       
             /  /
            /  /
           /  /
          /  /
         /  /
        /  /
       /  /
      /  /__________
     /_____________/


'''


#19,判断闰年
'''
year = int(input("请输入一个年份："))
if (year % 4)==0 and (year % 100) != 0 or (year % 400)==0:
    print("{0}是闰年。".format(year))
else:
    print("{0}不是闰年。".format(year))
'''



#20,获取最大值 
'''
N = int(input('输入需要对比大小数字的个数：\n'))
num = [int(input('请输入第{0}个对比数字：\n'.format(i))) for i in range(1,N+1)]
print('您输入的数字为：{0}'.format(num))
print('最大值为：{0}'.format(max(num)))
'''


#21,斐波那契数列
'''
斐波那契数列指的是这样的一个数列0,1,1,2,3,5,8,13;
特殊指出：第0项是0，第1项是第一个1。
从第三项开始，每一项都等于前两项之和

'''
#判断输入的值是否合法
'''
nterms = int(input("请输入一个整数：")) #这个数是数列的层数
n1 = 0
n2 = 1
if nterms <=0:
    print("请输入一个正整数:")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("契波那契数列：")
    print(n1,",",n2,end=",")
    count = 1
    while count < nterms:
        nth = n1 + n2
        print(n1+n2,end=",")
        #更新值
        n1 = n2
        n2 = nth
        count += 1
'''



#22,十进制转二进制、八进制、十六进制
'''
dec = int(input("请输入一个整数："))
print("十进制数为：{0}".format(dec))
print("转换为二进制为：{0}".format(bin(dec)))
print("转换为八进制为：{0}".format(oct(dec)))
print("转换为十六进制为：{0}".format(hex(dec)))
'''

#23,最大公约数
'''
def hcf(x,y):
    #该函数返回两个数的最大公约数
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if ((x % i)==0 and (y % i)==0):
            hcf = i
    return hcf

#用户输入两个数字 
num1 = int(input("输入第一个正整数："))
num2 = int(input("输入第二个正整数："))
print("{0}和{1}的最大公约数为是{2}".format(num1,num2,hcf(num1,num2)))
'''


#24,最小公倍数
'''
def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if((greater % x)==0 and (greater % y)==0 ):
            lcm = greater
            break
        greater +=1
    return lcm

#用户输入两个数字 
num1 = int(input("输入第一个正整数："))
num2 = int(input("输入第二个正整数："))
print("{0}和{1}的最小公约数为是{2}".format(num1,num2,lcm(num1,num2)))
'''


#25,生成日历
#引入日历模块
'''
import calendar
#输入指定年月
yy = int(input("请输入年份："))
mm = int(input("请输入月份："))

#显示日历
print(calendar.month(yy,mm))
'''



#26,文件I/O
#写文件
'''
with open("test.txt",'wt') as out_file:
    out_file.write("把这句话写到文件中。")

#读文件
with open("test.txt",'rt') as in_file:
    text = in_file.read()
print(text)
'''


#27,字符串判断
#测试实例一
print("测试实例一")
str = "zoroo.com"
print(str.isalnum())#判断所有字符是否都是数字
print(str.isalpha())#判断所有字符是否都是字母
print(str.isdigit())#判断所有字符是否都是数字
print(str.islower())#判断所有字符是否都是小写
print(str.isupper())#判断所有字符是否都是大写
print(str.istitle())#判断所有单词是否都是首字母大写
print(str.isspace())#判断所有字符是否都是空白字符，包括\t,\n,\r
print("-------------------------------------")

#测试实例二
print("测试实例二")
str = "Bake corN"
print(str.isalnum())#判断所有字符是否都是数字
print(str.isalpha())#判断所有字符是否都是字母
print(str.isdigit())#判断所有字符是否都是数字
print(str.islower())#判断所有字符是否都是小写
print(str.isupper())#判断所有字符是否都是大写
print(str.istitle())#判断所有单词是否都是首字母大写
print(str.isspace())#判断所有字符是否都是空白字符，包括\t,\n,\r
print("-------------------------------------")



#28,字符串大小写，转换
str = "https://www.baidu.com/tieba/"
print(str.upper())#把所有字符串的小写字母转换成大写字母
print(str.lower())#把所有字符串的大写字母转换成小写字母
print(str.capitalize())#把第一个字符转化为大写字母，其余小写
print(str.title())#把每一个单词的第一个字母转化为大写，其余小写


#29,计算第个月天数
import calendar
monthRange = calendar.monthrange(2019,2)
print(monthRange)


#30,获取昨天的日期
#引入datetime模块
import datetime
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

print(getYesterday())