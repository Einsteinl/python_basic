#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Point:
    # 构造方法
    def __init__(self,x=2,y=9):
        self.x=x
        self.y=y

    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"销毁")

pt1=Point()
pt2=pt1
pt3=pt1
print (id(pt1),id(pt2),id(pt3))

del pt1
del pt2
del pt3