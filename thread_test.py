# -*- coding:utf-8 -*-

import threading
from time import ctime,sleep


#功能一
def music(func):
    for i in range(2):
        print('i am listening %s.%s'%(func,ctime()))
        sleep(1)
#功能二
def movie(func):
    for i in range(2):
        print('i watching %s,%s'%(func,ctime()))
        sleep(3)


#管理功能一和功能二
def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        movie(name)
    else:
        print('错误，不能识别的格式')

#超级播放器，同时实现功能一和功能二
def super_player(file,time):
    for i in range(2):
        print('Start playing:%s! %s'%(file,ctime()))
        sleep(int(time))

#list = ['爱情买卖.mp3','小叮当.mp4']
#改进一下，使用字典，加上时间长度参数
list = {'爱情买卖.mp3':'3','小叮当.mp4':'15','错错错.mp3':'4'}


#music('123')
#if if __name__ == "__main__":

#创建一个线程列表，把要执行的函数放在列表队列中
thread_list = []
files = range(len(list))
#创建线程
for file,time in list.items():
    t = threading.Thread(target=super_player,args=(file,time))
    thread_list.append(t)
print('****************')
print(thread_list)

#启动线程
for i in files:
    thread_list[i].start()
for i in files:
    thread_list[i].join()
    

#music('小叮咣')
#movie('武林外传')
print('all thing is done!%s'%(ctime()))