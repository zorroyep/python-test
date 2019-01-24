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

t = power(5,2)
print(t)