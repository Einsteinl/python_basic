#!/usr/bin/python
# -*- coding: UTF-8 -*-
def outfunc(func,x,y):
    c=func(x,y)
    print(c)

# 这里的lambda关键字是声明匿名函数的
outfunc(lambda x,y:x+y,1,2)







